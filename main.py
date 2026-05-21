import joblib

from src.data_processing.text_cleaner import clean_text
from src.data_processing.skill_extractor import extract_skills
from src.resume_parser.parser import extract_resume_text

from src.recommendation.recommender import (
    hybrid_recommend_jobs
)


# Load trained artifacts
vectorizer = joblib.load(
    "models/vectorizer/tfidf_vectorizer.pkl"
)

job_vectors = joblib.load(
    "models/vectorizer/job_vectors.pkl"
)

tech_jobs = joblib.load(
    "models/vectorizer/tech_jobs.pkl"
)


# Resume path
resume_path = "data/resumes/sample_resume.pdf"


# Extract resume text
resume_text = extract_resume_text(
    resume_path
)


# Generate recommendations
recommendations = hybrid_recommend_jobs(
    resume_text=resume_text,
    tech_jobs=tech_jobs,
    vectorizer=vectorizer,
    job_vectors=job_vectors,
    clean_text=clean_text,
    extract_skills=extract_skills,
    top_n=5
)


# Display results
print("\nTOP JOB RECOMMENDATIONS:\n")

print(recommendations)