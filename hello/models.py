class Calculator(object):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

if __name__ == '__main__':
    while 1:
        menu = int(input('0.EXIT 1.계산기(+, -, *, /)'))
        if menu == 0:
            break
        else:
            while 1:
                menu = int(input('0.EXIT 1.더하기 2.빼기 3.곱하기 4.나누기'))
                if menu == 0:
                    break
                if menu < 5:
                    num1 = int(input('첫번째 수'))
                    num2 = int(input('두번째 수'))
                    calc = Calculator(num1, num2)
                    print('*' * 30)
                    if menu == 1:
                        print(f'{calc.num1} + {calc.num2} = {calc.add()}')
                    elif menu == 2:
                        print(f'{calc.num1} - {calc.num2} = {calc.sub()}')
                    elif menu == 3:
                        print(f'{calc.num1} * {calc.num2} = {calc.mul()}')
                    elif menu == 4:
                        print(f'{calc.num1} / {calc.num2} = {calc.div()}')








