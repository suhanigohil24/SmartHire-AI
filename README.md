# SmartHire-AI

AI-powered candidate ranking system for recruiter search.

## Objective

Rank candidates based on their relevance to an AI/ML Search & Ranking Engineer job description.

## Project Structure

data/
- candidates.jsonl
- candidate_schema.json

docs/
- job_description.docx
- submission_spec.docx

src/
- load_data.py
- scorer.py
- rank_candidates.py
- save_results.py
- generate_submission.py

output/
- results.json
- submission.csv

## Scoring Logic

Candidates are scored using:

- AI/ML skills
- Search & ranking experience
- Retrieval systems experience
- Vector database experience
- NLP experience
- Recommendation systems experience
- Years of experience
- Recruiter engagement signals
- Open-to-work status
- Activity signals

## Running

Generate rankings:

```bash
python src/rank_candidates.py