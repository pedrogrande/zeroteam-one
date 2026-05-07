# Improve an Agent

> Claude Code prompt. Open Claude Code in this repo and paste:
> `Run docs/improve-agent.md`

You are iterating on a live agent against a running AgentOS container. The platform is on `http://localhost:8000` with hot-reload enabled (`RUNTIME_ENV=dev`), so edits to `agents/<slug>.py` are picked up by uvicorn within ~1s. No rebuild, no restart.

This is a **single-pass** improvement loop, not a recurring scheduled run. One pass usually takes 10-15 minutes. Re-run if the user is still unhappy.

## 0. Preconditions

- `agentos-api` running: `docker compose ps`. If not, ask the user to `docker compose up -d --build` first.
- `curl -sSf http://localhost:8000/health` returns 200.
- Recommend the user create a feature branch before starting (`git checkout -b improve/<agent-slug>-$(date +%Y%m%d)`) so any wrong turns are easy to revert.

## 1. Define test cases

Ask the user:

1. **Which agent?** (slug — e.g. `web-search`)
2. **What is it doing wrong?** Describe the failure mode in their own words.
3. **Three to five concrete inputs** the agent should handle, with the **expected behavior** for each.

Example shape:

```
Agent: web-search
Failure: vague answers, no citations, doesn't drill into pages.
Cases:
  1. "what changed in Anthropic's research this week?"
     Expected: at least one web_fetch on a real source; cites URLs.
  2. "find the top 3 recent articles about Mistral's new models"
     Expected: 3 sources, all URLs that resolve.
  3. "what's the latest on OpenAI's o-series?"
     Expected: cites source dates from the past 60 days.
```

Lock these in before touching any code.

## 2. Run the cases against the live agent

For each case, send a probe via cURL and capture the response:

```bash
curl -sS -X POST http://localhost:8000/agents/<slug>/runs \
  -F "message=<the prompt>" \
  -F "user_id=claude-improve" \
  -F "stream=false" \
  -o /tmp/probe-1.json \
  -w "HTTP %{http_code} in %{time_total}s\n"

jq -r '.content // .' < /tmp/probe-1.json
```

For multi-turn cases, capture `session_id` from the first response and pass `-F "session_id=<id>"` on the next call:

```bash
SID=$(jq -r '.session_id' < /tmp/probe-1.json)
curl ... -F "session_id=$SID" ...
```

Save each response to `/tmp/probe-<n>.json` so you can compare before vs. after.

## 3. Read the result

Look at three things:

1. **The response itself** — does it match the expected behavior?
2. **Which tools fired** — read the container logs:
   ```bash
   docker logs agentos-api --since 30s 2>&1 | grep -E "Tool Calls|Running:|Error" | head -40
   ```
   "Tool Calls" lines tell you which tools the agent chose; arguments are inline.
3. **Any errors** — rate limits, missing API keys, MCP server timeouts. Surface these to the user immediately if they explain the failure.

For the example: if the agent only called `web_search` once and never `web_fetch`, the instructions don't push hard enough on drilling into pages.

## 4. Edit the agent

One file: `agents/<slug>.py`. Surgical edits only — pick **one** lever and change it:

- **Instructions** — most fixes live here. Tighten or add a rule. Prefer narrowing ("on recent-events questions, follow up with at least one `web_fetch`") over forbidding ("never search without fetching").
- **Tools** — add or remove a tool. Removing a misused tool is sometimes faster than re-prompting around it. To add a new agno toolkit, look it up via the `agno-docs` MCP (configured in [`.mcp.json`](../.mcp.json)) so you get the right import path and constructor args.
- **Context provider** — swap mode (e.g. `agent` → `tools`) if the routing layer is the problem.
- **Model** — bump if the agent is genuinely under-capable. Last resort.
- **`num_history_runs`** — raise if the agent is losing context across turns; lower if old turns are leaking into new ones.

Keep edits short. If you add more than ~5 lines of instruction in one pass, you're probably bolting; back up and try removing instead.

## 5. Hot-reload picks up the change

The dev compose mounts `.:/app` and runs `uvicorn --reload --reload-dir agents …`. Save the file, wait ~2 seconds, you're done. No rebuild, no restart.

## 6. Re-run the test cases

Re-send each probe from Step 2. Compare the new responses to the old ones (the `/tmp/probe-<n>.json` files from before). Did the failures pass this time? Did anything previously passing regress?

## 7. Iterate

If all cases pass: tell the user, suggest committing on the feature branch (`git add -p && git commit -m "improve(<slug>): <one-line summary>"`), and stop. For a regression check across the full eval suite, see [`docs/run-evals.md`](run-evals.md).

If some still fail: pick the next lever and edit again. Cap at three attempts on the same pattern — if the third attempt still fails, the issue may not be prompt-shaped (could be a tool capability gap, a model limit, or a missing data source). Surface that finding to the user; don't keep grinding.

---

## A worked example (lifted from the blog post)

Your WebSearch Agent fails on "what changed in Anthropic's research this week?". The response is a vague summary with no citations.

You probe it. Container logs show the agent called `web_search` once, got back stale snippets, stopped. Never called `web_fetch`.

You edit `agents/web_search.py` and add one rule to the instructions:

```
When the user asks about recent events or specific pages, follow up with
at least one `web_fetch` to read the most relevant source before answering.
```

Hot-reload kicks in. You re-run the probe. Now the agent calls `web_search`, then `web_fetch` on the top result, and answers with a real citation. One-line fix, single iteration.

That's the loop. Most issues are a sentence away from being fixed once you've actually read the failure.
