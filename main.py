#Это будет простая игра в русское лото
def create_dict_with_lists(num_lists):
    """
   
    """
    result_dict = {}
    for i in range(num_lists):
        result_dict[f'list_{i+1}'] = []
    return result_dict


my_dict = create_dict_with_lists(3)
print(my_dict)

import random

number = [i for i in range(1, 91)]
card = sorted(random.sample(number, 15))
def winner_found():
    if len(card) == 0:
        return True
    return False

def main():
    while (not winner_found()):
        print("\n### NEW GAME ###")
        random_choice = number.pop()
        print("The random lotto is: {} ".format(random_choice))
        if random_choice in card:
            card.remove(random_choice)