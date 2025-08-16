import re

documents = {
    "doc1": "Artificial intelligence and machine learning are important fields in computer science.",
    "doc2": "Natural language processing is a subfield of AI that helps in understanding human language.",
    "doc3": "Deep learning is a type of machine learning that works with neural networks.",
    "doc4": "Python is a programming language that is widely used for data science and machine learning.",
}

def process_text(text):
    text = text.lower()			        # Convert to lowercase
    text = re.sub(r'\W+', ' ', text)	# Remove non-alphanumeric characters
    return set(text.split())

def find_best_matching_document(query, documents):
    query_words = process_text(query)		# Process the query

    max_common_words = 0	# Initialize variables 
    best_doc = None		    # to keep track of the best match

    for doc_name, doc_text in documents.items():	# Iterate through the documents
        doc_words = process_text(doc_text)		    # Process the document
        
        common_words = query_words & doc_words  	# Intersection of query words and document words
        common_count = len(common_words)

        if common_count > max_common_words:		# If this document has more common words, 
            max_common_words = common_count		# update the best match
            best_doc = doc_name
    
    return best_doc

def chat():
    print("Welcome to the document retrieval bot!")

    while True:
        query = input("\nEnter your query (or type 'exit' to quit): ")

        if query.lower() == 'exit':		# Exit condition
            print("Goodbye!")
            break
        
        best_doc = find_best_matching_document(query, documents)  # Find the best matching document

        if best_doc:
            print(f"\nThe document most relevant to your query is: {best_doc}")
            print(f"Document Content: {documents[best_doc]}")
        else:
            print("Sorry, no document matches your query.")

if __name__ == "__main__":
    chat()

