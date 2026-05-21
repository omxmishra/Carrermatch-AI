from sklearn.metrics.pairwise import cosine_similarity


def calculate_skill_overlap(
    resume_skills,
    job_skills
):

    resume_set = set(resume_skills)

    job_set = set(job_skills)

    overlap = resume_set.intersection(job_set)

    return len(overlap)


def get_matched_skills(
    resume_skills,
    job_skills
):

    return list(
        set(resume_skills).intersection(
            set(job_skills)
        )
    )


def hybrid_recommend_jobs(
    resume_text,
    tech_jobs,
    vectorizer,
    job_vectors,
    clean_text,
    extract_skills,
    top_n=5
):

    # Clean resume
    cleaned_resume = clean_text(resume_text)

    # Extract resume skills
    resume_skills = extract_skills(
        cleaned_resume
    )

    # Vectorize resume
    resume_vector = vectorizer.transform(
        [cleaned_resume]
    )

    # Semantic similarity
    similarity_scores = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]

    # Copy tech jobs
    recommendations = tech_jobs.copy()

    # Add similarity score
    recommendations['similarity_score'] = (
        similarity_scores * 100
    )

    # Skill overlap score
    recommendations['skill_overlap'] = (
        recommendations['extracted_skills']
        .apply(
            lambda job_skills:
            calculate_skill_overlap(
                resume_skills,
                job_skills
            )
        )
    )

    # Matched skills
    recommendations['matched_skills'] = (
        recommendations['extracted_skills']
        .apply(
            lambda job_skills:
            get_matched_skills(
                resume_skills,
                job_skills
            )
        )
    )

    # Final hybrid score
    recommendations['final_score'] = (
        recommendations['similarity_score']
        +
        recommendations['skill_overlap'] * 5
    )

    # Sort recommendations
    recommendations = recommendations.sort_values(
        by='final_score',
        ascending=False
    )

    return recommendations[
        [
            'title',
            'company_name',
            'location',
            'extracted_skills',
            'similarity_score',
            'skill_overlap',
            'matched_skills',
            'final_score'
        ]
    ].head(top_n)