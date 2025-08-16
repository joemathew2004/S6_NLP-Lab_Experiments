import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

''' nltk.download('punkt')  		        # For word tokenization
    nltk.download('maxent_ne_chunker')  	# For named entity chunking
    nltk.download('words')  		        # For word list (used in NER)
    nltk.download('maxent_ne_chunker_tab')  # For missing resource
    nltk.download('averaged_perceptron_tagger') '''

# Label expansion dictionary
label_expansion = {
    'PERSON': 'Person',
    'ORGANIZATION': 'Organization',
    'GPE': 'Geopolitical Entity',
    'LOCATION': 'Location',
    'FACILITY': 'Facility',
    'TIME': 'Time',
    'MONEY': 'Money',
    'PERCENT': 'Percentage',
    'DATE': 'Date',
    'NORP': 'Nationalities or Religious or Political Groups',
    'ORDINAL': 'Ordinal',
    'CARDINAL': 'Cardinal Numbers'
}

text = input("Enter a sentence for Named Entity Recognition: ")
tokens = word_tokenize(text)
print("Tokens:", tokens)

tagged_tokens = pos_tag(tokens)		# POS Tagging
print("POS tagged tokens:", tagged_tokens)

ner_tree = ne_chunk(tagged_tokens)	# Named Entity Recognition using ne_chunk

# Displaying the named entities in a more readable format
named_entities = []
for subtree in ner_tree:
    if isinstance(subtree, nltk.Tree):          # If it's a named entity subtree
        entity = " ".join([word for word, tag in subtree.leaves()])
        label = subtree.label()
        expanded_label = label_expansion.get(label, "Unknown")  # Get expanded label
        named_entities.append((entity, label, expanded_label))

print("\nExtracted Named Entities:")
for entity, label, expanded_label in named_entities:
    print(f"{entity}: {label} ({expanded_label})")
# ----------------------------------------------------------------------------------------------------------

'''
import spacy

# Load spaCy English model (run: python -m spacy download en_core_web_sm if needed)
nlp = spacy.load("en_core_web_sm")

label_expansion = {
    'PERSON': 'Person',
    'ORG': 'Organization',
    'GPE': 'Geopolitical Entity',
    'LOC': 'Location',
    'FAC': 'Facility',
    'TIME': 'Time',
    'MONEY': 'Money',
    'PERCENT': 'Percentage',
    'DATE': 'Date',
    'NORP': 'Nationalities or Religious or Political Groups',
    'ORDINAL': 'Ordinal',
    'CARDINAL': 'Cardinal Numbers'
}

# Input from user
text = input("Enter a sentence for Named Entity Recognition: ")
doc = nlp(text)

# Tokenization (spaCy handles it automatically)
tokens = [token.text for token in doc]
print("Tokens:", tokens)

# POS tagging (optional)
tagged_tokens = [(token.text, token.pos_) for token in doc]
print("POS tagged tokens:", tagged_tokens)

# Named Entity Recognition
named_entities = []
for ent in doc.ents:
    entity = ent.text
    label = ent.label_
    expanded_label = label_expansion.get(label, "Unknown")
    named_entities.append((entity, label, expanded_label))

# Output
print("\nExtracted Named Entities:")
for entity, label, expanded_label in named_entities:
    print(f"{entity}: {label} ({expanded_label})")
'''