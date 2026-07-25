# Polytoken Hooks

**Canonical URL:** https://docs.polytoken.dev/harness-engineering/hooks/

## Where hooks live

Polytoken reads `hooks.json` from two places:

- Global: `hooks.json` in the Polytoken config directory
- Project: `.polytoken/hooks.json`

Global entries load first, then project entries append. Polytoken validates the file at load time and rejects unknown events, malformed matchers, or unknown handler keys.

## Format

A JSON array of hook entries:

```json
[
  {
    "name": "log-edits",
    "event": "post_tool_use",
    "matcher": "file_edit_*",
    "handler": { "bash": "jq -r .tool_name >> /tmp/polytoken-edits.log" }
  }
]
```

| Field | Required | Description |
|---|---|---|
| `name` | yes | Identifier used in logs and negation syntax |
| `event` | yes | Lifecycle event name |
| `matcher` | no | Glob narrowing which instances fire |
| `handler` | yes | Object containing the code to run |

## Events

Blocking events wait for the handler and act on the result. Fire-and-forget events run in the background.

| Event | Waits | Fires |
|---|---|---|
| `session_start` | yes | Session begins |
| `pre_user_prompt` | yes | Before a user prompt is recorded |
| `pre_model_turn` | yes | Before a model turn |
| `post_model_turn` | no | After a model turn finishes |
| `pre_tool_use` | yes | Before a tool runs |
| `post_tool_use` | no | After a tool succeeds |
| `post_tool_use_failure` | no | After a tool fails |
| `stop` | yes | When the model would hand back to the user |
| `pre_compaction` | yes | Before compaction |
| `post_compaction` | yes | After compaction |
| `notification` | yes | When a notification would be raised |
| `facet_switch` | no | After the active facet changes |
| `subagent_start` | no | After a subagent starts |
| `subagent_stop` | no | After a subagent finishes |

## Environment variables

Polytoken sets `POLYTOKEN_*` variables for every handler, including `POLYTOKEN_HOOK_EVENT`, `POLYTOKEN_HANDLER_NAME`, `POLYTOKEN_PROJECT_DIR`, `POLYTOKEN_FACET_NAME`, and `POLYTOKEN_MODEL_NAME`.

## What a handler returns

Blocking events accept outcome-specific JSON:

| Event | Outcomes | Fields |
|---|---|---|
| `pre_tool_use` | `allow`, `deny` | `deny`: `reason` |
| `pre_user_prompt` | `accept`, `reject` | `accept`: `additional_context`; `reject`: `reason` |
| `pre_model_turn` | `proceed`, `retry` | `proceed`: `additional_context`; `retry`: `reason` |
| `stop` | `stop`, `continue` | `continue`: `reason` |
| `pre_compaction` | `allow`, `cancel`, `suppress` | `allow`: `prepend_to_prompt`; `cancel`/`suppress`: `reason` |

Fire-and-forget events return `{"outcome": "acknowledged"}` or `{"outcome": "error", "message": "..."}`.

### Exit-code shorthand

- `0` with no output = proceed outcome.
- `2` = stop outcome (with captured stdout as reason).
- Any other non-zero = error.

## Example: block edits to a generated file

```json
[
  {
    "name": "protect-generated-reference",
    "event": "pre_tool_use",
    "matcher": "file_edit_search_replace",
    "handler": {
      "bash": "test \"$(jq -r '.input.path // empty')\" = docs/reference/generated.md && { echo 'docs/reference/generated.md is generated; do not edit it by hand.'; exit 2; }; exit 0"
    }
  }
]
```

## Negation

A project file can disable a global hook by name:

```json
["!log-edits"]
```

## Security notes

- Handlers have a short deadline; a hung handler becomes an error and may block the action.
- On blocking events, an error from the handler stops the action unless the event is `pre_user_prompt`, `notification`, or `post_compaction`.
- Validate the matcher subject before acting on it.
