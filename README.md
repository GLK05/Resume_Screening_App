# 📄 AI Resume Screening Tool

An intelligent resume screening application built with Streamlit that uses machine learning to rank and match resumes against job descriptions.

## Features

- **PDF Resume Upload**: Upload multiple PDF resumes at once
- **Job Description Matching**: Paste job description to find best matching candidates
- **AI-Powered Ranking**: Uses spaCy NLP and scikit-learn for intelligent matching
- **CSV Export**: Download ranked results as CSV file
- **User-Friendly Interface**: Built with Streamlit for easy web-based access

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation & Setup

### 1. Clone or Navigate to the Project Directory

```bash
cd Resume_Screening_App
```

### 2. Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download spaCy Language Model

The application requires the English language model for spaCy:

```bash
python -m spacy download en_core_web_sm
```

## Running the Application

### Start the Streamlit Server

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

### How Scoring Works

The application ranks resumes using a **hybrid matching approach**:

### Scoring Components:
- **Keyword Matching (60%)**: TF-IDF algorithm identifies relevant keywords from the job description in each resume
- **Semantic Similarity (40%)**: spaCy NLP model understands the meaning and context of both resumes and job description

### Score Interpretation:
- **0-25%**: Poor match - resume has minimal relevance to the job
- **25-50%**: Fair match - some relevant skills/experience
- **50-75%**: Good match - strong alignment with job requirements
- **75-100%**: Excellent match - very strong candidate fit

### Why Scores Matter:
Higher scores indicate better alignment between a candidate's resume and the job requirements. The algorithm considers:
- Skill keywords mentioned in both documents
- Experience levels and descriptions
- Educational background
- Domain-specific terminology
- Contextual meaning (e.g., "Python developer" vs "software engineer")

## Using the Application

1. **Upload Resumes**: Click "Upload PDF Resumes" and select one or more PDF files
2. **Enter Job Description**: Paste the job description in the text area
3. **Rank Resumes**: Click the "Rank Resumes" button
4. **View Results**: See candidates ranked by match score
5. **Export Results**: Download the ranked candidates as a CSV file

## Project Structure

```
Resume_Screening_App/
├── app.py                 # Main Streamlit application
├── ranking_engine.py      # Resume ranking logic
├── resume_parser.py       # Resume parsing utilities
├── utils.py               # Helper functions (PDF extraction)
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Requirements

- `streamlit` - Web application framework
- `spacy` - Natural Language Processing
- `scikit-learn` - Machine learning algorithms
- `pandas` - Data manipulation
- `PyPDF2` - PDF file handling

## Troubleshooting

### Port Already in Use
If port 8501 is already in use, you can specify a different port:
```bash
streamlit run app.py --server.port 8502
```

### spaCy Model Not Found
Make sure to download the language model:
```bash
python -m spacy download en_core_web_sm
```

### PDF Upload Issues
Ensure your PDF files are readable and not encrypted. Some PDFs may have extraction restrictions.

## Development

To modify the ranking algorithm or add features, edit the following files:

- `ranking_engine.py` - Core ranking logic
- `resume_parser.py` - Resume parsing methods
- `app.py` - UI and user interactions

## License

This project is available for use and modification.

## Support

For issues or questions, please check the application logs in the terminal where Streamlit is running.
