#Это будет простая игра в русское лото
# Савельев
import random

def  generate_card():
    card = random.sample(range(1, 91), 15)
    return card
1
