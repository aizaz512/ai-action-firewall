# AI Action Firewall — Product Definition

## 1. What does our product do?
Our product protects AI agents from performing dangerous or unauthorized actions.
It checks what an AI agent wants to do and decides whether to allow or block the action.

## 2. Who is our first customer?
Our first customers are small companies that use AI agents to perform business tasks.

## 3. What painful problem are we solving?
Companies may give AI agents access to important business data and tools,
but they may not have a good way to control or monitor what those agents do.

## 4. What happens today without our product?
The company may have separate permissions and logs, but no single system
that evaluates AI-agent actions before they happen.

## 5. What does our product do differently?
Our product sits between the AI agent and the tools it wants to use.
It checks the action before allowing it to reach the real system.

## 6. What is the single most important workflow in our MVP?
An AI agent requests an action → our system checks it → the system allows,
monitors, asks for approval, or blocks the action.

## 7. What actions can our product ALLOW?
Reading an allowed customer record
Creating a support ticket
Sending an approved email
Reading an approved document

## 8. What actions can our product BLOCK?
Unauthorized customer-data export
Accessing restricted information
Sending sensitive information to an unknown destination
Performing an action that violates a security policy

## 9. What is NOT included in our MVP?
We will not initially build:
- mobile application
- large enterprise compliance platform
- dozens of integrations
- Kubernetes infrastructure
- custom large language model

## 10. Why would a small company pay for this?
A company may pay because it wants to safely use AI agents
without giving those agents unlimited control over company data and systems.