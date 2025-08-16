import spacy
nlp = spacy.load("en_core_web_sm")

text = input("Enter your text: ")
doc = nlp(text)

tokens = [token.text for token in doc]
print("\n--- Tokenization ---")
print(tokens)

pos_tags = [(token.text, token.pos_, token.tag_ ) for token in doc]
print("\n--- POS Tagging ---")
print(pos_tags)  # [('Apple', 'PROPN', 'NNP'), ('is', 'AUX', 'VBZ'), ('buying', 'VERB', 'VBG'), ...]

lemmas = [(token.text, token.lemma_) for token in doc]
print("\n--- Lemmatization ---")
print(lemmas)  # [('Apple', 'Apple'), ('is', 'be'), ('buying', 'buy'), ...]

print("\n--- Named Entity Recognition (NER) ---")
if doc.ents:
    ner_results = [(ent.text, ent.label_) for ent in doc.ents]
    print(ner_results)   # [('Apple', 'ORG'), ('UK', 'GPE')]
else:
    print([])

def concordance(doc, word, window=5):
    print(f"\n--- Concordance for '{word}' ---")
    tokens = [token.text for token in doc]
    matches = [i for i, t in enumerate(tokens) if t.lower() == word.lower()]
    
    if not matches:
        print([])
        return

    contexts = []
    for idx in matches:
        start = max(0, idx - window)
        end = min(len(tokens), idx + window + 1)
        context = tokens[start:end]
        contexts.append(context)
    
    print(contexts)

search_word = input("\nEnter a word to search for concordance: ")
concordance(doc, search_word)
