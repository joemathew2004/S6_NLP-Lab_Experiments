'''
import nltk

def sentence_tokenize(text):
  sentences = nltk.sent_tokenize(text)
  return sentences

# Example usage:
text = "This is the first sentence. This is the second sentence! And this is the third one? Hello."
sentences = sentence_tokenize(text)
print(sentences)
'''

import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def tokenize_and_filter(text):
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    filtered_tokens = [
        token for token in tokens
        if token.isalnum() and token not in stop_words
    ]
    return filtered_tokens

def is_script_valid(text):
    pattern = r'^[\w\s.,!?;\'"-]*$'
    return bool(re.match(pattern, text))

def perform_stemming(tokens):
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

# Example Usage
text1 = "This is a sample text with some stop words like is and a. It also has punctuation! and numbers 123."
text2 = "This text contains some non-English characters: こんにちは"

# Script Validation
print(f"Is text1 script valid? {is_script_valid(text1)}")
print(f"Is text2 script valid? {is_script_valid(text2)}")

# Tokenization and Filtration
filtered_tokens1 = tokenize_and_filter(text1)
print(f"\nFiltered tokens for text1: {filtered_tokens1}")

filtered_tokens2 = tokenize_and_filter(text2)
print(f"Filtered tokens for text2: {filtered_tokens2}")

# Stemming
stemmed_tokens1 = perform_stemming(filtered_tokens1)
print(f"\nStemmed tokens for text1: {stemmed_tokens1}")

stemmed_tokens2 = perform_stemming(filtered_tokens2)
print(f"Stemmed tokens for text2: {stemmed_tokens2}")