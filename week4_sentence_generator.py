import random

subjects = ["The cat", "The dog", "A boy"]
verbs = ["eats", "chases", "sees"]
objects = ["a mouse", "the ball", "a car"]

sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}"

print(sentence)