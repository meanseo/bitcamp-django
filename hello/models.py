import random

def main():
    while 1:
        menu = input('0.EXIT 1.계산기(+, -, *, /) 2.BMI 3.성적표 4.자동 성적표 5.주사위 6.원하는 범위에서 랜덤 뽑기 7.이름 뽑기 8.가위바위보')
        if menu == '0':
            break
        elif menu == '1': # 계산기
            calc = Quiz01Calculator(int(input('첫번째 수')), input('연산 기호'), int(input('두번째 수')))
            print(f'{calc.num1} {calc.op} {calc.num2} = {calc.calc()}')

        elif menu == '2': # BMI
            bmi = Quiz02Bmi(input('이름 입력'), float(input('키 입력')), float(input('몸무게 입력')))
            print(f'{bmi.name} 님, 결과: {bmi.bmi()}')

        elif menu == '3': # 성적표
            q4 = Quiz03Grade(input('이름 입력'), int(input('국어 점수')), int(input('영어 점수')), int(input('수학 점수')))
            print(q4.getGrade())

        elif menu == '4':
            for i in ['국어', '영어', '수학']:
                print(i)
            grade = Quiz04GradeAuto(input('이름 입력'), int(input('국어 점수')), int(input('영어 점수')), int(input('수학 점수')))

        elif menu == '5':
            print(f'결과: {Quiz05dice.getDice()}')

        elif menu == '6':
            q6 = None

        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(f'결과: {q7.chooseMember()}')

        elif menu == '8':
            q8 = Quiz08Rps(1) # 가위 1 바위 2 보 3
            print(q8.game())

class Quiz01Calculator(object):

    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        if self.op == '+':
            s = self.add()
        elif self.op == '-':
            s = self.sub()
        elif self.op == '*':
            s = self.mul()
        elif self.op == '/':
            s = self.div()
        return s

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

class Quiz02Bmi(object):

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        bmi = self.weight / self.height * self.height * 10000
        if bmi > 30:
            res = '고도 비만 입니다.'
        elif bmi > 25:
            res = '경도 비만 입니다.'
        elif bmi > 23:
            res = '과체중 입니다.'
        elif bmi > 18.5:
            res = '정상 체중 입니다.'
        else:
            res = '저체중 입니다.'
        return res

class Quiz03Grade(object):

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def getGrade(self):
        return f'이름 : {self.name} \n 국어 점수 : {self.kor} \n '\
                  f'영어 점수 : {self.eng}\n 수학 점수: {self.math}\n'\
                  f'총합: {self.total()} 평균: {self.avg()} 합격 여부: {self.chkPass()}'

    def total(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def chkPass(self):
        return '합격' if self.avg() >= 60 else '불합격'

class Quiz04GradeAuto(object):

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def getGrade(self):
        pass

    def chkPass(self):
        pass

def myRandom(start, end):
    return random.randint(start, end)

class Quiz05dice(object):
    @staticmethod
    def getDice():
            return myRandom(1, 6)

class Quiz07RandomChoice(object):
    def __init__(self):
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        '권혜민', '서성민', '조현국', '김한슬', '김진영',
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        '강 민', '최건일', '유재혁', '김아름', '장원종']

    def chooseMember(self):
        ran = myRandom(0, len(self.members)-1)
        return self.members[ran]
        # res = random.choice(self.members)

class Quiz08Rps(object):
    def __init__(self, user):
        self.user = user
        self.com = myRandom(1, 3)


    def game(self):
        u = self.user
        c = self.com
        # 1 가위 2 바위 3 보
        rps = ['가위', '바위', '보']
        if u == 1:
            if c == 1:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[1]}, 결과: 패배'
            elif c == 3:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[2]}, 결과: 승리'
        if u == 2:
            if c == 1:
                res = '승리'
            elif c == 2:
                res = '무승부'
            elif c == 3:
                res = '패배'
        if u == 3:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '승리'
            elif c == 3:
                res = '무승부'
        else:
            res = '잘못된 입력값 입니다.'

        return res

class Quiz09GetPrime(object):
    def __init__(self):
        pass

class Quiz10LeapYear(object):
    def __init__(self):
        pass

class Quiz11NumberGolf(object):
    def __init__(self):
        pass

class Quiz12Lotto(object):
    def __init__(self):
        pass

class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass

class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass

if __name__ == '__main__':
    main()