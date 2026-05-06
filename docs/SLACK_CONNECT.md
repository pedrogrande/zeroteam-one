# Connecting AgentOS to Slack

AgentOS can live in Slack as a teammate. Each Slack thread becomes an independent session, so follow-ups in the same thread carry context forward automatically.

The default wiring in [`app/main.py`](../app/main.py) routes Slack messages to the WebSearch agent. You can swap `agent=web_search` for any other agent (or a team / workflow) once you have one ready.

## Prerequisites

- AgentOS running locally or deployed (see the [README](../README.md))
- A Slack workspace with admin privileges
- [ngrok](https://ngrok.com) installed (for local development only)

## Step 1: Get your URL

You need a public URL that Slack can reach. If you're running locally, use ngrok to expose your local server.

### Local development

```bash
ngrok http 8000
```

Copy the `https://` URL from the output — you'll paste it into the manifest next.

### Production

Use your deployed URL (e.g. `https://your-app.up.railway.app`).

## Step 2: Create a Slack App

1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Click **Create New App**
3. Select **From an app manifest**
4. Select your workspace
5. Choose **JSON** and paste the manifest below — replace `https://your-url` with the URL from Step 1
6. Click **Create**

```json
{
    "display_information": {
        "name": "AgentOS",
        "description": "A multi-agent platform that lives in Slack.",
        "background_color": "#000000"
    },
    "features": {
        "app_home": {
            "home_tab_enabled": false,
            "messages_tab_enabled": true,
            "messages_tab_read_only_enabled": false
        },
        "bot_user": {
            "display_name": "AgentOS",
            "always_online": true
        }
    },
    "oauth_config": {
        "scopes": {
            "bot": [
                "app_mentions:read",
                "assistant:write",
                "channels:history",
                "channels:read",
                "chat:write",
                "chat:write.customize",
                "chat:write.public",
                "files:read",
                "files:write",
                "groups:history",
                "groups:read",
                "im:history",
                "im:read",
                "im:write",
                "mpim:read",
                "users:read",
                "users:read.email"
            ]
        }
    },
    "settings": {
        "event_subscriptions": {
            "request_url": "https://your-url/slack/events",
            "bot_events": [
                "app_mention",
                "message.channels",
                "message.groups",
                "message.im"
            ]
        },
        "org_deploy_enabled": false,
        "socket_mode_enabled": false,
        "is_hosted": false,
        "token_rotation_enabled": false
    }
}
```

The manifest configures scopes, events, and app home settings in one shot.

## Step 3: Install to Workspace

After creating the app:

1. Go to **Install App** in the sidebar
2. Click **Install to Workspace**
3. Click **Allow** to authorize

Copy the **Bot User OAuth Token** shown after install — you'll need it next.

## Step 4: Set Environment Variables

Copy the credentials into your `.env` (or `.env.production` for Railway):

```bash
# Bot User OAuth Token (from Step 3)
SLACK_BOT_TOKEN=xoxb-***

# Signing Secret (Basic Information → App Credentials)
SLACK_SIGNING_SECRET=***
```

Restart AgentOS so it picks up the credentials:

```bash
# Local
docker compose up -d

# Railway
./scripts/railway/env-sync.sh && ./scripts/railway/redeploy.sh
```

## Verify

Two ways to chat in Slack:

**Direct message** — find the app under **Apps** in the Slack sidebar and message it directly:

```
hi
what are the latest developments in AI agents?
```

**In a channel** — invite it first, then mention it:

```
/invite @AgentOS
@AgentOS what's the latest research on LLM agents?
```

Each thread keeps its own conversation. Follow-up messages in the same thread don't need to mention `@AgentOS` again.

## How it works

The Slack interface is wired conditionally in [`app/main.py`](../app/main.py):

```python
if SLACK_BOT_TOKEN and SLACK_SIGNING_SECRET:
    interfaces.append(
        Slack(
            agent=web_search,
            streaming=True,
            token=SLACK_BOT_TOKEN,
            signing_secret=SLACK_SIGNING_SECRET,
            resolve_user_identity=True,
        )
    )
```

Thread timestamps become session IDs, so each Slack thread is an independent conversation with full history. `resolve_user_identity=True` maps Slack user IDs to names so the agent addresses you by name.

The interface is only instantiated when both env vars are set — leave them unset to run AgentOS without Slack.

## Other interfaces (Discord, Telegram, WhatsApp, custom UIs)

The agno docs cover every interface AgentOS supports — see [agno interfaces overview](https://docs.agno.com/agent-os/interfaces/overview). The wiring pattern is the same: import the interface class, gate it on the relevant env vars, append to `interfaces=[…]`.

When the same person reaches the agent across surfaces (Slack today, web tomorrow), you'll want to map each surface's user ID to a canonical `user_id`. The blog post leaves the implementation as an exercise; the pattern is an identity table with one row per `(surface, surface_user_id)` pointing at the same canonical user.
