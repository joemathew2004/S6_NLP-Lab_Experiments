import re
import nltk

# nltk.download('punkt')

def concord(tokens, context_size, target):
    concordances = []
    for i, w in enumerate(tokens):
        if w.lower() == target.lower():
            start = max(0, i - context_size)
            end = min(len(tokens), i + context_size + 1)
            concordance = " ".join(tokens[start:end])
            concordances.append(concordance)
    return concordances

text = input("Enter your text: ")
target = input("Enter the word: ").strip().lower()
context_size = 5  # Number of words before and after the target

tokens = nltk.word_tokenize(text)

result = concord(tokens, context_size, target)  # Find concordances

print(f"Concordance for '{target}': ")

for i in result:
    print(i, end='\n')