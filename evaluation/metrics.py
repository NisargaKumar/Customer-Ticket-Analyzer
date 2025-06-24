# evaluation/metrics.py
from collections import Counter
from typing import List

def calculate_metrics(ticket_results: List[dict]):
    metrics = {}

    # Escalation Rate
    total = len(ticket_results)
    escalated = sum(1 for t in ticket_results if t["routing"]["escalate"])
    metrics["escalation_rate"] = escalated / total

    # Route Distribution
    routes = [t["routing"]["route_to"] for t in ticket_results]
    metrics["route_distribution"] = dict(Counter(routes))

    # Average SLA Duration (in hours)
    def parse_sla(sla):
        if "hour" in sla:
            return int(sla.split()[0])
        elif "minute" in sla:
            return int(sla.split()[0]) / 60
        return 0

    slas = [parse_sla(t["priority"]["sla_target_time"]) for t in ticket_results]
    metrics["average_sla_hours"] = sum(slas) / total if slas else 0

    return metrics
