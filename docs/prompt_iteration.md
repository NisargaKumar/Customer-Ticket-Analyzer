# Prompt Iterations

## Iteration 1 – Basic Sentiment Heuristic
Initial logic was based only on keywords in the message.
Resulted in neutral ratings for very negative feedback.

## Iteration 2 – Added Exclamation Emphasis
Weighted message tone higher if exclamation/anger words present.
Improved urgency tagging in SentimentAgent.

## Iteration 3 – Priority Agent Edge Case Fixes
Initially assigned high priority only on revenue.  
Now considers customer tier + previous tickets for better accuracy.
