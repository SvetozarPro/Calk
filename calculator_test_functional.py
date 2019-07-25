import unittest
import logging
from calculator_marat import *
from calculator_svetozar import *

logging.basicConfig(filename = 'tests_result.log', level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

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

test_suite_sub = [
    ['9', '5', '10', '4'],
    ['DC1EFA', 'EEFA1', '16', 'CD2F59'],
    ['10010001100111001110', '100100011001','2','10010001000010110101'],
    ['0', '1', '10', '-1'],
    ['100', '1', '10', '99'],
    ['900000000000000000', '1', '10', '899999999999999999'],
    ['FF', 'F0', '16', 'F'],
    ['5612346261622331', '1256643626', '8', '5612345002756503'],
    ['52', '42', '8', '10'],
    ['111', '111', '10', '0'],
    ['999', '999', '10', '0'],
    ['0', '0', '10', '0'],
    ['1110', '1001', '2', '101']
]
test_suite_mul = [
    ['0', '0', '10', '0'],
    ['0', '55', '10',  '0'],
    ['55', '0', '10',  '0'],
    ['999999999999999999', '555', '10',  '554999999999999999445'],
    ['555', '999999999999999999', '10', '554999999999999999445'],
    ['111', '10', '2', '1110'],
    ['7541', '561', '8', '5425321'],
    ['FA12', '5D', '16', '5AD88A'],
    ['100000001', '55', '10', '5500000055'],
    ['55', '100000001', '10', '5500000055']
]

test_suite_floordiv = [
    ['0', '10', '10', '0'],
    ['5', '10', '10', '0'],
    ['555', '31', '10', '17'],
    ['F', 'AA', '16', '0'],
    ['1110', '11', '2', '100'],
    ['7561', '11', '8', '667'],
    ['9999999999999', '15', '10', '666666666666'],
    ['15', '9999999999999', '10', '0'],
    ['1110100111001010', '10110001', '2', '101010010'],
    ['FFFFB9', 'CB9', '16', '141F'],
    ['1110', '1001', '2', '1'],
    ['55', '1', '10', '55'],
    ['AFE', 'AA', '16', '10']
]
test_suite_mod = [
    ['0', '10', '10', '0'],
    ['5', '10', '10', '5'],
    ['5', '-10', '10', '-5'],
    ['-5', '10', '10', '5'],
    ['15', '-8', '10', '-1'],
    ['555', '31', '10', '28'],
    ['F', '5', '16', '0'],
    ['1110', '11', '2', '10'],
    ['7561', '11', '8', '2'],
    ['9999999999999', '15', '10', '9'],
    ['15', '9999999999999', '10', '15'],
    ['55', '1', '10', '0'],
    ['55', '-1', '10', '0']
]

class CalculatorTest(unittest.TestCase):


    def test_add(self):
        for num1, num2, system, total in test_suite_add:
            self.assertEqual(calc_marat(num1, num2, system, '+'), (total, system))
            self.assertEqual(calc_svetozar(num1, num2, system, '+'), (total, system))
        logging.debug('Test_add: Passed')



    def test_sub(self):
        for num1, num2, system, total in test_suite_sub:
            self.assertEqual(calc_marat(num1, num2, system, '-'), (total, system))
            self.assertEqual(calc_svetozar(num1, num2, system, '-'), (total, system))
        logging.debug('Test_sub: Passed')


    def test_mul(self):
        for num1, num2, system, total in test_suite_mul:
            self.assertEqual(calc_marat(num1, num2, system, '*'), (total, system))
            self.assertEqual(calc_svetozar(num1, num2, system, '*'), (total, system))
        logging.debug('Test_mul: Passed')



    def test_floordiv(self):
        for num1, num2, system, total in test_suite_floordiv :
            self.assertEqual(calc_marat(num1, num2, system, '//'), (total, system))
            self.assertEqual(calc_svetozar(num1, num2, system, '//'), (total, system))
        logging.debug('Test_floordiv: Passed')

    def test_mod(self):
        for num1, num2, system, total in test_suite_mod:
            self.assertEqual(calc_svetozar(num1, num2, system, '%'), (total, system))
        logging.debug('Test_mod: Passed')



if __name__ == '__main__':
    unittest.main()
