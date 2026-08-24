# 🛡️ AI Action Firewall

> **Security middleware for AI agents — evaluate, control, and audit agent actions before they reach business systems.**

AI Action Firewall is a production-oriented AI security platform that sits between an AI agent and the tools/APIs it wants to use. It evaluates an action against identity, permissions, security policies, and risk signals before deciding whether the action should be **allowed, monitored, approved, or blocked**.

## 🎯 The Problem

AI agents are becoming capable of calling APIs, reading data, sending messages, and executing business workflows. Traditional application permissions and logs do not always provide a single control point for evaluating agent actions before execution.

## 💡 The Solution

```text
AI Agent
   │
   │  requested action
   ▼
┌──────────────────────┐
│  AI Action Firewall  │
│                      │
│ Identity & Access    │
│ Policy Evaluation    │
│ Risk Analysis        │
│ Audit Logging        │
└──────────┬───────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
   ALLOW       BLOCK
     │
     ▼
Business System / Tool
```

## ✨ Core Capabilities

- 🔐 AI-agent action authorization
- 🧩 Policy-based enforcement
- 🧠 ML-assisted risk scoring
- 🚦 Allow / monitor / approval / block decisions
- 📝 Security event and audit logging
- 📊 Web dashboard for security visibility
- 🔌 API-first architecture
- 🧪 Automated testing
- ⚙️ Environment-based configuration
- 🚀 Production deployment roadmap

## 🏗️ Technology Direction

| Layer | Technology |
|---|---|
| Backend | Python + FastAPI |
| ML | Python ML stack / risk models |
| Frontend | Web application |
| Database | PostgreSQL (production target) |
| Cache / queues | Redis (planned) |
| Packaging | uv / pyproject.toml |
| Containers | Docker (deployment target) |
| CI/CD | GitHub Actions (target) |
| API documentation | OpenAPI / FastAPI |

## 📁 Repository Structure

```text
ai-action-firewall/
├── backend/             # FastAPI application and business logic
├── frontend/            # Web dashboard
├── ml/                  # Risk-scoring and ML components
├── tests/               # Automated tests
├── docs/                # Architecture, product and case-study documentation
├── scripts/             # Developer/operations scripts
├── .env.example         # Environment variable template
├── pyproject.toml       # Python project configuration
├── PRODUCT_DEFINITION.md
├── README.md
└── uv.lock
```

## 🚀 Project Status

**Current stage: Early development / MVP build.**

The repository is being developed incrementally from a working FastAPI foundation toward a production-ready AI security SaaS. Features and deployment claims will only be marked complete when implemented and tested.

## 🧪 Development

Clone the repository:

```bash
git clone https://github.com/aizaz512/ai-action-firewall.git
cd ai-action-firewall
```

Create/sync the environment with uv:

```bash
uv sync
```

Run the FastAPI application:

```bash
uv run uvicorn backend.app.main:app --reload
```

Run tests:

```bash
uv run pytest
```

Run linting:

```bash
uv run ruff check backend tests
```

## 📚 Documentation

- [Product Definition](PRODUCT_DEFINITION.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Case Study](docs/CASE_STUDY.md)
- [Demo Script](docs/DEMO_SCRIPT.md)

## 🔭 Roadmap

- [x] FastAPI backend foundation
- [x] Application configuration foundation
- [ ] Authentication and authorization
- [ ] Agent/action request schema
- [ ] Policy engine
- [ ] Allow/block decision workflow
- [ ] Audit event storage
- [ ] ML risk scoring
- [ ] Dashboard
- [ ] PostgreSQL integration
- [ ] Docker deployment
- [ ] CI/CD pipeline
- [ ] Cloud deployment
- [ ] Usage metering and billing
- [ ] Public SaaS launch

## 🤝 Product Direction

The long-term goal is to provide a practical security control layer for teams adopting AI agents, starting with a focused MVP and expanding toward integrations, enterprise deployment, and SaaS capabilities.

## 📌 Portfolio

This repository is also a public engineering case study showing the progression from product definition → backend architecture → AI/ML risk analysis → testing → deployment → SaaS readiness.
