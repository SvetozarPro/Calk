import unittest
import calc_marat


class CalculatorBinTest(unittest.TestCase):

    def setUp(self):
        self.calc = calc_marat.Calculator('10011110101', '111010110', 2)

    def test_add(self):
        self.assertEqual(self.calc.__add__('10011110101', '111010110'), '11011001011')

    def test_mul(self):
        self.assertEqual(self.calc.__mul__('10011110101', '111010110'), '10010001100111001110')


    def test_sub(self):
        self.assertEqual(self.calc.__sub__('10011110101', '111010110'), '1100011111')


class CalculatorHexTest(unittest.TestCase):

    def setUp(self):
        self.calc2 = calc_marat.Calculator('A15', 'BC', 16)


    def test_add(self):
        self.assertEqual(self.calc2.__add__('A15', 'BC'), 'AD1')


    def test_mul(self):
        self.assertEqual(self.calc2.__mul__('A15', 'BC'), '7676C')


    def test_sub(self):
        self.assertEqual(self.calc2.__sub__('A15', 'BC'), '959')


class CalculatorDecTest(unittest.TestCase):

    def setUp(self):
        self.calc3 = calc_marat.Calculator('938193', '483212', 10 )


    def test_add(self):
        self.assertEqual(self.calc3.__add__('938193', '483212'), '1421405')


    def test_mul(self):
        self.assertEqual(self.calc3.__mul__('938193', '483212'), '453346115916')


    def test_sub(self):
        self.assertEqual(self.calc3.__sub__('938193', '483212'), '454981')


class CalculatorOctTest(unittest.TestCase):

    def setUp(self):
        self.calc4 = calc_marat.Calculator('64231', '32134', 8)


    def test_add(self):
        self.assertEqual(self.calc4.__add__('64231', '32134'), '116365')


    def test_mul(self):
        self.assertEqual(self.calc4.__mul__('64231', '32134'), '2531125374')


    def test_sub(self):
        self.assertEqual(self.calc4.__sub__('64231', '32134'), '32075')

if __name__ == '__main__':
    unittest.main()
