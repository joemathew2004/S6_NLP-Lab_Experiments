'''import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import string

def process_text(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()

    text = text.lower()             # to lowercase
    tokens = word_tokenize(text)    # tokenize
    tokens = [word for word in tokens if word not in string.punctuation]  # remove punctuation

    num_tokens = len(tokens)            # Number of words (tokens) in the text

    distinct_tokens = set(tokens)       # Number of distinct words (types) in the text
    num_dist_tokens = len(distinct_tokens)

    freq_dist = FreqDist(tokens)        # Frequency distribution of all words in the text

    word_percentages = {word: (freq / num_tokens) * 100 for word, freq in freq_dist.items()}  # Calculate the percentage for each word

    TTR = (num_dist_tokens / num_tokens) * 100 if num_tokens > 0 else 0  # Type-Token Ratio (TTR)

    output_data = []

    output_data.append(f"Number of words (tokens): {num_tokens}")
    output_data.append(f"Number of distinct words (types): {num_dist_tokens}")

    output_data.append("\nWord Frequencies and Percentages:")

    for word in sorted(freq_dist.keys()):
        freq = freq_dist[word]
        percentage = word_percentages[word]
        output_data.append(f"{word}: Frequency = {freq}, Percentage = {percentage:.2f}%")

    output_data.append(f"\nType-Token Ratio (TTR): {TTR:.2f}%")

    with open(output_file, 'w') as f:
        f.write("\n".join(output_data))

input_file = 'input_EXP3.txt'
output_file = 'output_EXP3.txt'

process_text(input_file, output_file)
'''

import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import string

def process_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in string.punctuation]

    num_tokens = len(tokens)
    distinct_tokens = set(tokens)
    num_dist_tokens = len(distinct_tokens)

    freq_dist = FreqDist(tokens)
    word_percentages = {word: (freq / num_tokens) * 100 for word, freq in freq_dist.items()}

    TTR = (num_dist_tokens / num_tokens) * 100 if num_tokens > 0 else 0

    output_data = []

    output_data.append(f"Number of words (tokens): {num_tokens}")
    output_data.append(f"Number of distinct words (types): {num_dist_tokens}")

    output_data.append("\nWord Frequencies and Percentages:")

    for word in sorted(freq_dist.keys()):
        freq = freq_dist[word]
        percentage = word_percentages[word]
        output_data.append(f"{word}: Frequency = {freq}, Percentage = {percentage:.2f}%")

    output_data.append(f"\nType-Token Ratio (TTR): {TTR:.2f}%")

    return "\n".join(output_data)

# Example Usage:
text = "This is a test. This is only a test. Is it working?"
result = process_text(text)
print(result)