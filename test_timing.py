from time import process_time
from Calk_Svetozar.Svetozar_05_dict import *


def calc_time(func):
    time = process_time()
    for i in range(100):
        func()
    time = (process_time() - time) / 100
    return time


to_calc = calc_time(to_calc)

