
import sys, os, time
import string
sys.path.append('/storage/emulated/0/pydroid3/projects/The machine')
from common import clear_screen as cls
#Basic text processor with word frequency count
class TextAnalyzer:
    def __init__(self, text):
        self.text = text.lower()  # Make everything lowercase
        self.cleaned_text = ""
        self.word_counts = {}

    def clean_text(self):
        # Remove punctuation
        for char in self.text:
            if char not in string.punctuation:
                self.cleaned_text += char
        return self.cleaned_text

    def count_words(self):
        if not self.cleaned_text:
            self.clean_text()

        words = self.cleaned_text.split()
        for word in words:
            if word in self.word_counts:
                self.word_counts[word] += 1
            else:
                self.word_counts[word] = 1
        return self.word_counts


def analize():
    while True:
        try:
            cls()
            print("Text Analyzer With Word Frequency_Count\n")
            choice = input("Options:\n1. Clean Yext\nEnter Choice: ")
            if choice == "1":
                cls()
                input_text = input("Enter Text: ")
                cls()
                analyzer = TextAnalyzer(input_text)
                print("\nCleaned Text:", analyzer.clean_text())
                choice = input("Press Enter to View Word Count or any letter to go Back: ")
                cls()
                if choice == "":
                    cls()
                    print("Word Counts:", analyzer.count_words())
                    input("Press Enter to go Back")
                    cls()
            elif choice == "4":
                break
            else:
                print("Invalid input")
        except Exception as e:
            print(f"{e}")
        except ImportError as e:
            print(f"Import Error! {e}")



# ==== USAGE ====
if __name__ == "__main__":
   analize()
    


import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class SimpleNLP:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = CountVectorizer()
        self.classifier = MultinomialNB()
        self.trained = False

    def preprocess(self, text):
        tokens = nltk.word_tokenize(text.lower())
        tokens = [t for t in tokens if t not in string.punctuation]
        filtered = [self.lemmatizer.lemmatize(t) for t in tokens if t not in self.stop_words]
        return " ".join(filtered)

    def train(self, texts, labels):
        processed = [self.preprocess(t) for t in texts]
        X = self.vectorizer.fit_transform(processed)
        self.classifier.fit(X, labels)
        self.trained = True

    def predict_intent(self, text):
        if not self.trained:
            return "NLP Engine not trained."
        processed = self.preprocess(text)
        X = self.vectorizer.transform([processed])
        return self.classifier.predict(X)[0]

nlp = SimpleNLP()
def Training():
    # Sample training data (you can expand this!)
    texts = [
        "shutdown the system", 
        "show me the surveillance feed", 
        "analyze the target behavior",
        "gather intel from the scene"
    ]
    labels = ["shutdown", "show_feed", "analyze", "gather_intel"]

    nlp.train(texts, labels)

    # Test inputs
    test_input = input("Enter Training Test Input: ")
    intent = nlp.predict_intent(test_input)
    print(f"Intent Detected: {intent}")

# === USAGE ===
if __name__ == "__main__":
    nlp = SimpleNLP()




