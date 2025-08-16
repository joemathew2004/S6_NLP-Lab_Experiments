import re
import nltk
# import contractions
import emoji

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

# Initialize stop words, stemmer, and lemmatizer
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess_tweet(tweet):
    print('Original tweet:', tweet)

    # Convert to lowercase
    tweet = tweet.lower()
    print('Conversion to lowercase:', tweet)

    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+', '', tweet)
    print('Removal of URLs:', tweet)

    # Remove emojis
    tweet = emoji.demojize(tweet)           # Convert emojis to text
    tweet = re.sub(r':\S+:', '', tweet)     # Remove emoji-related words
    print('Removal of emojis:', tweet)

    # Tokenize the tweet
    words = word_tokenize(tweet)
    print("Tokenized words:", words)

    # Remove punctuation
    words = [re.sub(r'[^\w\s]', '', word) for word in words if word.strip() != '']
    print("Removal of punctuation:", words)

    # Remove stop words
    words = [word for word in words if word not in stop_words]
    print("After removing stop words:", words)

    # Perform stemming
    words_stemmed = [stemmer.stem(word) for word in words]
    print("After stemming:", words_stemmed)

    # Perform lemmatization
    words_lemmatized = [lemmatizer.lemmatize(word) for word in words]
    print("After lemmatization:", words_lemmatized)

    return ' '.join(words_lemmatized)

def process_multiple_tweets(tweets):
    for tweet in tweets:
        preprocessed_tweet = preprocess_tweet(tweet)
        print("Final processed tweet:", preprocessed_tweet)
        print("-" * 50)

# Sample tweets
tweets = [
    "I can't believe it's already December! Check out https://example.com 😍",
    "Just bought a new phone, it's amazing! #excited #newphone",
    "Loving the new album @ https://JB.instagram.com from my favorite artist! 🎶 #musiclover"
]

process_multiple_tweets(tweets)
