from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz04GradeAuto, Quiz05dice, Quiz07RandomChoice, \
    Quiz08Rps, Quiz09GetPrime, Quiz10LeapYear, Quiz11NumberGolf, Quiz14Gugudan, Quiz12Lotto, Quiz13Bank
from hello.quiz30 import Quiz30

if __name__ == '__main__':

    while 1:
        menu = input('0.EXIT 1.계산기(+, -, *, /) 2.BMI 3.성적표 4.자동 성적표 5.주사위 6.원하는 범위에서 랜덤 뽑기 7.이름 뽑기 8.가위바위보')
        if menu == '0':
            break
        elif menu == '1': # 계산기
            calc = Quiz01Calculator(int(input('첫번째 수')), input('연산 기호'), int(input('두번째 수')))
            print(f'{calc.num1} {calc.op} {calc.num2} = {calc.calc()}')

        elif menu == '2': # BMI
            member = Member()
            q2 = Quiz02Bmi()
            member.name = input('이름: ')
            member.height = float(input('키: '))
            member.weight = float(input('몸무게: '))
            res = q2.bmi(member)
            print(f'{member.name} 님, 결과: {res}')

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

            q8 = Quiz08Rps(int(input('1.가위 2.바위 3.보'))) # 가위 1 바위 2 보 3
            print(q8.game())

        elif menu == '9':
            q9 = Quiz09GetPrime() # 가위 1 바위 2 보 3
            q9.getPrime()

        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('year: '))) # 가위 1 바위 2 보 3
            print(f'{q10.year}년은 {q10.getLeapYear()}')

        elif menu == '11':
            q11 = Quiz11NumberGolf()
            print(q11.numGame())

        elif menu == '12':
            q12 = Quiz12Lotto
            print(f'{q12.lotto()}')

        elif menu == '13':
            q13 = Quiz13Bank(input('이름: '))
            q13.bank()

        elif menu == '14':
            q14 = Quiz14Gugudan()
            print(q14.gugudan())

        elif menu == '30':
            q30 = Quiz30()
            q30.quiz30List()
            q30.quiz30tuple()
            q30.quiz30dict()
