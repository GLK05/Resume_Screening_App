import streamlit as st
from ranking_engine import rank_resumes
from utils import extract_text_from_pdf
import pandas as pd

st.title("📄 AI Resume Screening Tool")

uploaded_files = st.file_uploader(
    "Upload PDF Resumes", type="pdf", accept_multiple_files=True
)
job_description = st.text_area("Paste Job Description Here")

if uploaded_files and job_description and st.button("Rank Resumes"):
    resume_texts = [extract_text_from_pdf(file) for file in uploaded_files]

    # Check if ranking works
    scores = rank_resumes(resume_texts, job_description)

    # Defensive check: scores must match number of resumes
    if len(scores) != len(uploaded_files):
        st.error("Error: Number of scores does not match number of resumes.")
    else:
        results = sorted(
            zip([file.name for file in uploaded_files], scores),
            key=lambda x: x[1], reverse=True
        )

        st.write("### 🏆 Ranked Candidates")
        for i, (name, score) in enumerate(results, 1):
            st.write(f"{i}. {name} — Match Score: {score:.2f}")

        df = pd.DataFrame(
            [(name, score) for name, score in results],
            columns=["Candidate", "Match Score"]
        )
        st.download_button(
            "📥 Export to CSV",
            data=df.to_csv(index=False),
            file_name="ranked_candidates.csv",
            mime="text/csv"
        )
