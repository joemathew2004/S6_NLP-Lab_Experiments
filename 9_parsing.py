import nltk
from nltk import CFG, PCFG

def constituency_parsing_nltk(sentence):                # Define a simple context-free grammar (CFG)
    grammar = CFG.fromstring("""
      S -> NP VP
      NP -> Det N
      VP -> V NP
      Det -> 'the' | 'a'
      N -> 'cat' | 'dog' | 'man' | 'ball'
      V -> 'chased' | 'ate' | 'kicked'
    """)

    parser = nltk.ChartParser(grammar)		            # Create a parser

    try:
        print("Constituency Parsing using NLTK:")	    # Generate the parse tree
        for tree in parser.parse(sentence):
            tree.pretty_print()
            
    except ValueError:
        print("Error: Sentence could not be parsed. Try a simpler sentence.")

def probabilistic_parsing_nltk(sentence):               # Define a simple probabilistic context-free grammar (PCFG)
    pcfg = PCFG.fromstring("""
      S -> NP VP [1.0]
      NP -> Det N [1.0]
      NP -> Det N PP [0.2]
      VP -> V NP [0.7]
      VP -> V [0.3]
      Det -> 'the' [0.9]
      Det -> 'a' [0.1]
      N -> 'cat' [0.3]
      N -> 'dog' [0.3]
      N -> 'man' [0.2]
      N -> 'ball' [0.2]
      V -> 'chased' [0.5]
      V -> 'ate' [0.3]
      V -> 'kicked' [0.2]
      PP -> P NP [1.0]
      P -> 'on' [1.0]
    """)

    parser = nltk.ChartParser(pcfg)		                # Create a parser

    try:
        print("\nProbabilistic Parsing using NLTK:")	# Generate the parse tree
        for tree in parser.parse(sentence):
            tree.pretty_print()
            
    except ValueError:
        print("Error: Sentence could not be parsed. Try a simpler sentence.")

def main():
    sentence = input("Enter a sentence: ").lower().split()
    constituency_parsing_nltk(sentence)
    probabilistic_parsing_nltk(sentence)

if __name__ == "__main__":
    main()
