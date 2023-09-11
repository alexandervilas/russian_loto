# import random

# def create_loto_card():
#     card = []

#     for i in range(3):
#         row = random.sample(range(1, 91), 5)
#         card.append(row)

# или

import random

def generate_card():
card = random.sample(range(1, 91), 9)
return card

