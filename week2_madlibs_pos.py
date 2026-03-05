import nltk

sentence = "The cat runs quickly"

tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)

for word, tag in tags:
    if tag.startswith('NN'):
        new_word = input(f"Replace noun '{word}' with another noun: ")
        sentence = sentence.replace(word, new_word)

print("New Sentence:", sentence)