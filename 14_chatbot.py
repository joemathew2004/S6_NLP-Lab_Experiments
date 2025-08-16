from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer

def chatbot():
    model_name = "facebook/blenderbot-400M-distill"

    # Load the tokenizer and model for BlenderBot
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

    print("Chatbot: Hello! Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        inputs = tokenizer(user_input, return_tensors="pt")     # Tokenize the user input and convert it into tensors
        response_ids = model.generate(**inputs)                 # Generate the chatbot's response

        response = tokenizer.decode(response_ids[0], skip_special_tokens=True)  # Decode the model's response to readable text

        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
