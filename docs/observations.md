# Observations

- Some tickets with angry tone but from free-tier users were routed to Tier 2 due to combined score logic.
- SentimentAgent treats all tickets equally; future enhancement: weigh enterprise users higher.
- Ticket SUP-005 (security issue) got medium urgency — may need security keyword overrides.
- RoutingAgent consistently escalated any ticket with score > 0.8 — could make this more dynamic.
