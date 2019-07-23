from time import perf_counter_ns
from itertools import starmap
from Calk_Svetozar.Svetozar_05_dict import *
from marat_calc.calc_marat import *


def maker(function):
    def calc_time(value1, value2, notation, operation):
        start = perf_counter_ns()
        function(value1, value2, notation, operation)
        end = perf_counter_ns()
        return end - start
    return calc_time


length_list = [1, 5, 10, 20, 50]  # список количества разрядов чисел для тестов
num_sys_list = [['2', '1'], ['8', '7'], ['10', '9'], ['16', 'F']]
operations = ['+', '-', '*', '//']
test_suit = [
    [
        [
            (i, j, num_sys, operation)
            for i in [num*k for k in length_list]
            for j in [num*k for k in length_list]
        ]
        for num_sys, num in num_sys_list
    ]
    for operation in operations
]

test_functions = [to_calc, do_calc]
for func in test_functions:
    timer = maker(func)
    operations_times = [[list(starmap(timer, num_sys)) for num_sys in operator] for operator in test_suit]
    print("Функция: {}".format(str(func.__name__)))
    for i in range(len(operations)):
        print("Операция: {}".format(operations[i]))
        for j in range(len(num_sys_list)):
            print("Система счисления: {}".format(num_sys_list[j][0]))
            print("\t"+"\t\t\t\t".join(map(str, length_list)))
            for k in range(len(length_list)):
                space = (3 - len(str(operations_times[i][j][k*len(length_list)]))//8) * "\t"
                print(str(length_list[k])+"\t" +
                      space.join(map(str, operations_times[i][j][k*len(length_list):(k+1)*len(length_list)])))
