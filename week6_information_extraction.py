import spacy

nlp = spacy.load("en_core_web_sm")

text = "Elon Musk founded SpaceX."

doc = nlp(text)

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)