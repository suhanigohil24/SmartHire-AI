import json
from scorer import calculate_score

results = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        score = calculate_score(candidate)

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": score
        })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

with open("output/results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Results saved successfully!")