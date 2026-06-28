#!/bin/bash

############################################################################
#
#    Agno Railway Setup (first-time provisioning)
#
#    Usage:     ./scripts/railway/up.sh
#    Redeploy:  ./scripts/railway/redeploy.sh
#    Sync env:  ./scripts/railway/env-sync.sh
#
#    Prerequisites:
#      - Railway CLI installed
#      - Logged in via `railway login`
#      - OPENAI_API_KEY set in environment (or .env / .env.production)
#
############################################################################

set -e

# Colors
ORANGE='\033[38;5;208m'
DIM='\033[2m'
BOLD='\033[1m'
NC='\033[0m'

echo ""
echo -e "${ORANGE}"
cat << 'BANNER'
     █████╗  ██████╗ ███╗   ██╗ ██████╗
    ██╔══██╗██╔════╝ ████╗  ██║██╔═══██╗
    ███████║██║  ███╗██╔██╗ ██║██║   ██║
    ██╔══██║██║   ██║██║╚██╗██║██║   ██║
    ██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝
BANNER
echo -e "${NC}"

# Load env file — .env.production preferred for Railway, .env as fallback
if [[ -f .env.production ]]; then
    set -a
    source .env.production
    set +a
    echo -e "${DIM}Loaded .env.production${NC}"
elif [[ -f .env ]]; then
    set -a
    source .env
    set +a
    echo -e "${DIM}Loaded .env${NC}"
fi

# Preflight
if ! command -v railway &> /dev/null; then
    echo "Railway CLI not found. Install: https://docs.railway.app/guides/cli"
    exit 1
fi

if [[ -z "$OPENAI_API_KEY" ]]; then
    echo "OPENAI_API_KEY not set. Add to .env (or .env.production) or export it."
    exit 1
fi

if [[ -z "$OLLAMA_API_KEY" ]]; then
    echo "OLLAMA_API_KEY not set. The default model (glm-5.2:cloud) authenticates"
    echo "to https://ollama.com via this key. Add to .env (or .env.production) or export it."
    exit 1
fi

echo -e "${BOLD}Initializing project...${NC}"
echo ""
railway init -n "petes-agno" 2>/dev/null || echo -e "${DIM}Project already initialized${NC}"

echo ""
echo -e "${BOLD}Deploying PgVector database...${NC}"
echo ""
railway add -s pgvector -i agnohq/pgvector:18 \
    -v "POSTGRES_USER=${DB_USER:-ai}" \
    -v "POSTGRES_PASSWORD=${DB_PASS:-ai}" \
    -v "POSTGRES_DB=${DB_DATABASE:-ai}"

echo ""
echo -e "${BOLD}Adding database volume...${NC}"
railway service link pgvector
railway volume add -m /var/lib/postgresql 2>/dev/null || echo -e "${DIM}Volume already exists or skipped${NC}"

echo ""
echo -e "${DIM}Waiting 15s for database...${NC}"
sleep 15

echo ""
echo -e "${BOLD}Creating application service...${NC}"
echo ""
# Forward every relevant env var the first deploy might need. Optional
# keys are only included when set — Railway CLI rejects empty values.
# Use ./scripts/railway/env-sync.sh to sync the rest from .env later.
# RUNTIME_ENV=dev disables JWT authorization for the initial deploy.
# Switch to prd (and set JWT_VERIFICATION_KEY) once you're ready to gate
# the API. See AGENTS.md → Environment Variables.
RAILWAY_VARS=(
    -v "DB_USER=${DB_USER:-ai}"
    -v "DB_PASS=${DB_PASS:-ai}"
    -v "DB_HOST=pgvector.railway.internal"
    -v "DB_PORT=${DB_PORT:-5432}"
    -v "DB_DATABASE=${DB_DATABASE:-ai}"
    -v "DB_DRIVER=postgresql+psycopg"
    -v "WAIT_FOR_DB=True"
    -v "PORT=8000"
    -v "RUNTIME_ENV=dev"
    -v "OPENAI_API_KEY=${OPENAI_API_KEY}"
    -v "OLLAMA_API_KEY=${OLLAMA_API_KEY}"
)
[[ -n "$PARALLEL_API_KEY" ]] && RAILWAY_VARS+=(-v "PARALLEL_API_KEY=${PARALLEL_API_KEY}")

railway add -s agent-os "${RAILWAY_VARS[@]}"

echo ""
echo -e "${BOLD}Deploying application...${NC}"
echo ""
railway up --service agent-os -d

echo ""
echo -e "${BOLD}Creating domain...${NC}"
echo ""
railway domain --service agent-os

echo ""
echo -e "${BOLD}Done.${NC} Domain may take ~5 minutes."
echo -e "${DIM}Logs:           railway logs --service agent-os${NC}"
echo -e "${DIM}Sync env vars:  ./scripts/railway/env-sync.sh  (defaults to .env.production)${NC}"
echo ""
