# AI Action Firewall — 60–90 Second Demo Script

## 0–5 seconds — Hook

On screen:

> **What happens when an AI agent tries to perform a dangerous action?**

Show the dashboard/product immediately.

## 5–15 seconds — Problem

Narration:

> AI agents can now call APIs, access data, and execute business workflows. Teams need a control point that can evaluate those actions before execution.

Show an agent action request.

## 15–30 seconds — Firewall

Show:

```text
AI Agent → AI Action Firewall → Policy + Risk → Decision
```

Narration:

> AI Action Firewall sits between the agent and the business tool, evaluates the request, and produces a security decision.

## 30–50 seconds — Decision

Show three example requests:

1. Allowed customer-record read → **ALLOW**
2. Unknown destination with sensitive data → **BLOCK**
3. High-risk business action → **REQUIRES APPROVAL**

## 50–65 seconds — Auditability

Show the security event/audit log.

Narration:

> Every decision should be observable and auditable so teams can understand what agents attempted and why a request was allowed or blocked.

## 65–80 seconds — Technical proof

Show the repository and architecture briefly.

On screen:

> Python • FastAPI • AI/ML • PostgreSQL • Docker

Only show technologies that are actually implemented at the time of recording.

## 80–90 seconds — CTA

On screen:

> **Building safer AI agents.**
>
> GitHub: github.com/aizaz512/ai-action-firewall
>
> Follow the build → test → deploy journey.
