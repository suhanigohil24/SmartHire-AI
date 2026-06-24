def calculate_score(candidate):

    score = 0

    text = str(candidate).lower()

    # =====================
    # AI / ML Skills
    # =====================

    weights = {
        "python": 10,
        "machine learning": 15,
        "ml": 15,
        "nlp": 20,
        "retrieval": 25,
        "ranking": 25,
        "embeddings": 25,
        "vector": 20,
        "pinecone": 20,
        "weaviate": 20,
        "qdrant": 20,
        "faiss": 20,
        "llm": 15,
        "recommendation": 30,
        "search": 20
    }

    for keyword, weight in weights.items():
        if keyword in text:
            score += weight

    # =====================
    # Experience Score
    # =====================

    profile = candidate.get("profile", {})

    years = profile.get("years_of_experience", 0)

    if 5 <= years <= 9:
        score += 60

    elif 3 <= years < 5:
        score += 30

    elif 10 <= years <= 12:
        score += 15

    elif years > 12:
        score -= 20

    # =====================
    # Career History
    # =====================

    career = candidate.get("career_history", [])

    for job in career:

        title = str(job.get("title", "")).lower()

        if "ai" in title:
            score += 20

        if "ml" in title:
            score += 20

        if "machine learning" in title:
            score += 20

        if "data scientist" in title:
            score += 15

        if "backend" in title:
            score += 10

        if "search" in title:
            score += 15

        if "recommendation" in title:
            score += 20

        if "ranking" in title:
            score += 20

    # =====================
    # Recruiter Signals
    # =====================

    signals = candidate.get("redrob_signals", {})

    response_rate = signals.get("recruiter_response_rate", 0)

    if response_rate > 0.8:
        score += 30
    elif response_rate > 0.5:
        score += 20

    if signals.get("open_to_work_flag", False):
        score += 15

    if signals.get("applications_submitted_30d", 0) > 5:
        score += 10

    if signals.get("interview_completion_rate", 0) > 0.8:
        score += 15

    if signals.get("github_activity_score", 0) > 50:
        score += 15

    # =====================
    # Availability Signals
    # =====================

    if signals.get("willing_to_relocate", False):
        score += 10

    notice_period = signals.get("notice_period_days", 90)

    if notice_period <= 30:
        score += 15
    elif notice_period <= 60:
        score += 5

    # =====================
    # Negative Signals
    # =====================

    bad_keywords = [
        "marketing",
        "sales",
        "hr",
        "recruiter",
        "business development"
    ]

    for word in bad_keywords:
        if word in text:
            score -= 30

    return score