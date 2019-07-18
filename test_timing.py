from time import process_time
from itertools import starmap
from Calk_Svetozar.Svetozar_05_dict import *


def calc_time(value1, value2, notation, operation):
    time = process_time()
    for i in range(100):
        to_calc(value1, value2, notation, operation)
    time = (process_time() - time) / 100
    return time


length_list = [1, 5, 10, 20, 50]  # список количества разрядов чисел для тестов

test_suit_add = [
    [(i, j, '2', '+') for i in ['1'*k for k in length_list] for j in ['1'*k for k in length_list]],
    [(i, j, '8', '+') for i in ['7'*k for k in length_list] for j in ['7'*k for k in length_list]],
    [(i, j, '10', '+') for i in ['9'*k for k in length_list] for j in ['9'*k for k in length_list]],
    [(i, j, '16', '+') for i in ['F'*k for k in length_list] for j in ['F'*k for k in length_list]]
]

addition_time = [list(starmap(calc_time, num_sys)) for num_sys in test_suit_add]
