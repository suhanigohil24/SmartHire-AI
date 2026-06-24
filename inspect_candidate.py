import json

TARGET_ID = "CAND_0039754"

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] == TARGET_ID:

            print(candidate)

            break