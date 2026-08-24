# AI Action Firewall — Architecture

## 1. High-level architecture

```text
                    ┌─────────────────┐
                    │    AI Agent     │
                    └────────┬────────┘
                             │ action request
                             ▼
                    ┌─────────────────┐
                    │   FastAPI API   │
                    └────────┬────────┘
                             ▼
              ┌────────────────────────────┐
              │   AI Action Firewall       │
              │                            │
              │  1. Identity / Auth        │
              │  2. Permission checks      │
              │  3. Policy evaluation      │
              │  4. Risk analysis          │
              │  5. Decision engine        │
              └─────────────┬──────────────┘
                            │
                 ┌──────────┼──────────┐
                 ▼          ▼          ▼
              ALLOW      APPROVAL    BLOCK
                 │          │          │
                 └──────────┼──────────┘
                            ▼
                    ┌───────────────┐
                    │ Audit Events  │
                    └───────┬───────┘
                            ▼
                    Database / Logs
```

## 2. Request lifecycle

1. An AI agent submits an intended action.
2. The API validates the request structure.
3. The system identifies the requesting agent/user.
4. Permissions and security policies are evaluated.
5. Risk signals are calculated.
6. The decision engine produces an action decision.
7. The event is recorded for auditability.
8. Only an allowed action is forwarded to the target business tool.

## 3. Security principle

The firewall follows a **default-control-point** design: an AI agent should not receive unrestricted access to sensitive business tools. Actions should pass through a policy and risk decision point before execution.

## 4. Production evolution

The MVP is intentionally focused. Production hardening will add authentication, persistent audit storage, rate limiting, secrets management, observability, CI/CD, Docker deployment, and controlled integrations.
