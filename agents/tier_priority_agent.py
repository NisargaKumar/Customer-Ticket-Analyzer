from pydantic import BaseModel
from pydantic_ai import AIModel

class PriorityInput(BaseModel):
    customer_tier: str
    previous_tickets: int
    monthly_revenue: float
    account_age_days: int

class PriorityOutput(BaseModel):
    priority_score: float
    sla_target_time: str

class TierPriorityAgent(AIModel):
    prompt_template = """
You are a customer priority evaluator.
Based on customer tier, revenue, history, and account age:
1. Output a priority_score (0.0 to 1.0)
2. Suggest SLA response time (e.g. '2 hours', '1 day')
Respond in JSON.
"""
    input_model = PriorityInput
    output_model = PriorityOutput
