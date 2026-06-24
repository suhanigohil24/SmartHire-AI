import json

target_id = "CAND_0002025"

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] == target_id:

            print(candidate)

            break