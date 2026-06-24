import json

file_path = "data/candidates.jsonl"

with open(file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        candidate = json.loads(line)

        print("\nCandidate", i + 1)
        print(candidate)

        if i == 2:
            break