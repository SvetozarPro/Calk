from time import process_time
from Calk_Svetozar.Svetozar_05_dict import *


def calc_time(func):
    time = process_time()
    func()
    time = process_time() - time
    return time


to_calc = calc_time(to_calc)

