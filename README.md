# NLP Programs - S6 AI & ML Lab

This repository contains Natural Language Processing (NLP) programs developed during the 6th semester AI & ML lab hours. The programs cover fundamental to advanced NLP concepts and techniques.

## 📁 Repository Structure

### Core NLP Programs
- **2_preprocessing.py** - Text preprocessing pipeline (tokenization, stemming, lemmatization, stop word removal)
- **3_counting.py** - Word frequency analysis and Type-Token Ratio (TTR) calculation
- **4_concordances.py** - Concordance analysis for word context examination
- **5_BagOfWords.py** - Bag of Words model implementation with cosine similarity
- **6_similarsentence.py** - Sentence similarity analysis
- **7_HMM.py** - Hidden Markov Model implementation
- **8_NER.py** - Named Entity Recognition using NLTK and spaCy
- **9_parsing.py** - Syntactic parsing techniques

### Advanced Applications
- **10_keyword_chatbot.py** - Keyword-based chatbot implementation
- **10_ontology_chatbot.py** - Ontology-driven chatbot system
- **10_QA_pair.py** - Question-Answer pair processing
- **11_Text_Classification.py** - Text classification using Naive Bayes
- **12_tfidf.py** - TF-IDF (Term Frequency-Inverse Document Frequency) implementation
- **13_translator.py** - Language translation utilities
- **14_chatbot.py** - Advanced chatbot using Transformers (BlenderBot)

### Utility Scripts
- **spacy_ner.py** - spaCy-based Named Entity Recognition
- **spacy_pos.py** - Part-of-Speech tagging with spaCy
- **z_FILTERATION.py** - Text filtration techniques
- **z_K_means.py** - K-means clustering for text data
- **z_tagging_using_RE.py** - Regular expression-based tagging
- **zz_rough.py** - Development and testing script

### Data Files
- **data_11.csv** - Dataset for text classification
- **file4.txt, file5.txt, file6.txt** - Sample text files
- **input_EXP3.txt, output_EXP3.txt** - Input/output files for 3_counting.py

## 🛠️ Prerequisites

### Required Libraries
```bash
pip install nltk
pip install scikit-learn
pip install pandas
pip install spacy
pip install transformers
pip install emoji
```

### NLTK Data Downloads
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
```

### spaCy Model
```bash
python -m spacy download en_core_web_sm
```

## 🎯 Learning Objectives

This collection covers:
- **Text Preprocessing**: Cleaning and preparing text data
- **Feature Extraction**: Bag of Words, TF-IDF
- **Language Models**: N-grams, HMM
- **Information Extraction**: NER, POS tagging
- **Text Classification**: Sentiment analysis
- **Conversational AI**: Chatbot development
- **Similarity Analysis**: Document comparison
- **Parsing**: Syntactic analysis

## 🤝 Contributing

This is an academic project for S6 AI & ML lab. Programs are designed for educational purposes and demonstrate core NLP concepts.

## 📄 License

Educational use only - S6 AI & ML Laboratory Programs

---
*Developed for Natural Language Processing Laboratory - 6th Semester AI & ML*