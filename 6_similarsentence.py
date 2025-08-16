import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

def preprocess_text(text):
    text = text.lower()  				        # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)         # Remove punctuation
    return text

def find_most_similar_sentence(input_sentence, file_path):
    with open(file_path, 'r') as file:
        sentences = file.readlines()  			 # Read all sentences
    
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]     # Remove empty lines
    sentences = [preprocess_text(sentence) for sentence in sentences]  		         # Preprocess sentences
   
    sentences.append(preprocess_text(input_sentence))    # Append input sentence for comparison
    
    vectorizer = CountVectorizer()			 # Convert sentences to Bag of Words vectors
    bow_matrix = vectorizer.fit_transform(sentences)
    
    similarity_scores = cosine_similarity(bow_matrix[-1], bow_matrix[:-1])[0] 
    # Compute cosine similarity between input sentence and all others 
    
    most_similar_index = similarity_scores.argmax()		# Find the most similar sentence
    most_similar_sentence = sentences[most_similar_index]
    highest_similarity = similarity_scores[most_similar_index]
    
    return most_similar_sentence, highest_similarity

file_path = "file6.txt" 
input_sentence = input("Enter a sentence: ")

most_similar, similarity_score = find_most_similar_sentence(input_sentence, file_path)

print("\nMost similar sentence:", most_similar)
print(f"Cosine Similarity Score: {similarity_score:.4f}")


'''
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def find_most_similar_sentence(input_sentence, sentences):
    sentences = [preprocess_text(sentence) for sentence in sentences]
    sentences.append(preprocess_text(input_sentence))

    vectorizer = CountVectorizer()
    bow_matrix = vectorizer.fit_transform(sentences)

    similarity_scores = cosine_similarity(bow_matrix[-1], bow_matrix[:-1])[0]

    most_similar_index = similarity_scores.argmax()
    most_similar_sentence = sentences[most_similar_index]
    highest_similarity = similarity_scores[most_similar_index]

    return most_similar_sentence, highest_similarity

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A lazy dog is jumped over by a quick brown fox.",
    "This is a completely unrelated sentence.",
    "Quick brown foxes are known for jumping.",
    "Lazy dogs often sleep during the day.",
    "The fox jumped quickly.",
    "Dogs and foxes are animals.",
    "How quickly can a fox jump?",
    "That is a lazy dog.",
    "Quick brown foxes are fast."
]

input_sentence = input("Enter a sentence: ")

most_similar, similarity_score = find_most_similar_sentence(input_sentence, sentences)

print("\nMost similar sentence:", most_similar)
print(f"Cosine Similarity Score: {similarity_score:.4f}")'''
