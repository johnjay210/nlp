from nltk import ngrams
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

text = "Natural language processing helps computers understand human language"

tokens = word_tokenize(text)
trigrams = list(ngrams(tokens, 3))

print("Trigrams:")
print(trigrams)