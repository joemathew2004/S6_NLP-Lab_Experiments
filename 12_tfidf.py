from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_tfidf_sklearn(documents):
    vectorizer = TfidfVectorizer()			            # Initialize the TF-IDF vectorizer
    tfidf_matrix = vectorizer.fit_transform(documents)  # Convert the document-term matrix (TF-IDF scores)
    feature_names = vectorizer.get_feature_names_out()  # Get the list of unique words 

    tfidf_scores = []

    for i in range(tfidf_matrix.shape[0]):              # tfidf_matrix.shape[0]: returns the number of rows in the TF-IDF matrix
        row = tfidf_matrix.getrow(i)  			                                # Get the TF-IDF values for the current doc
        scores = {feature_names[col]: row[0, col] for col in row.indices}       # Extract nonzero values
        tfidf_scores.append(scores)			                    # Store scores for this document

    return tfidf_scores, feature_names  

documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
]

tfidf_scores, feature_names = calculate_tfidf_sklearn(documents)

for i, doc_scores in enumerate(tfidf_scores):
    print(f"TF-IDF scores for document {i + 1}:")
    for word, score in doc_scores.items():
        print(f"{word}: {score:.4f}")  
    print(" ")  