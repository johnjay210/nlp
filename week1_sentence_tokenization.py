import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

text = """Natural Language Processing is a branch of Artificial Intelligence.
It helps computers understand human language.
Many applications like chatbots and translation use NLP."""

sentences = sent_tokenize(text)

print("Sentences:")
for s in sentences:
    print(s)