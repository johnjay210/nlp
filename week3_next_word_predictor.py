from nltk.util import bigrams
from collections import defaultdict

text = "I love natural language processing and natural language models"

words = text.split()
bigram_pairs = list(bigrams(words))

model = defaultdict(list)

for w1, w2 in bigram_pairs:
    model[w1].append(w2)

print("Next word predictions for 'language':")
print(model["language"])