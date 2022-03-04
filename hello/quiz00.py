import random

from hello import Member
from hello.domains import my100, myRandom, members


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        op = ['+', '-', '*', '/', '%']
        res = op[myRandom(0, len(op) - 1)]
        if res == '+':
            s = self.add(a, b)
        elif res == '-':
            s = self.sub(a, b)
        elif res == '*':
            s = self.mul(a, b)
        elif res == '/':
            s = self.div(a, b)
        elif res == '%':
            s = self.mod(a, b)

        print(f'{a} {res} {b} = {s}')
        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        this = Member()
        this.name = members()[myRandom(0,len(members())-1)]
        this.height = myRandom(1, 200)
        this.weight = myRandom(1, 200)
        res = this.weight / (this.height * this.height) * 10000
        if res > 30:
            s = f'고도 비만'
        elif res > 25:
            s = f'비만'
        elif res > 23:
            s = f'과체중'
        elif res > 18.5:
            s = f'정상'
        else:
            s = f'저체중'
        print(f'{this.name}님, {s} 입니다.')
        return None

    def quiz02dice(self):
        return myRandom(1, 6)

    def quiz03rps(self):
        c = myRandom(1, 3)
        p = input('가위', '바위', '보')
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '1~3 입력'
        print(res)

    def quiz04leap(self):
        year = myRandom(0, 3000)
        return '윤년' if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else '평년'

    def quiz05grade(self):
        name = members()[myRandom(0,23)]
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.avg(kor, eng, math)
        grade = self.grade(kor, eng, math)
        passChk = self.passChk(kor, eng, math)

        print(f'{name}님, 국어 점수 : {kor} \n '\
                  f'영어 점수 : {eng}\n 수학 점수: {math}\n'\
                  f'총합: {sum} 평균: {avg} 등급: {grade} 합격 여부: {passChk}')
        return None

    def sum(self, kor, eng, math):
        return kor + eng + math

    def avg(self, kor, eng, math):
        return self.sum(kor, eng, math) / 3

    def passChk(self, kor, eng, math):  # 60점 이상 이면 합격
        return '합격' if self.avg(kor, eng, math) >= 60 else '불합격'

    def grade(self, kor, eng, math):
        if (self.avg(kor, eng, math)) >= 90:
            return 'A등급'
        elif (self.avg(kor, eng, math)) >= 70:
            return 'B등급'
        elif (self.avg(kor, eng, math)) >= 60:
            return 'C등급'
        elif (self.avg(kor, eng, math)) >= 40:
            return 'D등급'
        else:
            return 'F등급'

    @staticmethod
    def quiz06memberChoice():
        print(members()[myRandom(0, 23)])

    @staticmethod
    def quiz07lotto():
        a = random.sample(range(1, 46), 6)
        a.sort()
        print(a)
        return None

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        total = 0
        money = myRandom(0, 100000)

        while 1:
            bankMenu = int(input('0.Exit 1.입금 2.출금 3.잔고 확인'))
            if bankMenu == 0:
                return
            elif bankMenu == 1:
                s = self.add(total, money)
                total += s
            elif bankMenu == 2:
                s = self.sub(total, money)
                total -= s
            elif bankMenu == 3:
                s = total
            else:
                s = '잘못된 번호 입니다.'
            print(s)

    def save(self, total, money):
        return total + money

    def pay(self, total, money):
        return total - money

    @staticmethod
    def quiz09gugudan():  # 책받침구구단
        for i in range(2, 10, 4):
            for j in range(1, 10):
                for k in range(i, i + 4):
                    print(f'{k} * {j} = {k * j}\t', end='')
                print('\n', end='')
            print('\n', end='')
            return None
