import unittest
from calc_marat import *
from Svetozar_05_dict import *


test_suite_add = [
    ['99', '1', '10', '100'],
    ['1111', '10', '2', '10001'],
    ['FFA', 'DFA', '16', '1DF4'],
    ['AEFDA', 'ACD', '16', 'AFAA7'],
    ['EB7F9ADBD', 'C9B12EDA', '16', 'F81AADC97'],
    ['1', '1', '10', '2'],
    ['9951845645', '6845354127841631', '10', '6845364079687276'],
    ['57', '0', '10', '57'],
    ['456', '23', '8', '501'],
    ['46725562626', '425166371662351', '8', '425235317445177'],
    ['0', '110001', '2',  '110001'],
    ['10010001100111001110', '10010001100111001110111101', '2', '10010011111000110110001011'],
    ['1', '7', '8', '10'],
    ['0', '0', '10', '0'],
    ['8', '102', '10',  '110'],
    ['1', '99', '10', '100']
]

test_suite_sub = [
    ['9', '5', '10', '4'],
    ['110100101001001001', '100110010001', '2', '110100000010111000'],
    ['1110', '1010', '2', '100'],
    ['0', '1', '10', '-1'],
    ['2456345162616672', '4535251523', '8', '2456340425345147'],
    ['53', '46', '8', '5'],
    ['100', '1', '10', '99'],
    ['900000000000000000', '1', '10', '899999999999999999'],
    ['FFEB', 'AB1', '16', 'F53A'],
    ['53CE8FF', '8EAC', '16', '53C5A53'],
    ['999', '999', '10', '0'],
    ['0', '0', '2', '0']
]



class CalculatorTest(unittest.TestCase):


    def test_add(self):
        for num1, num2, system, total in test_suite_add:
            self.assertEqual(Calculator.__add__(self,num1, num2, system), (total, system))
            self.assertEqual(to_calc(num1, num2, system, '+'), (total, system))


    def test_sub(self):
        for num1, num2, system, total in test_suite_sub:
            self.assertEqual(Calculator.__sub__(self,num1, num2, system), (total, system))
            self.assertEqual(to_calc(num1, num2, system, '-'), (total, system))






if __name__ == '__main__':
    unittest.main()
