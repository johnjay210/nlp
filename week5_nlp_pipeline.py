import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple was founded by Steve Jobs in California."

doc = nlp(text)

print("Tokens:")
for token in doc:
    print(token.text)

print("\nPOS Tags:")
for token in doc:
    print(token.text, token.pos_)

print("\nEntities:")
for ent in doc.ents:
    print(ent.text, ent.label_)