#Это будет простая игра в русское лото


import random

def generate_card():
card = random.sample(range(1, 91), 9)
return card