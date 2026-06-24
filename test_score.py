import json
from scorer import calculate_score

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    first_candidate = json.loads(next(f))

score = calculate_score(first_candidate)

print("Candidate ID:", first_candidate["candidate_id"])
print("Score:", score)