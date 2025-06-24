from pydantic import BaseModel
from pydantic_ai import AIModel

class RoutingInput(BaseModel):
    urgency_level: str
    sentiment_score: float
    priority_score: float
    sla_target_time: str

class RoutingOutput(BaseModel):
    route_to: str
    escalate: bool

class RoutingAgent(AIModel):
    prompt_template = """
You are a support routing decider.
Based on urgency, sentiment, and priority:
1. Decide who should handle the ticket ("Tier 1 Support", "Security Team", etc.)
2. Should it be escalated? (true/false)
Respond in JSON.
"""
    input_model = RoutingInput
    output_model = RoutingOutput
