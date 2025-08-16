import nltk
from nltk.corpus import wordnet
import re

# nltk.download('punkt')
# nltk.download('wordnet')

def get_synonyms(word):
    """Returns a list of synonyms for a given word."""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def get_antonyms(word):
    """Returns a list of antonyms for a given word."""
    antonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                for antonym in lemma.antonyms():
                    antonyms.add(antonym.name())
    return list(antonyms)

def replace_words(text):
    """Replaces words with synonyms and negations with antonyms."""
    words = nltk.word_tokenize(text)
    replaced_words = []

    for word in words:
        if word.lower() in ["not", "no", "never", "n't"]:  # Handle negations
            if replaced_words:  # Check if there's a previous word
                prev_word = replaced_words.pop()
                antonyms = get_antonyms(prev_word)
                if antonyms:
                    replaced_words.append(antonyms[0])  # Replace with the first antonym
                else:
                    replaced_words.append(prev_word) #If no antonym, keep the original.
            replaced_words.append("not") #keep the negation if there is no previous word.
        else:
            synonyms = get_synonyms(word)
            if synonyms:
                replaced_words.append(synonyms[0])  # Replace with the first synonym
            else:
                replaced_words.append(word) #if no synonym, keep original.

    return " ".join(replaced_words)

# Example Usage
text = "I don't like the bad weather. It's not good."
replaced_text = replace_words(text)
print(replaced_text)

text2 = "He is a good person. They are not bad."
replaced_text2 = replace_words(text2)
print(replaced_text2)

text3 = "They never go to the store."
replaced_text3 = replace_words(text3)
print(replaced_text3)

text4 = "It is a beautiful day."
replaced_text4 = replace_words(text4)
print(replaced_text4)