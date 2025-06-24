# 💡 Multi-Agent Ticket Routing System (Case Study)

This project is a **multi-agent AI system** designed to analyze customer support tickets and intelligently route them based on ticket sentiment, customer profile, and urgency. The solution follows the **Pydantic AI** pattern and simulates a production-ready coordination between modular agents.

---

## 🚀 Project Overview

- **Architecture**: Modular multi-agent setup using Python + Pydantic
- **Agents**:
  - `SentimentAgent`: Estimates sentiment score and urgency level
  - `TierPriorityAgent`: Evaluates customer priority and SLA expectations
  - `RoutingAgent`: Determines the best route based on outputs from other agents
- **Evaluation**: Runs on 5 test tickets and outputs metrics like escalation rate, route distribution, and average SLA time

---

## 🔩 Folder Structure

```
customer-ticket-analyzer/
├── main.py
├── agents/
│   ├── sentiment_agent.py
│   ├── tier_priority_agent.py
│   └── router_agent.py
├── evaluation/
│   ├── test_cases.py
│   └── metrics.py
├── docs/
│   ├── system_architecture.md
│   ├── prompt_iterations.md
│   └── observations.md
├── ai_chat_history.txt
├── results.json
└── requirements.txt #here termcolor is for color-coded, readable formatting for the outputs 
```

---

## 💠 How It Works

### 1. `SentimentAgent`
- Takes ticket subject + message
- Outputs:
  - `sentiment_score` (e.g., 0.8)
  - `urgency_level` (e.g., High, Medium)

### 2. `TierPriorityAgent`
- Uses customer metadata (tier, revenue, etc.)
- Outputs:
  - `priority_score` (e.g., 0.9)
  - `sla_target_time` (e.g., "4 hours")

### 3. `RoutingAgent`
- Combines sentiment + priority to decide:
  - `route_to` (e.g., "Tier 2 Support")
  - `escalate` (bool)

All agents use **Pydantic models** for clean validation and structure.

---

## 📊 Evaluation Metrics

After processing all 5 test tickets, the system outputs:

- `Escalation Rate`: % of tickets escalated
- `Route Distribution`: How many tickets go to each queue
- `Average SLA (hrs)`: Average time expectations

Example:
```json
{
  "escalation_rate": 1.0,
  "route_distribution": {
    "Tier 2 Support": 5
  },
  "average_sla_hours": 4.0
}
```

---

## 🧪 Running the Project

### ✅ Requirements
```bash
pip install -r requirements.txt
```

### ▶ Run Main Script
```bash
python main.py
```

- Outputs will be printed to terminal with colored headers
- Final metrics summary will appear at the bottom
- Results also saved to `results.json`

---

## 🤖 Mock Logic & Design

- All agents currently use **mock logic** for scoring and decisions.
- The architecture is **LLM-ready**: drop in OpenAI, Claude, Hugging Face, or Groq APIs later.
- Modular agents are independently testable and replaceable.

---

## 🎯 Key Insight

> Rather than one monolithic prompt, this solution **uses three distinct AI perspectives** — sentiment, customer importance, and routing — to produce a cooperative, explainable decision system.

---

## 📬 Contact

Built by **Nisarga K**  
For any questions, reach out at: `nisarganishu3112@gmail.com`
