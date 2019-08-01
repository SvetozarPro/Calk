from time import perf_counter
from random import randint
from calculator_svetozar import *
from calculator_marat import *


def maker(function):
    def calc_time(value1, value2, notation, operation):
        start = perf_counter()
        function(value1, value2, notation, operation)
        end = perf_counter()
        return end - start
    return calc_time


def get_two_big_num():
    first = revers_nums[randint(1, 15)]
    second = revers_nums[randint(1, 15)]
    for i in range(149):
        first += revers_nums[randint(0, 15)]
    for i in range(99):
        second += revers_nums[randint(0, 15)]
    return str(first), str(second)


operations = ['+', '-', '*', '//']


with open("calculator_test_timing_results.tsv", "w") as file_out:
    test_functions = [calc_svetozar, calc_marat]
    for func in test_functions:
        timer = maker(func)
        file_out.write("Функция\t{}\n".format(str(func.__name__)))
        for i in range(len(operations)):
            file_out.write("Операция\t{}\n".format(operations[i]))
            file_out.write("Система счисления\t16")
            operation_time = 0.0
            for j in range(1000):
                operation_time += timer(*get_two_big_num(), '16', operations[i])
            file_out.write("150 и 100 цифр 1000 раз, сек\t" + f"{operation_time:.3f}")
            print(str(func.__name__), operations[i], f"{operation_time:.3f}")
