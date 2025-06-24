from pydantic import BaseModel
from pydantic_ai import AIModel

class SentimentInput(BaseModel):
    subject: str
    message: str

class SentimentOutput(BaseModel):
    sentiment_score: float
    urgency_level: str

class SentimentAgent(AIModel):
    prompt_template = """
You are a customer sentiment analyzer.
Based on the subject and message, return:
1. sentiment_score (between -1 and 1)
2. urgency_level (Low, Medium, or High)
Respond in JSON format.
"""
    input_model = SentimentInput
    output_model = SentimentOutput
