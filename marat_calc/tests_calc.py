import unittest
from calc_marat import *
from Svetozar_05_dict import *


test_suite_add = [
    ['99', '1', '10', '100'],
    ['0', '01', '2', '1'],
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



class CalculatorTest(unittest.TestCase):


    def test_add(self):
        for num1, num2, system, total in test_suite_add:
            self.assertEqual(do_calc(num1, num2, system, '+'), (total, system))
            self.assertEqual(to_calc(num1, num2, system, '+'), (total, system))



if __name__ == '__main__':
    unittest.main()
