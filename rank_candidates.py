import json

from scorer import calculate_score

results = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        score = calculate_score(candidate)

        results.append(
            (
                candidate["candidate_id"],
                score
            )
        )

results.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nTOP 10 CANDIDATES\n")

for rank, item in enumerate(results[:10], start=1):

    print(
        rank,
        item[0],
        item[1]
    )