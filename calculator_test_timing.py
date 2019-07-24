from time import perf_counter_ns
from itertools import starmap
from calculator_svetozar import *
from calculator_matat import *


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

with open("calculator_test_timing_results.tsv", "w") as file_out:
    test_functions = [calc_svetozar, calc_marat]
    for func in test_functions:
        timer = maker(func)
        operations_times = [[list(starmap(timer, num_sys)) for num_sys in operator] for operator in test_suit]
        file_out.write("Функция\t{}\n".format(str(func.__name__)))
        for i in range(len(operations)):
            file_out.write("Операция\t{}\n".format(operations[i]))
            for j in range(len(num_sys_list)):
                file_out.write("Система счисления\t{}\n".format(num_sys_list[j][0]))
                file_out.write("Количество цифр\t" + "\t".join(map(str, length_list)) + "\n")
                for k in range(len(length_list)):
                    file_out.write(
                        str(length_list[k]) + "\t" +
                        "\t".join(map(str, operations_times[i][j][k*len(length_list):(k+1)*len(length_list)])) + "\n"
                    )
