
import random

#Это будет простая игра в русское лото

# Функция, которая должна показывать карточку игрока, при вводу двух аргументов
def show_card(player, card):
    card = player
    print("Карточка игрока" + " №" + player + "\n" + card)

def create_dict_with_lists(num_lists):
    """
   
    """
    result_dict = {}
    for i in range(num_lists):
        result_dict[f'list_{i+1}'] = []
    return result_dict


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

my_dict = create_dict_with_lists(3)
print(my_dict)


