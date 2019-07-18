from time import process_time
from itertools import starmap, combinations_with_replacement as comb
from Calk_Svetozar.Svetozar_05_dict import *


def calc_time(value1, value2, notation, operation):
    time = process_time()
    for i in range(100):
        to_calc(value1, value2, notation, operation)
    time = (process_time() - time) / 100
    return time


length_list = [1, 5, 10, 20, 50]  # список количества разрядов чисел для тестов
num_sys_list = [['2', '1'], ['8', '7'], ['10', '9'], ['16', 'F']]
operations = ['+', '-', '*', '//']
test_suit = [
    [(i, j, num_sys, operation)
     for num_sys, num in num_sys_list
     for i, j in comb([num*k for k in length_list], 2)]
    for operation in operations
]

# addition_time = [list(starmap(calc_time, num_sys)) for num_sys in test_suit_add]
