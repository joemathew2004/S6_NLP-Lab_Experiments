import re

# Function to perform text filtering (removing unwanted characters, words, etc.)
def filter_text(text, forbidden_words=None):
    filtered_text = re.sub(r'[^a-zA-Z\s]', '', text)	#  Remove any non-alphabet characters (you can change this depending on your needs)
    if forbidden_words:					# Remove forbidden words (if any)
        for word in forbidden_words:
            filtered_text = re.sub(r'\b' + re.escape(word) + r'\b', '', filtered_text)
    
    filtered_text = ' '.join(filtered_text.split())	    # Remove extra spaces left after removal
    
    return filtered_text

# Function to validate the script (length, only alphabetic characters, etc.)
def validate_script(text, min_length=5, max_length=200):
    if not text:					# Check if the text is empty
        return False, "Text cannot be empty."
    
    # Check the length of the text
    if len(text) < min_length or len(text) > max_length:
        return False, f"Text should be between {min_length} and {max_length} characters long."
    
    # Check if the text contains only alphabetic characters and spaces (optional check)
    if not all(c.isalpha() or c.isspace() for c in text):
        return False, "Text should contain only alphabetic characters and spaces."
    
    return True, "Text is valid."

forbidden_words = ["hate", "hell"]
text = input("Enter a text: ")

# 1. Perform text filtering
filtered_text = filter_text(text, forbidden_words)
print("\nFiltered Text:", filtered_text)

# 2. Validate the filtered text
is_valid, validation_message = validate_script(filtered_text)
print("\nValidation Message:", validation_message)

if is_valid:
    print("\nFinal Valid Text:", filtered_text)