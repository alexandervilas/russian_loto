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

