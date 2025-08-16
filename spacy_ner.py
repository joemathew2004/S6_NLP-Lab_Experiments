import spacy

nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    doc = nlp(text)
    named_entities = [(ent.text, ent.label_) for ent in doc.ents]
    return named_entities

# Example Usage
text = "Apple Inc. is planning to open a new store in London next Tuesday."
entities = extract_named_entities(text)
print(entities)

text2 = "Barack Obama visited the White House in Washington D.C."
entities2 = extract_named_entities(text2)
print(entities2)


'''      [('Apple Inc.', 'ORG'), ('London', 'GPE'), ('next Tuesday', 'DATE')]
         [('Barack Obama', 'PERSON'), ('the White House', 'ORG'), ('Washington D.C.', 'GPE')]      '''