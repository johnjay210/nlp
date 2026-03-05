from collections import Counter
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

text = "NLP is interesting. NLP helps computers understand language."
words = word_tokenize(text.lower())

frequency = Counter(words)

print("Word Frequency:")
print(frequency)