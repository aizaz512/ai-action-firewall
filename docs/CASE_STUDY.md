# AI Action Firewall — Engineering Case Study

## The problem

AI agents can interact with business tools and data. As agent capabilities increase, teams need a practical control point that can inspect intended actions before those actions reach sensitive systems.

## The product idea

AI Action Firewall is designed as a security middleware layer between an AI agent and the tools it wants to call.

The core workflow is:

```text
Agent requests action
        ↓
Firewall evaluates action
        ↓
Policy + permissions + risk
        ↓
Allow / Monitor / Approval / Block
        ↓
Audit event
```

## Target customer

The initial customer profile is a small company using AI agents for business tasks and wanting more control over what those agents can do.

## Why this is an engineering problem

The project combines several production concerns rather than only model training:

- API design
- authorization and policy enforcement
- AI/ML risk analysis
- event/audit design
- frontend visibility
- testing
- configuration management
- deployment
- future SaaS billing and usage metering

## What makes the project portfolio-worthy

The project is being developed as a real product rather than a notebook. The repository tracks product definition, architecture, implementation, tests, deployment work, and a roadmap toward SaaS.

## Current implementation status

Implemented foundations include the FastAPI backend and application configuration. The remaining MVP capabilities are being added incrementally and will be marked complete only after implementation and testing.

## Success metrics for the MVP

The project should eventually report measurable results such as:

- policy decision accuracy
- risk-model evaluation metrics
- API latency
- test coverage
- blocked/allowed action counts
- error rate
- deployment health

No metric should be presented publicly until it has been measured from the implemented system.

## Business model direction

Potential commercial models include:

1. SaaS subscription
2. Usage-based API
3. Enterprise licensing
4. Self-hosted/on-premise deployment
5. Custom integration and consulting

The initial go-to-market direction is B2B SaaS with an enterprise/self-hosted path.
