import spacy
nlp = spacy.load("en_core_web_sm")

def parse_resume(text):
    doc = nlp(text)
    return {
        "skills": [token.text for token in doc if token.pos_ == "NOUN"],
        "education": [ent.text for ent in doc.ents if ent.label_ in ["ORG", "EDUCATION"]],
        "experience": [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    }