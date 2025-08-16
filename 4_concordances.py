import re
import nltk
from nltk.text import Text
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def find_concordance(word, text_data):
    tokens = word_tokenize(text_data)          # word tokeniazation
    tokens = [word for word in tokens if word not in stop_words]  # removing stop words

    text = Text(tokens)             # tokens to nltk objects

    print(f"Concordance for '{word}':")
    text.concordance(word)          # finding concordance
    

with open('file4.txt', 'r') as file:   # reading text file
    sample_text = file.read()

sample_text = re.sub(r'[^\w\s]', '', sample_text)       # removing punctuations 

search_word = input("Enter the word: ").strip().lower()

find_concordance(search_word, sample_text)