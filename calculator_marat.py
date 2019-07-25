numbers = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6':'6', '7': '7', '8': '8', '9': '9', 'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15', '-': '-'}


rev_numbers = { '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F', '-': '-'}



class Calculator:

    """Конструктор принимает 3 аргумента, числа a и b и систему счисления(2, 8, 10, 16)"""

    def __init__(self, num1, num2, system):
        self.result = []
        self.shift = 0  # сдвиг
        self.system = int(system)  # CC


    def __add__(self, l1, l2):
        self.result = []
        max_len = max(len(l1), len(l2))
        l1, l2 = l1.rjust(max_len, '0'), l2.rjust(max_len, '0')
        if self.system == 16:
            l1 = [numbers[value] for value in l1 if value in numbers.keys()]  # генераторы для обработки шестнадцатеричных чисел
            l2 = [numbers[value] for value in l2 if value in numbers.keys()]
        for i in range(max_len-1, -1, -1):
            r = int(l1[i]) + int(l2[i]) + self.shift
            self.shift = r // self.system
            r = r % self.system
            self.result.append(str(r))

        if self.shift > 0:
            self.result.append(str(self.shift))

        r = [rev_numbers[value] for value in self.result if value in rev_numbers.keys()] # Обратное преобразование для шестнадцатеричных чисел


        self.shift = 0

        r = ''.join(r)[::-1]

        if all([i=='0' for i in r]):
            return '0'
        elif r.startswith('0'):
            return r.lstrip('0')
        else:
            return r



    def __sub__(self, l1, l2):
        self.result = []
        char = ''
        if l1 == '0' and l2 != '0':
            return '-' + l2
        if len(l1) < len(l2):
            l1, l2 = l2, l1
            char = '-'
        max_len = max(len(l1), len(l2))
        l1, l2 = l1.rjust(max_len, '0'), l2.rjust(max_len, '0')
        if self.system == 16:
            l1 = [numbers[value] for value in l1 if value in numbers.keys()]
            l2 = [numbers[value] for value in l2 if value in numbers.keys()]
        for i in range(max_len-1, -1, -1):
            r = int(l1[i]) - int(l2[i]) - self.shift
            if r >= 0:
                self.result.append(str(r))
                self.shift = 0
            else:
                r += self.system
                self.shift = 1
                self.result.append(str(r))

        if char == '-':
            self.result.append(char)

        r = self.result

        if self.system == 16:
            r = [rev_numbers[value] for value in self.result if value in rev_numbers.keys()]

        self.result = []

        r = ''.join(r)[::-1]
        if all([i=='0' for i in r]):
            return '0'
        elif r.startswith('0'):
            return r.lstrip('0')
        else:
            return r



    def __mul__(self, l1, l2):
        self.result = []
        self.zero = -1
        temp = []
        mul = ''
        if self.system == 16:
            l1 = [numbers[value] for value in l1 if value in numbers.keys()]
            l2 = [numbers[value] for value in l2 if value in numbers.keys()]
        for i in range(len(l2)-1, -1, -1):
            self.zero += 1
            for j in range(len(l1)-1,-1,-1):
                result = int(l2[i]) * int(l1[j]) + self.shift
                self.shift = 0
                while result >= self.system:
                    result -= self.system
                    self.shift += 1
                temp.append(str(result))
            if self.shift > 0:
                temp.append(str(self.shift))
            temp = temp[::-1]
            if self.system == 16:
                temp = [rev_numbers[value] for value in temp if value in rev_numbers.keys()]
            temp2 = ''.join(temp) + '0' * self.zero
            self.shift = 0
            mul = self.__add__(temp2, mul)
            temp = []

        return mul

    def __floordiv__(self, num, num2):
        if len(num) < len(num2):
            return '0'
        result = ''
        temp = ''
        max_len = max(len(num), len(num2))
        for i in range(max_len):
            temp += num[i]
            temp2 = int(temp, self.system) // int(num2, self.system)
            while temp2 > self.system:
                temp2 %= self.system
            if self.system == 16:
                temp2 = str(temp2)
                temp2 = rev_numbers.get(temp2, '0')
            result += str(temp2)
            if int(temp, self.system) >= int(num2, self.system):
                temp = self.__sub__(temp, num2)


        return result.lstrip('0')





def calc_marat(num1, num2, system, operation):
    result = None
    calc = Calculator(num1, num2, system)
    if operation == '+':
        result = calc.__add__(num1,num2)
    elif operation == '-':
        result = calc.__sub__(num1,num2)
    elif operation == '*':
        result = calc.__mul__(num1,num2)
    elif operation == '//':
        result = calc.__floordiv__(num1,num2)

    return result, str(system)
