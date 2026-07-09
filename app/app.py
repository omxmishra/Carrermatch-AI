import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import tempfile, joblib, pandas as pd

from src.data_processing.text_cleaner import clean_text
from src.data_processing.skill_extractor import extract_skills
from src.resume_parser.parser import extract_resume_text
from src.recommendation.recommender import hybrid_recommend_jobs

st.set_page_config(
    page_title="CareerMatch AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Lora:wght@500;600&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: #141924 !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #eef0f6;
}
[data-testid="stAppViewContainer"] > .main { background: #141924 !important; }
[data-testid="stHeader"], [data-testid="stToolbar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
#MainMenu, footer { visibility: hidden; }

.block-container {
    padding: 0 60px 80px !important;
    max-width: 900px !important;
    margin: 0 auto;
}

.hero {
    text-align: center;
    padding: 64px 0 48px;
    border-bottom: 1px solid #2c3649;
    margin-bottom: 40px;
}
.hero-eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #e8a838;
    margin-bottom: 16px;
}
.hero-title {
    font-family: 'Lora', serif;
    font-size: 48px;
    font-weight: 600;
    color: #eef0f6;
    letter-spacing: -0.02em;
    margin: 0 0 16px;
    line-height: 1.1;
}
.hero-sub {
    font-size: 16px;
    color: #8b93a7;
    font-weight: 300;
    margin: 0;
}

[data-testid="stFileUploader"] {
    background: #1c2333 !important;
    border: 1.5px dashed #2c3649 !important;
    border-radius: 12px !important;
    padding: 28px 24px !important;
    transition: border-color 0.2s;
}
[data-testid="stFileUploader"]:hover { border-color: #e8a838 !important; }
[data-testid="stFileUploader"] label { color: #8b93a7 !important; font-size: 14px !important; }
[data-testid="stFileUploadDropzone"] p { color: #8b93a7 !important; }
[data-testid="stFileUploader"] button {
    background: #212a3e !important;
    color: #eef0f6 !important;
    border: 1px solid #2c3649 !important;
    border-radius: 8px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
[data-testid="stFileUploader"] button:hover { border-color: #e8a838 !important; color: #e8a838 !important; }

.stButton > button {
    background: #e8a838 !important;
    color: #141924 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px 28px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    letter-spacing: 0.02em !important;
    transition: all 0.2s !important;
    box-shadow: 0 2px 12px rgba(232,168,56,0.25) !important;
}
.stButton > button:hover {
    background: #f0b84a !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 20px rgba(232,168,56,0.4) !important;
}

[data-testid="stAlert"] {
    background: rgba(62,207,142,0.08) !important;
    border: 1px solid rgba(62,207,142,0.25) !important;
    border-radius: 10px !important;
    color: #3ecf8e !important;
}
[data-testid="stInfo"] {
    background: #1c2333 !important;
    border: 1px solid #2c3649 !important;
    border-radius: 10px !important;
    color: #8b93a7 !important;
}

[data-testid="stMetric"] {
    background: #1c2333;
    border: 1px solid #2c3649;
    border-radius: 10px;
    padding: 16px 18px;
}
[data-testid="stMetricLabel"] {
    font-size: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: #4f5669 !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Lora', serif !important;
    font-size: 24px !important;
    font-weight: 600 !important;
    color: #eef0f6 !important;
}

[data-testid="stExpander"] {
    background: #1c2333 !important;
    border: 1px solid #2c3649 !important;
    border-radius: 14px !important;
    margin-bottom: 12px !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
    overflow: hidden;
}
[data-testid="stExpander"]:hover {
    border-color: #e8a838 !important;
    box-shadow: 0 0 0 3px rgba(232,168,56,0.08) !important;
}
[data-testid="stExpander"] summary {
    padding: 18px 22px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    color: #eef0f6 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
[data-testid="stExpander"] summary:hover { color: #e8a838 !important; }
details[data-testid="stExpander"] > div { padding: 4px 22px 20px !important; }

.stProgress > div > div {
    background: linear-gradient(90deg, #e8a838, #f0b84a) !important;
    border-radius: 99px !important;
}
.stProgress { margin: 2px 0 16px !important; }
[data-testid="stProgressBar"] {
    background: #212a3e !important;
    border-radius: 99px !important;
    height: 6px !important;
}

[data-testid="stSpinner"] p { color: #e8a838 !important; }
.stCaption { color: #4f5669 !important; font-size: 12px !important; letter-spacing: 0.04em; }
hr { border: none !important; border-top: 1px solid #2c3649 !important; margin: 28px 0 !important; }

code {
    background: #212a3e !important;
    color: #8b93a7 !important;
    border: 1px solid #2c3649 !important;
    border-radius: 6px !important;
    padding: 2px 8px !important;
    font-size: 12px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 500 !important;
}

[data-testid="stHorizontalBlock"] { gap: 10px !important; }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_artifacts():
    vectorizer  = joblib.load("models/vectorizer/tfidf_vectorizer.pkl")
    job_vectors = joblib.load("models/vectorizer/job_vectors.pkl")
    tech_jobs   = joblib.load("models/vectorizer/tech_jobs.pkl")
    return vectorizer, job_vectors, tech_jobs

vectorizer, job_vectors, tech_jobs = load_artifacts()


st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">AI Career Tool</div>
    <div class="hero-title">CareerMatch AI 🚀</div>
    <p class="hero-sub">Upload your resume. Get the roles that actually fit your skills.</p>
</div>
""", unsafe_allow_html=True)


st.markdown(
    '<p style="font-size:11px;font-weight:700;letter-spacing:0.12em;'
    'text-transform:uppercase;color:#4f5669;margin-bottom:14px;">Your Resume</p>',
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    label="Upload PDF",
    type=["pdf"],
    label_visibility="collapsed",
)

if uploaded_file:
    col_btn, col_info = st.columns([2, 5])
    with col_btn:
        run = st.button("Find My Matches →")
    with col_info:
        st.caption(f"📄  {uploaded_file.name}  ·  {uploaded_file.size // 1024} KB")

    if run:
        with st.spinner("Scanning resume and matching roles…"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                temp_path = tmp.name
            resume_text = extract_resume_text(temp_path)
            recs = hybrid_recommend_jobs(
                resume_text=resume_text,
                tech_jobs=tech_jobs,
                vectorizer=vectorizer,
                job_vectors=job_vectors,
                clean_text=clean_text,
                extract_skills=extract_skills,
                top_n=5,
            )
            st.session_state["recs"] = recs
        st.success("✓  Recommendations ready — scroll down to review your matches.")


MEDAL = {1: "🥇", 2: "🥈", 3: "🥉", 4: "#4", 5: "#5"}

if "recs" in st.session_state:
    df: pd.DataFrame = st.session_state["recs"]

    st.divider()
    left, right = st.columns([5, 2])
    with left:
        st.markdown(
            '<h2 style="font-family:\'Lora\',serif;font-size:24px;font-weight:600;'
            'color:#eef0f6;margin:0;">Top Matches</h2>',
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            f'<p style="font-size:12px;color:#4f5669;text-align:right;margin-top:6px;">'
            f'{len(df)} roles found</p>',
            unsafe_allow_html=True,
        )

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    for rank, (_, row) in enumerate(df.iterrows(), start=1):
        title    = str(row.get("title", "Role")).title()
        company  = str(row.get("company_name", "—"))
        location = str(row.get("location", "—"))
        sim      = float(row.get("similarity_score", 0))
        overlap  = int(row.get("skill_overlap", 0))
        final    = float(row.get("final_score", 0))

        matched_list = [
            s.strip() for s in
            str(row.get("matched_skills", "")).replace(",", " ").split()
            if s.strip() and s != "nan"
        ][:8]

        extracted_list = [
            s.strip() for s in
            str(row.get("extracted_skills", "")).replace(",", " ").split()
            if s.strip() and s != "nan"
        ][:6]

        medal = MEDAL.get(rank, f"#{rank}")
        header_label = f"{medal}  {title}  ·  {company}  ·  📍 {location}"

        with st.expander(header_label, expanded=(rank == 1)):
            c1, c2, c3 = st.columns(3)
            c1.metric("Similarity", f"{sim:.1f}")
            c2.metric("Skill Overlap", f"{overlap} skills")
            c3.metric("Final Score", f"{final:.1f}")

            bar_pct = min(1.0, final / 100)
            st.caption(f"Match strength  {final:.1f} / 100")
            st.progress(bar_pct)

            if matched_list:
                st.markdown(
                    '<p style="font-size:11px;font-weight:700;letter-spacing:0.1em;'
                    'text-transform:uppercase;color:#4f5669;margin:12px 0 6px;">Matched from resume</p>',
                    unsafe_allow_html=True,
                )
                st.markdown("  ".join(f"`{s}`" for s in matched_list))

            if extracted_list:
                st.markdown(
                    '<p style="font-size:11px;font-weight:700;letter-spacing:0.1em;'
                    'text-transform:uppercase;color:#4f5669;margin:12px 0 6px;">Role requires</p>',
                    unsafe_allow_html=True,
                )
                st.markdown("  ".join(f"`{s}`" for s in extracted_list))

else:
    st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)
    st.info("📂  Upload your resume and click **Find My Matches** to see your top job recommendations.")