import json

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    candidate = json.loads(next(f))

print(candidate.keys())