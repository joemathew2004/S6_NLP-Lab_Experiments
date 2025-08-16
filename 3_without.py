import string

def process_text(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()

    text = text.lower()  # Convert text to lowercase
    tokens = text.split()  # Split text into words

    # Remove punctuation
    tokens = [word.strip(string.punctuation) for word in tokens if word.strip(string.punctuation)]

    num_tokens = len(tokens)  # Number of words (tokens) in the text
    distinct_tokens = set(tokens)  # Number of distinct words (types) in the text
    num_dist_tokens = len(distinct_tokens)

    word_freq = {}  # Dictionary to store word frequencies

    for word in tokens:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    word_percentages = {word: (freq / num_tokens) * 100 for word, freq in word_freq.items()}  # Calculate percentage for each word

    TTR = (num_dist_tokens / num_tokens) * 100 if num_tokens > 0 else 0  # Type-Token Ratio (TTR)

    output_data = []

    output_data.append(f"Number of words (tokens): {num_tokens}")
    output_data.append(f"Number of distinct words (types): {num_dist_tokens}")

    output_data.append("\nWord Frequencies and Percentages:")  # Add frequency distribution and percentage of each word

    for word in sorted(word_freq.keys()):
        freq = word_freq[word]
        percentage = word_percentages[word]
        output_data.append(f"{word}: Frequency = {freq}, Percentage = {percentage:.2f}%")

    output_data.append(f"\nType-Token Ratio (TTR): {TTR:.2f}%")

    with open(output_file, 'w') as f:
        f.write("\n".join(output_data))

    print(f"Processing complete. Results written to {output_file}")

input_file = 'input_EXP3.txt'
output_file = 'output_EXP3.txt'

process_text(input_file, output_file)

