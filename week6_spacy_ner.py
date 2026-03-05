import spacy

nlp = spacy.load("en_core_web_sm")

text = "Microsoft was founded by Bill Gates in the United States."

doc = nlp(text)

for ent in doc.ents:
    print("Entity:", ent.text, "Label:", ent.label_)