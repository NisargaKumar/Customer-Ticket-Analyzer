import json
from agents.sentiment_agent import SentimentAgent, SentimentInput
from agents.tier_priority_agent import TierPriorityAgent, PriorityInput
from agents.router_agent import RoutingAgent, RoutingInput
from evaluation.test_cases import TEST_TICKETS
from evaluation.metrics import calculate_metrics

try:
    from termcolor import cprint
except ImportError:
    def cprint(text, color=None, attrs=None):
        print(text)

def process_ticket(ticket):
    sentiment_agent = SentimentAgent()
    sentiment_result = sentiment_agent.run(SentimentInput(
        subject=ticket["subject"],
        message=ticket["message"]
    ))

    tier_agent = TierPriorityAgent()
    priority_result = tier_agent.run(PriorityInput(
        customer_tier=ticket["customer_tier"],
        previous_tickets=ticket["previous_tickets"],
        monthly_revenue=ticket["monthly_revenue"],
        account_age_days=ticket["account_age_days"]
    ))

    router_agent = RoutingAgent()
    routing_result = router_agent.run(RoutingInput(
        urgency_level=sentiment_result.urgency_level,
        sentiment_score=sentiment_result.sentiment_score,
        priority_score=priority_result.priority_score,
        sla_target_time=priority_result.sla_target_time
    ))

    return {
        "ticket_id": ticket["ticket_id"],
        "sentiment": sentiment_result.model_dump(),
        "priority": priority_result.model_dump(),
        "routing": routing_result.model_dump(),
    }

if __name__ == "__main__":
    results = []
    for i, ticket in enumerate(TEST_TICKETS):
        result = process_ticket(ticket)
        results.append(result)
        cprint(f"\n=== Ticket {i+1}: {result['ticket_id']} ===", "cyan", attrs=["bold"])
        print(json.dumps(result, indent=2))

    # Save to JSON file
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    # Print metrics summary
    cprint("\n=== Evaluation Metrics ===", "green", attrs=["bold"])
    metrics = calculate_metrics(results)
    print(json.dumps(metrics, indent=2))
