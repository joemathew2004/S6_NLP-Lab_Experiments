from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_corpus_from_file(filename):
    with open(filename, 'r') as file:
        corpus = file.readlines()
    corpus = [line.strip() for line in corpus]  	# Strip extra spaces/newlines
    return corpus

def get_bag_of_words(corpus):
    vectorizer = CountVectorizer(stop_words='english')  # Automatically removes English stopwords
    X = vectorizer.fit_transform(corpus)  		        # Create the document-term matrix
    return X, vectorizer.get_feature_names_out()

def calculate_all_cosine_similarities(matrix):
    cosine_sim = cosine_similarity(matrix)		# Calculate cosine similarity for all document pairs
    return cosine_sim  

def main():
    filename = input("Enter the filename of your corpus: ")
    try:
        corpus = read_corpus_from_file(filename)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return

    bow_matrix, vocabulary = get_bag_of_words(corpus)	# Get the Bag of Words model

    print("\nVocabulary (Unique words):")		
    print(vocabulary)
    
    print("\nBag of Words Model Representation:")
    for i, vector in enumerate(bow_matrix.toarray()):
        print(f"\nDocument {i+1}: {corpus[i]}")
        print("Vector:", vector)
    
    cosine_sim = calculate_all_cosine_similarities(bow_matrix)  
    print("\nCosine Similarity Between Documents:")
    for i in range(len(cosine_sim)):
        for j in range(i + 1, len(cosine_sim)):        # Only compute upper triangle (unique pairs)
            print(f"Cosine Similarity between Document {i+1} and Document {j+1}: {cosine_sim[i][j]:.4f}")
            
if __name__ == "__main__":
    main()