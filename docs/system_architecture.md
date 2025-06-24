# System Architecture

## Overview
This system is a multi-agent architecture for customer support ticket analysis using Pydantic AI design pattern.

## Agents Used

1. **SentimentAgent**  
   - Inputs: subject and message  
   - Outputs: sentiment score and urgency level  
   - Role: Determines tone and severity of the ticket.

2. **TierPriorityAgent**  
   - Inputs: customer tier, ticket count, revenue, account age  
   - Outputs: priority score, SLA time  
   - Role: Assigns ticket priority based on business value.

3. **RoutingAgent**  
   - Inputs: results from the two agents  
   - Outputs: routing decision and escalation flag  
   - Role: Combines insights to decide escalation and target team.

## Why Multiple Agents?
- Separation of concerns makes each agent testable and reusable.
- Independent logic allows for asynchronous execution or individual upgrades.
- Easier to monitor and evaluate agent-level behavior.
