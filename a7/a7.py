import math, os, pickle, re
from typing import Tuple, List, Dict


class BayesClassifier:
    """A simple BayesClassifier implementation

    Attributes:
        pos_freqs - dictionary of frequencies of positive words
        neg_freqs - dictionary of frequencies of negative words
        pos_filename - name of positive dictionary cache file
        neg_filename - name of positive dictionary cache file
        training_data_directory - relative path to training directory
        neg_file_prefix - prefix of negative reviews
        pos_file_prefix - prefix of positive reviews
    """

    def __init__(self):
        """Constructor initializes and trains the Naive Bayes Sentiment Classifier. If a
        cache of a trained classifier is stored in the current folder it is loaded,
        otherwise the system will proceed through training.  Once constructed the
        classifier is ready to classify input text."""
        # initialize attributes
        self.pos_freqs: Dict[str, int] = {}
        self.neg_freqs: Dict[str, int] = {}
        self.pos_filename: str = "pos.dat"
        self.neg_filename: str = "neg.dat"
        self.training_data_directory: str = "movie_reviews/"
        self.neg_file_prefix: str = "movies-1"
        self.pos_file_prefix: str = "movies-5"

        # check if both cached classifiers exist within the current directory
        if os.path.isfile(self.pos_filename) and os.path.isfile(self.neg_filename):
            print("Data files found - loading to use cached values...")
            self.pos_freqs = self.load_dict(self.pos_filename)
            self.neg_freqs = self.load_dict(self.neg_filename)
        else:
            print("Data files not found - running training...")
            self.train()

    def train(self) -> None:
        """Trains the Naive Bayes Sentiment Classifier
        
        Train here means generates `pos_freq/neg_freq` dictionaries with frequencies of
        words in corresponding positive/negative reviews
        """
        # Get the list of file names from the training data directory
        _, __, files = next(os.walk(self.training_data_directory), (None, None, []))
        if not files:
            raise RuntimeError(f"Couldn't find path {self.training_data_directory}")
        
        # Load the stopwords from the provided file
        
        file = self.load_file("sorted_stoplist.txt")
        stopwords = self.tokenize(file)
        
        # Process each file
        for index, filename in enumerate(files, 1):  # type: ignore
            print(f"Training on file {index} of {len(files)}")
            
            # Load the file content
            filepath = os.path.join(self.training_data_directory, filename)
            text = self.load_file(filepath)
            
            # Tokenize the text
            tokens = self.tokenize(text)
            filtered_tokens = [token for token in tokens if token not in stopwords]
            # print(filtered_tokens)
            # Update the appropriate frequency dictionary based on file prefix
            if filename.startswith(self.pos_file_prefix):
                self.update_dict(filtered_tokens, self.pos_freqs)
            elif filename.startswith(self.neg_file_prefix):
                self.update_dict(filtered_tokens, self.neg_freqs)
    
        # Save the dictionaries for future use
        self.save_dict(self.pos_freqs, self.pos_filename)
        self.save_dict(self.neg_freqs, self.neg_filename)

    def classify(self, text: str) -> str:
        """Classifies given text as positive, negative or neutral from calculating the
        most likely document class to which the target string belongs
        
        Args:
            text - text to classify
            
        Returns:
            classification, either positive, negative or neutral
        """
        # Tokenize the input text
        tokens = self.tokenize(text)
        
        # Create the stopword list
        file = self.load_file("sorted_stoplist.txt")
        stopwords = self.tokenize(file)

        # Initialize probability scores (we use logs to prevent underflow)
        pos_score = 0
        neg_score = 0
        
        # Calculate total word counts for each class
        pos_total = sum(self.pos_freqs.values())
        neg_total = sum(self.neg_freqs.values())

        # Vocabulary size (for add-one smoothing)
        vocab = set(self.pos_freqs.keys()).union(set(self.neg_freqs.keys()))
        vocab_size = len(vocab)
        print(vocab_size)
        
        # Calculate probability for each token
        for token in tokens:
            # Get frequency of token in each class (with add-one smoothing)
            if token not in stopwords:
                pos_freq = self.pos_freqs.get(token, 0) + 1
                neg_freq = self.neg_freqs.get(token, 0) + 1
                
                # Calculate log probabilities and add to running totals
                pos_score += math.log(pos_freq / (pos_total + vocab_size))
                neg_score += math.log(neg_freq / (neg_total + vocab_size))
        
        # For debugging purposes
        print(f"Positive score: {pos_score}, Negative score: {neg_score}")
        
        # Return classification based on higher probability
        if pos_score > neg_score:
            return "positive"
        else:
            return "negative"

    def load_file(self, filepath: str) -> str:
        """Loads text of given file

        Args:
            filepath - relative path to file to load

        Returns:
            text of the given file
        """
        with open(filepath, "r", encoding='utf8') as f:
            return f.read()

    def save_dict(self, dict: Dict, filepath: str) -> None:
        """Pickles given dictionary to a file with the given name

        Args:
            dict - a dictionary to pickle
            filepath - relative path to file to save
        """
        print(f"Dictionary saved to file: {filepath}")
        with open(filepath, "wb") as f:
            pickle.Pickler(f).dump(dict)

    def load_dict(self, filepath: str) -> Dict:
        """Loads pickled dictionary stored in given file

        Args:
            filepath - relative path to file to load

        Returns:
            dictionary stored in given file
        """
        print(f"Loading dictionary from file: {filepath}")
        with open(filepath, "rb") as f:
            return pickle.Unpickler(f).load()

    def tokenize(self, text: str) -> List[str]:
        """Splits given text into a list of the individual tokens in order

        Args:
            text - text to tokenize

        Returns:
            tokens of given text in order
        """
        tokens = []
        token = ""
        for c in text:
            if (
                re.match("[a-zA-Z0-9]", str(c)) != None
                or c == "'"
                or c == "_"
                or c == "-"
            ):
                token += c
            else:
                if token != "":
                    tokens.append(token.lower())
                    token = ""
                if c.strip() != "":
                    tokens.append(str(c.strip()))

        if token != "":
            tokens.append(token.lower())
        return tokens

    def update_dict(self, words: List[str], freqs: Dict[str, int]) -> None:
        """Updates given (word -> frequency) dictionary with given words list

        By updating we mean increment the count of each word in words in the dictionary.
        If any word in words is not currently in the dictionary add it with a count of 1.
        (if a word is in words multiple times you'll increment it as many times
        as it appears)

        Args:
            words - list of tokens to update frequencies of
            freqs - dictionary of frequencies to update
        """
        # TODO: your work here
        for word in words:
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1


