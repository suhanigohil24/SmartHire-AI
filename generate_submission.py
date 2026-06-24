import json
import csv

from scorer import calculate_score

results = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        score = calculate_score(candidate)

        text = str(candidate).lower()
        career = str(candidate.get("career_history", "")).lower()

        profile = candidate.get("profile", {})
        years = profile.get("years_of_experience", 0)

        signals = candidate.get("redrob_signals", {})

        reasons = []

        # =====================
        # Experience
        # =====================

        if years >= 5:
            reasons.append(f"{years:.1f} years experience")

        # =====================
        # Company Experience
        # =====================

        if "google" in career:
            reasons.append("Google experience")

        if "meta" in career:
            reasons.append("Meta experience")

        if "apple" in career:
            reasons.append("Apple experience")

        if "flipkart" in career:
            reasons.append("Flipkart experience")

        if "zomato" in career:
            reasons.append("Zomato experience")

        # =====================
        # Search / Ranking Skills
        # =====================

        if "retrieval" in text:
            reasons.append("retrieval systems experience")

        if "ranking" in text:
            reasons.append("ranking expertise")

        if "rag" in text:
            reasons.append("RAG experience")

        if "pinecone" in text:
            reasons.append("Pinecone experience")

        if "faiss" in text:
            reasons.append("FAISS experience")

        if "weaviate" in text:
            reasons.append("Weaviate experience")

        if "qdrant" in text:
            reasons.append("Qdrant experience")

        if "bm25" in text:
            reasons.append("BM25 expertise")

        if "learning to rank" in text:
            reasons.append("Learning-to-Rank experience")

        if "elasticsearch" in text:
            reasons.append("Elasticsearch experience")

        if "opensearch" in text:
            reasons.append("OpenSearch experience")

        if "recommendation" in text:
            reasons.append("recommendation systems experience")

        if "nlp" in text:
            reasons.append("NLP experience")

        if "python" in text:
            reasons.append("strong Python background")

        # =====================
        # Evaluation Experience
        # =====================

        if "ndcg" in text:
            reasons.append("ranking evaluation expertise")

        if "mrr" in text:
            reasons.append("retrieval evaluation expertise")

        if "a/b" in text:
            reasons.append("online experimentation experience")

        # =====================
        # Recruiter Signals
        # =====================

        if signals.get("open_to_work_flag", False):
            reasons.append("open to work")

        if signals.get("recruiter_response_rate", 0) > 0.5:
            reasons.append("good recruiter engagement")

        if signals.get("willing_to_relocate", False):
            reasons.append("willing to relocate")

        if signals.get("notice_period_days", 90) <= 30:
            reasons.append("short notice period")

        # =====================
        # Remove duplicates
        # =====================

        reasons = list(dict.fromkeys(reasons))

        # Keep concise
        reason = ", ".join(reasons[:8])

        if not reason:
            reason = "General technical fit"

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": score,
            "reasoning": reason
        })

# =====================
# Sort Results
# =====================

results.sort(
    key=lambda x: (
        -x["score"],
        x["candidate_id"]
    )
)

top100 = results[:100]

# =====================
# Save Submission
# =====================

with open("output/submission.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, candidate in enumerate(top100, start=1):

        writer.writerow([
            candidate["candidate_id"],
            rank,
            candidate["score"],
            candidate["reasoning"]
        ])

print("submission.csv created successfully!")