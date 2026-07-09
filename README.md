<<<<<<< HEAD
# CareerMatch AI 🚀

An AI-powered resume-to-job recommendation system built with Python and Streamlit. Upload your resume and get the top matching roles ranked by skill overlap, TF-IDF similarity, and a hybrid final score.

---

## Demo

![CareerMatch AI]<img width="1917" height="850" alt="image" src="https://github.com/user-attachments/assets/16b16697-4a59-4b83-9bab-64efccd2b7b8" /><img width="1835" height="847" alt="image" src="https://github.com/user-attachments/assets/76467f27-b05a-474c-a8d5-0d4564a73645" />



---

## How It Works

1. **Resume Parsing** — Extracts raw text from your uploaded PDF resume
2. **Skill Extraction** — Identifies technical skills from the resume text using a curated skill extractor
3. **TF-IDF Vectorization** — Converts your resume text into a vector and computes cosine similarity against a pre-vectorized job dataset
4. **Hybrid Scoring** — Combines similarity score and skill overlap count into a weighted final score
5. **Top-N Ranking** — Returns the top 5 most relevant roles with matched and required skills

---

## Project Structure

```
careermatch-ai/
├── app.py                        # Streamlit frontend
├── models/
│   └── vectorizer/
│       ├── tfidf_vectorizer.pkl  # Trained TF-IDF vectorizer
│       ├── job_vectors.pkl       # Pre-computed job vectors
│       └── tech_jobs.pkl         # Cleaned tech job dataset
├── src/
│   ├── data_processing/
│   │   ├── text_cleaner.py       # Text normalization
│   │   └── skill_extractor.py    # Skill extraction logic
│   ├── resume_parser/
│   │   └── parser.py             # PDF text extraction
│   └── recommendation/
│       └── recommender.py        # Hybrid recommendation engine
├── notebooks/                    # EDA and model training notebooks
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Frontend | Streamlit |
| NLP | TF-IDF (scikit-learn) |
| Resume Parsing | PyMuPDF / pdfplumber |
| Recommendation | Cosine Similarity + Skill Overlap |
| Model Persistence | joblib |
| Data | pandas |

---

## Setup & Installation

**1. Clone the repository**

```bash
git clone https://github.com/omxmishra/careermatch-ai.git
cd careermatch-ai
```

**2. Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the app**

```bash
streamlit run app.py
```

---

## Requirements

```
streamlit
scikit-learn
pandas
joblib
pymupdf
```

---

## Output Fields

Each recommended job includes:

| Field | Description |
|---|---|
| `title` | Job role title |
| `company_name` | Hiring company |
| `location` | Job location |
| `similarity_score` | TF-IDF cosine similarity with resume |
| `skill_overlap` | Number of skills matched between resume and job |
| `matched_skills` | Skills found in both resume and job description |
| `extracted_skills` | Skills the job requires |
| `final_score` | Weighted hybrid score used for ranking |

---

## Author

**Om Mishra**
Final-year CS student 

- GitHub: [@omxmishra](https://github.com/omxmishra)
- LinkedIn: [om--mishra](https://linkedin.com/in/om--mishra)
- X: [@BuildWithOm](https://x.com/BuildWithOm)
=======
# CareerMatch AI 🚀

An AI-powered resume-to-job recommendation system built with Python and Streamlit. Upload your resume and get the top matching roles ranked by skill overlap, TF-IDF similarity, and a hybrid final score.

---

## Demo

![CareerMatch AI](assets/demo.png)

---

## How It Works

1. **Resume Parsing** — Extracts raw text from your uploaded PDF resume
2. **Skill Extraction** — Identifies technical skills from the resume text using a curated skill extractor
3. **TF-IDF Vectorization** — Converts your resume text into a vector and computes cosine similarity against a pre-vectorized job dataset
4. **Hybrid Scoring** — Combines similarity score and skill overlap count into a weighted final score
5. **Top-N Ranking** — Returns the top 5 most relevant roles with matched and required skills

---

## Project Structure

```
careermatch-ai/
├── app.py                        # Streamlit frontend
├── models/
│   └── vectorizer/
│       ├── tfidf_vectorizer.pkl  # Trained TF-IDF vectorizer
│       ├── job_vectors.pkl       # Pre-computed job vectors
│       └── tech_jobs.pkl         # Cleaned tech job dataset
├── src/
│   ├── data_processing/
│   │   ├── text_cleaner.py       # Text normalization
│   │   └── skill_extractor.py    # Skill extraction logic
│   ├── resume_parser/
│   │   └── parser.py             # PDF text extraction
│   └── recommendation/
│       └── recommender.py        # Hybrid recommendation engine
├── notebooks/                    # EDA and model training notebooks
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Frontend | Streamlit |
| NLP | TF-IDF (scikit-learn) |
| Resume Parsing | PyMuPDF / pdfplumber |
| Recommendation | Cosine Similarity + Skill Overlap |
| Model Persistence | joblib |
| Data | pandas |

---

## Setup & Installation

**1. Clone the repository**

```bash
git clone https://github.com/omxmishra/careermatch-ai.git
cd careermatch-ai
```

**2. Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the app**

```bash
streamlit run app.py
```

---

## Requirements

```
streamlit
scikit-learn
pandas
joblib
pymupdf
```

---

## Output Fields

Each recommended job includes:

| Field | Description |
|---|---|
| `title` | Job role title |
| `company_name` | Hiring company |
| `location` | Job location |
| `similarity_score` | TF-IDF cosine similarity with resume |
| `skill_overlap` | Number of skills matched between resume and job |
| `matched_skills` | Skills found in both resume and job description |
| `extracted_skills` | Skills the job requires |
| `final_score` | Weighted hybrid score used for ranking |

---

## Author

**Om Mishra**
Final-year CS student | AI/ML Portfolio

- GitHub: [@omxmishra](https://github.com/omxmishra)
- LinkedIn: [om--mishra](https://linkedin.com/in/om--mishra)
- X: [@BuildWithOm](https://x.com/BuildWithOm)
>>>>>>> 719e190 (Update README)
