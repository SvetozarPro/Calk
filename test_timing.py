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
print(test_suit)


test_functions = [to_calc]
for func in test_functions:
    operations_times = [list(starmap(calc_time, num_sys)) for num_sys in test_suit]
    print("Тестируемая функция: {0}".format(str(func)))
    for i in range(len(operations)):
        print("\tТестируемая операция: {0}".format(operations[i]))
        for j in range(len(num_sys_list)):
            print("\t\t{0[0]}: {1}".format(num_sys_list[j],
                                           operations_times[i][j*len(operations_times)//len(operations):
                                                               (j+1)*len(operations_times)//len(operations)]))
    print("Суммарнове время прохождения теста: {0}".format(sum(operations_times)))
