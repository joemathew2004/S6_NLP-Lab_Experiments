import spacy

nlp = spacy.load("en_core_web_sm")

def pos_tag_spacy(text):
    doc = nlp(text)
    print(doc)
    tagged_words = [(token.text, token.pos_) for token in doc]
    return tagged_words

text = "The quick brown fox jumps over the lazy dog."
tagged_text = pos_tag_spacy(text)
print(tagged_text)

text2 = "I am running quickly to the store."
tagged_text2 = pos_tag_spacy(text2)
print(tagged_text2)

'''
The quick brown fox jumps over the lazy dog.
[('The', 'DET'), ('quick', 'ADJ'), ('brown', 'ADJ'), ('fox', 'NOUN'), 
('jumps', 'VERB'), ('over', 'ADP'), ('the', 'DET'), ('lazy', 'ADJ'), ('dog', 'NOUN'), ('.', 'PUNCT')]
I am running quickly to the store.
[('I', 'PRON'), ('am', 'AUX'), ('running', 'VERB'), ('quickly', 'ADV'), ('to', 'ADP'), 
('the', 'DET'), ('store', 'NOUN'), ('.', 'PUNCT')]'''