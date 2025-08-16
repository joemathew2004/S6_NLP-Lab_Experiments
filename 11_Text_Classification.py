import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import accuracy_score, classification_report

dataset_path = "C:/Users/joema//Documents (local)/S6/NLP Programs/data_11.csv"

df = pd.read_csv(dataset_path)
# df = pd.read_csv(dataset_path, names=['text', 'sentiment'], header=None)

print(df.head())

X = df['text']          # Text data column
y = df['sentiment']     # Sentiment label column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = MultinomialNB()             # Model training
model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

while True:
    user_input = input("\nEnter a sentence or query to predict sentiment (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the program...")
        break
    
    user_input_tfidf = vectorizer.transform([user_input])
    predicted_label = model.predict(user_input_tfidf)
    print(f"Predicted Sentiment: {predicted_label[0]}")
