# Security for Agent Hooks

## Threat model

Agent hooks are powerful because they run inside the agent loop with the user's privileges. That also makes them a security risk:

- The hook script can read, write, or delete files the user can access.
- The agent that the hook controls can often edit the hook itself.
- Hook scripts receive untrusted JSON input on stdin and may call external tools.
- A misconfigured or malicious hook can leak secrets, exfiltrate data, or silently allow destructive actions.

## Checklist

| Do | Don't |
|---|---|
| Validate and sanitize every field read from stdin. | Pass user-controlled input directly to a shell. |
| Store secrets in environment variables or a secret manager. | Store secrets in hook JSON, `.env`, or hook scripts. |
| Require manual approval for edits to `.agents/hooks/` and platform hook files. | Let the agent auto-approve edits to its own hooks. |
| Log denials and errors to a durable, append-only log. | Fail silently on a blocking hook error. |
| Keep hooks short and fast. | Perform long-running or network-heavy work in a blocking hook. |
| Pin or review npm dependencies used by OpenCode plugins. | Install unvetted npm packages in `.opencode/package.json`. |
| Use exit code `2` / `deny` / `stop` to block on error. | Allow a blocking action when the hook errors. |

## Least privilege

- Run hooks with the minimum permissions needed. Avoid `sudo` or elevated accounts.
- Restrict filesystem access using `chroot`, containers, or directory permissions where practical.
- Do not let hooks make outbound network requests unless explicitly required.

## Input validation

- Treat stdin JSON as untrusted. Validate types, ranges, and allowed values.
- Escape file paths and command arguments before using them in shell commands.
- Use `jq` or a structured parser instead of regex where possible.

## Secrets management

- Never commit secrets to hook files or configuration files.
- Use environment variables injected at runtime, or a secret manager such as 1Password, AWS Secrets Manager, or HashiCorp Vault.
- If a hook needs an API key, load it from a file that is gitignored and not accessible to the agent by default.

## Audit and logging

- Log every blocking decision with timestamp, event, tool, and reason.
- Log hook errors, including malformed stdin and unexpected exceptions.
- Store logs outside the agent's direct write path to prevent tampering.

## Related skills

- `security` — secure design principles, cryptography, threat modeling.
- `security-best-practices` — web/API security, OWASP Top 10, authentication.
- `skill-vetter` — vetting external code and plugins before installation.
