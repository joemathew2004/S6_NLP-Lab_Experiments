import re

def regex_tagger(text, patterns):
    tagged_words = []
    words = text.split()  # Simple word splitting

    for word in words:
        tag = "UNK"  # Default tag (Unknown)
        for pattern, tag_name in patterns:
            if re.match(pattern, word, re.IGNORECASE): #ignore case.
                tag = tag_name
                break  # Stop after the first match
        tagged_words.append((word, tag))
    return tagged_words

tag_patterns = [
    (r"^(a|an|the)$", "DET"),  # Determiners
    (r"^[A-Z][a-z]*$", "NNP"),  # Proper nouns (start with uppercase)
    (r"^[0-9]+$", "CD"),     # Cardinal numbers
    (r"^(is|are|was|were|be|being|been)$", "VB"), #Verbs
    (r"^(he|she|it|they|we|you|i|him|her|them|us|me)$", "PRP"), #Pronouns
    (r"^[a-z]+ing$", "VBG"), #Gerund
    (r"^[a-z]+ed$", "VBD"), #Past tense
    (r"^[a-z]+ly$", "RB"), #Adverbs
]

text = "The quick brown fox jumps over 10 lazy dogs. John is running quickly."
tagged_text = regex_tagger(text, tag_patterns)

for word, tag in tagged_text:
    print(f"{word}: {tag}")


