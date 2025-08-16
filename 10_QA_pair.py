import random

qa_pairs = {
    "What is your name?": [
        "I am a chatbot created by a programmer.",
        "You can call me Chatbot!",
        "I don't have a specific name, but you can call me whatever you like!"
    ],
    "How are you?": [
        "I am doing well, thank you for asking!",
        "I'm great! How about you?",
        "I'm doing fine, just here to assist you!"
    ],
    "What can you do?": [
        "I can answer your questions, tell jokes, and help you with basic queries.",
        "I can provide information, chat with you, and entertain you with jokes!",
        "I am designed to assist you with any information you need, or just chat!"
    ],
    "Tell me a joke.": [
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't programmers like nature? It has too many bugs!",
        "What do you call fake spaghetti? An impasta!"
    ],
    "What is Python?": [
        "Python is a programming language that is widely used for web development, data science, and automation.",
        "Python is a versatile language used for everything from data analysis to artificial intelligence.",
        "Python is an easy-to-learn programming language known for its simplicity and readability."
    ],
    "What is your purpose?": [
        "My purpose is to assist you with information and provide fun conversations.",
        "I'm here to answer your questions and help you with anything you need.",
        "I was created to be helpful and make your experience more enjoyable!"
    ],
    "Goodbye": [
        "Goodbye! It was nice talking to you. Have a great day!",
        "Bye! It was a pleasure chatting with you.",
        "Take care! Come back anytime if you need help."
    ],
}

def get_answer(query):
    query = query.strip().lower()

    for question, answers in qa_pairs.items():    # Try to find an exact match
        if query == question.lower():
            return random.choice(answers)         # Randomly choose one of the answers

    # If no match found, return a default response
    return "Sorry, I don't understand that question. Can you ask something else?"

def chat():
    print("Hello! I'm your chatbot. Type 'exit' to exit.")
    while True:
        query = input("\nYou: ")

        if query.strip().lower() == 'exit':
            print("Chatbot:", random.choice(qa_pairs["Goodbye"]))
            break

        answer = get_answer(query)
        print("Chatbot:", answer)

if __name__ == "__main__":
    chat()