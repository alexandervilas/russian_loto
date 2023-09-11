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

number = [i for i in range(1, 91)]  #Здесь я добавил диапазон возможных чисел
card = sorted(random.sample(number, 15)) #здесь я указываю, что в карточке будут рандомные числа в нашем диапазоне
def winner_found(): #создаю функцию по поиску победителя, победитель находится тогда, когда длина карточки начинает равнятся нулю
    if len(card) == 0:
        return True
    return False #пока длина карточки не равняется нулю, мы продолжаем играть 

def main(): #создаем функцию самой игры, уже с самой игрой
    while (not winner_found()): #пока победитель не найден 
        print("\n### NEW GAME ###")
        random_choice = number.pop() #выпадает случайное число и если оно есть, то его удаляем по индексу с длины карточки 
        print("The random lotto is: {} ".format(random_choice))
        if random_choice in card:
            card.remove(random_choice) #удаляет первый элемент последовательности по назначению