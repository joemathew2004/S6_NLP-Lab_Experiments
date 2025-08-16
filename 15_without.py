import nltk

def replace_words_with_dicts(text, synonym_dict, antonym_dict):
    """Replaces words with synonyms and negations with antonyms using predefined dictionaries."""
 
    words = nltk.word_tokenize(text)
    replaced_words = []

    for word in words:
        if word.lower() in ["not", "no", "never", "n't"]:  # Handle negations
            if replaced_words:  # Check if there's a previous word
                prev_word = replaced_words.pop()
                if prev_word.lower() in antonym_dict:
                    replaced_words.append(antonym_dict[prev_word.lower()])
                else:
                    replaced_words.append(prev_word)  # Keep original if no antonym
            replaced_words.append("not") #keep the negation
        else:
            if word.lower() in synonym_dict:
                replaced_words.append(synonym_dict[word.lower()])
            else:
                replaced_words.append(word)

    return " ".join(replaced_words)

# Example Dictionaries (you can expand these)
synonym_dict = {
    "good": "excellent",
    "bad": "terrible",
    "beautiful": "lovely",
    "like": "enjoy",
    "store": "shop"
}

antonym_dict = {
    "good": "bad",
    "bad": "good",
    "like": "dislike",
    "happy": "sad"
}

# Example Usage
text = "I don't like the bad weather. It's not good. The store is beautiful."
replaced_text = replace_words_with_dicts(text, synonym_dict, antonym_dict)
print(replaced_text)

text2 = "He is a good person. They are not bad."
replaced_text2 = replace_words_with_dicts(text2, synonym_dict, antonym_dict)
print(replaced_text2)

text3 = "They never go to the store."
replaced_text3 = replace_words_with_dicts(text3, synonym_dict, antonym_dict)
print(replaced_text3)

text4 = "It is a beautiful day."
replaced_text4 = replace_words_with_dicts(text4, synonym_dict, antonym_dict)
print(replaced_text4)