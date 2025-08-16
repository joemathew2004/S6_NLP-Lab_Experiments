import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np

stopwords_set = set(stopwords.words('english'))         # Define a list of English stopwords

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)         # Tokenize the text using NLTK
    tokens = [word.strip(string.punctuation) for word in tokens if word.strip(string.punctuation) not in stopwords_set and word.strip(string.punctuation) != '']
    return tokens                     # Remove punctuation and stopwords, and avoid empty strings

def create_vocabulary(corpus):
    vocabulary = set()                             # Using a set to store unique words
    for doc in corpus:
        tokens = preprocess_text(doc)
        vocabulary.update(tokens)                 # Add unique tokens to the vocabulary
    return sorted(vocabulary)                     # Return sorted vocabulary for consistent indexing

def get_bag_of_words(corpus, vocabulary):
    bow_matrix = []
    for doc in corpus:
        tokens = preprocess_text(doc)
        doc_vector = [0] * len(vocabulary)         # Create a vector (same length as the vocabulary)
        for word in tokens:
            if word in vocabulary:                 # Update the vector with the count of each word
                index = vocabulary.index(word)     # Find the index of the word in the vocabulary
                doc_vector[index] += 1
        bow_matrix.append(doc_vector)
    return np.array(bow_matrix)                 # Return as a NumPy array for compatibility

def main():
    corpus = [
        "This is the first document.",
        "This document is the second document.",
        "And this is the third one.",
        "Is this the first document?"
    ]

    vocabulary = create_vocabulary(corpus)           # Create vocabulary

    bow_matrix = get_bag_of_words(corpus, vocabulary) # Get the Bag of Words model

    print("\nVocabulary (Unique words):")
    print(vocabulary)

    print("\nBag of Words Model Representation:")
    for i, vector in enumerate(bow_matrix):
        print(f"\nDocument {i+1}: {corpus[i]}")
        print("Vector:", vector)

if __name__ == "__main__":
    main()