class NotationError(ArithmeticError):
    pass


revers_nums = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
nums = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
notations = {'0B':2,'0O':8,'0X':16}
revers_notations = {'2':'0b','8':'0o','10':'','16':'0x'}


def normalize(body):
    """
    Приведение числа к стандартной форме (без нулей в старших разрядах)
    """
    for i in range(len(body) - 1, 0, -1):
        if body[i] == '0':
            body.pop(i)
        else:
            break


def dict_to_str(body):
    """
    Перевод формы представления тела числа из словаря в строку, где значения имеют тип int
    """
    rez = ''
    for i in range(len(body)):
        rez += revers_nums[body[i]]
    return rez[::-1]


class Num:
    """
    У объектов класса есть следующие параметры:
    self.positive - положительность числа
    self.code - текстовое обозначение системы счисления из словаря notations, в случае десятичной СС равен ''
    self.notation - числовое обозначение системы счисления
    self.body - словарь, представляющий число с ключами - разрядами, и их значениями - текстовая запись цифры разряда
    self.length - длина циферной части числа
    self.value - строковое представление числа без системы счисления
    """
    def __init__(self, value):
        value = value.upper()

        if value[0] == '-':
            self.positive = False
            value = value[1:]
        else:
            self.positive = True
        self.value = value

        if value[:2] in notations:
            self.code = value[:2]
            value = value[2:]
            self.notation = notations[self.code]
        else:
            self.code = ''
            self.notation = 10

        self.body = dict((i, value[::-1][i]) for i in range(len(value)))
        normalize(self.body)
        self.length = len(self.body)
        list_keys = sorted(list(nums.keys()))
        for num in value:
            if num not in list_keys[:self.notation]:
                raise NotationError
        # Ноль всегда положителен
        if self.length == 1 and self.body[0] == '0':
            self.positive = True

    def __str__(self):
        rez = ''
        for i in sorted(list(self.body)):
            rez += self.body[i]
        return (not self.positive) * '-' + self.code.lower() + rez[::-1]

    def __add__(self, other):
        if self.notation == other.notation:
            # Если сложение можно представить в виде вычитания отрицательных или положительных чисел -
            # вызывается соответстующее вычитание
            if self.positive ^ other.positive:
                return Num.__sub__(Num(self.value*self.positive+other.value*other.positive),
                                   Num(self.value*other.positive+other.value*self.positive))
            else:
                rez_add = {}
                # Поразрядное сложение с вынесением переполнения разряда как +1 к более старшему разряду в результате
                for i in range(max(self.length, other.length)):
                    rez_add[i] = rez_add.get(i, 0) + nums[self.body.get(i, '0')] + nums[other.body.get(i, '0')]
                    rez_add[i+1] = rez_add[i] // self.notation
                    rez_add[i] %= self.notation
                normalize(rez_add)
                return Num((not self.positive) * '-' + self.code + dict_to_str(rez_add))

        else:
            raise NotationError()

    def __sub__(self, other):
        if self.notation == other.notation:
            # Если вычитание можно представить в виде сложения отрицательных или положительных чисел -
            # вызывается соответстующее сложение
            if self.positive ^ other.positive:
                return Num.__add__(Num(('-'*(not self.positive))+self.value),
                                   Num(('-'*(not self.positive))+other.value))
            else:
                # Нахождение наибольшего и наименьшего по модулю числа,
                # чтобы далее вычитание наименьшего происходило из наибольшего
                swap = True
                for i in range(max(self.length, other.length)-1, -1, -1):
                    if self.body.get(i, '0') > other.body.get(i, '0'):
                        swap = False
                        break
                    elif self.body.get(i, '0') < other.body.get(i, '0'):
                        break
                if swap:
                    bigger, smaller = other.body, self.body
                else:
                    bigger, smaller = self.body, other.body

                rez_sub = {}
                # Поразрядное вычитание с вынесением недостатка в разряде как занимание из следующего
                # Гарантируется, что в результате в высших разрядах не будет отрицательных чисел
                # и все нули в них будут удалены
                for i in range(len(bigger)):
                    rez_sub[i] = rez_sub.get(i, 0) + nums[bigger[i]] - nums[smaller.get(i, '0')]
                    rez_sub[i+1] = rez_sub[i] // self.notation
                    rez_sub[i] -= self.notation * rez_sub[i+1]
                return Num((not (swap ^ self.positive)) * '-' + self.code + dict_to_str(rez_sub))

        else:
            raise NotationError()

    def __mul__(self, other):
        if self.notation == other.notation:
            rez = Num(self.code + '0')
            # Поразрядное умножение первого числа на разряды второго с последующим их сложением
            # с учётом мощности разряда множителя
            for i in range(other.length):
                if other.body[i] == '0':
                    continue
                middle_rez = {}
                for j in range(self.length):
                    middle_rez[j] = middle_rez.get(j, 0) + nums[other.body[i]] * nums[self.body[j]]
                    middle_rez[j+1] = middle_rez[j] // self.notation
                    middle_rez[j] %= self.notation
                normalize(middle_rez)
                rez = rez + Num(self.code + dict_to_str(middle_rez) + '0' * i)
            return Num((self.positive ^ other.positive) * '-' + str(rez))

        else:
            raise NotationError()

    def __floordiv__(self, other):
        if other.length == 1 and other.body[0] == 0:
            raise ZeroDivisionError
        if self.notation == other.notation:

            rez = Num(self.code + '0')
            dividend = self.body.copy()
            # Поразрядное вычитание модуля делителя, начиная с высших разрядов
            for i in range(len(dividend)-1, -1, -1):
                subtrahend_value = ''
                for j in range(len(dividend)-1, i-1, -1):
                    subtrahend_value += dividend[j]
                subtrahend = Num(self.code + subtrahend_value)
                quotient_quantum = -1
                module_other = Num(str(other)[not other.positive:])
                while subtrahend.positive:
                    subtrahend = subtrahend - module_other
                    quotient_quantum += 1
                rez = rez + Num(self.code + revers_nums[quotient_quantum] + i * '0')
                subtrahend = subtrahend + module_other
                for j in range(i, len(dividend)):
                    dividend[j] = subtrahend.body.get(j-i, '0')
                normalize(dividend)

            # Проверка на остаток при отрицательном итоге
            if self.positive ^ other.positive and ((subtrahend.length == 1 and subtrahend.body[0] != '0')
                                                   or subtrahend.length > 1):
                rez = rez + Num(self.code + '1')
            return Num((self.positive ^ other.positive) * '-' + str(rez))

        else:
            raise NotationError()

    def __mod__(self, other):
        if other.length == 1 and other.body[0] == 0:
            raise ZeroDivisionError
        if self.notation == other.notation:

            dividend = self.body.copy()
            module_other = Num(str(other)[not other.positive:])
            # Поразрядное вычитание модуля делителя, начиная с высших разрядов
            for i in range(len(dividend) - 1, -1, -1):
                subtrahend_value = ''
                for j in range(len(dividend) - 1, i - 1, -1):
                    subtrahend_value += dividend[j]
                subtrahend = Num(self.code + subtrahend_value)
                while subtrahend.positive:
                    subtrahend = subtrahend - module_other
                subtrahend = subtrahend + module_other
                for j in range(i, len(dividend)):
                    dividend[j] = subtrahend.body.get(j - i, '0')
                normalize(dividend)

            # Проверка на остаток при отрицательном делителе
            if (not other.positive) and ((subtrahend.length == 1 and subtrahend.body[0] != '0')
                                         or subtrahend.length > 1):
                rez = module_other - subtrahend
            else:
                rez = subtrahend
            return Num((not other.positive) * '-' + str(rez))

        else:
            raise NotationError()


def calc_svetozar(value1, value2, notation, operation):
    """
    Функция изменения интерфейса калькулятора
    :param value1: первое число
    :param value2: второе число
    :param notation: система счисления в виде числа в строковом формате:'2', '8', '10', '16'
    :param operation: арифметический оператор в строковом формате: '+', '-', '*', '//', '%'
    :return: кортеж результата числа и его системы счисления в строковом формате
    """
    num1, num2 = Num(revers_notations[notation] + value1), Num(revers_notations[notation] + value2)
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '//':
        result = num1 // num2
    elif operation == '%':
        result = num1 % num2
    else:
        raise TypeError
    return str(result).replace(result.code.lower(), ''), str(result.notation)