if __name__ == "__main__":
    # uncomment the below lines once you've implemented `train` & `classify`
    b = BayesClassifier()
    a_list_of_words = ["I", "really", "like", "this", "movie", ".", "I", "hope", \
                       "you", "like", "it", "too"]
    a_dictionary = {}
    b.update_dict(a_list_of_words, a_dictionary)
    assert a_dictionary["I"] == 2, "update_dict test 1"
    assert a_dictionary["like"] == 2, "update_dict test 2"
    assert a_dictionary["really"] == 1, "update_dict test 3"
    assert a_dictionary["too"] == 1, "update_dict test 4"
    print("update_dict tests passed.")

    pos_denominator = sum(b.pos_freqs.values())
    neg_denominator = sum(b.neg_freqs.values())

    print("\nThese are the sums of values in the positive and negative dicitionaries.")
    print(f"sum of positive word counts is: {pos_denominator}")
    print(f"sum of negative word counts is: {neg_denominator}")

    # print("\nHere are some sample word counts in the positive and negative dicitionaries.")
    # print(f"count for the word 'love' in positive dictionary {b.pos_freqs['love']}")
    # print(f"count for the word 'love' in negative dictionary {b.neg_freqs['love']}")
    # print(f"count for the word 'terrible' in positive dictionary {b.pos_freqs['terrible']}")
    # print(f"count for the word 'terrible' in negative dictionary {b.neg_freqs['terrible']}")
    # print(f"count for the word 'computer' in positive dictionary {b.pos_freqs['computer']}")
    # print(f"count for the word 'computer' in negative dictionary {b.neg_freqs['computer']}")
    # print(f"count for the word 'science' in positive dictionary {b.pos_freqs['science']}")
    # print(f"count for the word 'science' in negative dictionary {b.neg_freqs['science']}")
    # print(f"count for the word 'i' in positive dictionary {b.pos_freqs['i']}")
    # print(f"count for the word 'i' in negative dictionary {b.neg_freqs['i']}")
    # print(f"count for the word 'is' in positive dictionary {b.pos_freqs['is']}")
    # print(f"count for the word 'is' in negative dictionary {b.neg_freqs['is']}")
    # print(f"count for the word 'the' in positive dictionary {b.pos_freqs['the']}")
    # print(f"count for the word 'the' in negative dictionary {b.neg_freqs['the']}")

    print("\nHere are some sample probabilities.")
    print(f"P('love'| pos) {(b.pos_freqs['love']+1)/pos_denominator}")
    print(f"P('love'| neg) {(b.neg_freqs['love']+1)/neg_denominator}")
    print(f"P('terrible'| pos) {(b.pos_freqs['terrible']+1)/pos_denominator}")
    print(f"P('terrible'| neg) {(b.neg_freqs['terrible']+1)/neg_denominator}")

    # uncomment the below lines once you've implemented `classify`
    print("\nThe following should all be positive.")
    print(b.classify('I love computer science'))
    print(b.classify('this movie is fantastic'))
    print("\nThe following should all be negative.")
    print(b.classify('rainy days are the worst'))
    print(b.classify('computer science is terrible!.'))

    print()
    print(b.classify("I am so happy I can't stop smiling seriously"))

    