import re
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    text = text.lower()  			        # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  	# Remove punctuation
    return text

def create_bow_matrix(sentences):
    all_words = set(" ".join(sentences).split())     # Create a list of all unique words in the corpus
    
    word_to_index = {word: index for index, word in enumerate(all_words)}	# Create a word-to-index mapping
    
    bow_matrix = []				     # Create the Bag of Words matrix
    for sentence in sentences:
        vector = [0] * len(word_to_index)
        for word in sentence.split():
            if word in word_to_index:
                vector[word_to_index[word]] += 1
        bow_matrix.append(vector)
    
    return bow_matrix, word_to_index

def find_most_similar_sentence(input_sentence, file_path):
    with open(file_path, 'r') as file:
        sentences = file.readlines()  		    # Read all sentences
    
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]  # Remove empty lines
    sentences = [preprocess_text(sentence) for sentence in sentences]  		      # Preprocess sentences
    
    input_sentence = preprocess_text(input_sentence)		    # Preprocess input sentence
    sentences.append(input_sentence)				            # Append input sentence for comparison
    bow_matrix, word_to_index = create_bow_matrix(sentences)	# Create Bag of Words matrix
    
    similarity_scores = cosine_similarity([bow_matrix[-1]], bow_matrix[:-1])[0]	  # Compute cosine similarity
    
    most_similar_index = similarity_scores.argmax()		# Find the most similar sentence
    most_similar_sentence = sentences[most_similar_index]
    highest_similarity = similarity_scores[most_similar_index]
    
    return most_similar_sentence, highest_similarity

file_path = "file6.txt"
input_sentence = input("Enter a sentence: ")

most_similar, similarity_score = find_most_similar_sentence(input_sentence, file_path)

print("\nMost similar sentence:", most_similar)
print(f"Cosine Similarity Score: {similarity_score:.4f}")