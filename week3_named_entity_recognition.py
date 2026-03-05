import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

text = "Barack Obama was born in Hawaii."

tokens = word_tokenize(text)
tags = pos_tag(tokens)

entities = ne_chunk(tags)

print(entities)