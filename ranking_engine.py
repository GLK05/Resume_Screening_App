from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy

# Load spaCy model for semantic similarity
nlp = spacy.load("en_core_web_sm")

def rank_resumes(resume_texts, job_description):
    """
    Rank resumes using both TF-IDF and semantic similarity.
    Returns scores scaled to 0-100%.
    """
    # Method 1: TF-IDF Similarity (keyword matching)
    corpus = resume_texts + [job_description]
    vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)
    vectors = vectorizer.fit_transform(corpus)
    job_vector = vectors[-1:].reshape(1, -1)
    tfidf_scores = cosine_similarity(vectors[:-1], job_vector).flatten()
    
    # Method 2: Semantic Similarity (meaning-based)
    job_doc = nlp(job_description)
    semantic_scores = []
    
    for resume_text in resume_texts:
        resume_doc = nlp(resume_text)
        # Calculate semantic similarity between resume and job description
        similarity = resume_doc.similarity(job_doc)
        semantic_scores.append(similarity)
    
    semantic_scores = np.array(semantic_scores)
    
    # Combine both methods (weighted average)
    # 60% TF-IDF (keyword relevance) + 40% Semantic (meaning relevance)
    combined_scores = (0.6 * tfidf_scores + 0.4 * semantic_scores)
    
    # Scale to percentage (0-100)
    scaled_scores = combined_scores * 100
    
    return scaled_scores