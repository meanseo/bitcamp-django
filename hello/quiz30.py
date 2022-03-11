import random
import string

import pandas as pd
from icecream import ic

from hello.domains import myRandom


class Quiz30:
    '''
                데이터프레임 문제 Q02
            ic| df:     A   B   C
                    1   1   2   3
                    2   4   5   6
                    3   7   8   9
                    4  10  11  12
    '''
    def quiz30_df_4_by_3(self) -> object:
        a = [[i for i in range(j * 3 + 1, j * 3 + 4)] for j in range(4)]
        df = pd.DataFrame(a, index=range(1, 5), columns=['A', 'B', 'C'])
        # 위 식을 리스트 결합 형태로 분해해서 조립하시오

        # ls1 = [i for i in range(1, 4)]
        # ls2 = [i for i in range(4, 7)]
        # ls3 = [i for i in range(7, 10)]
        # ls4 = [i for i in range(10, 13)]
        ic(df)
        return None

    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
    '''
    def quiz31(self) -> str:
        # a = myRandom(10,100)
        # ls1 = [myRandom(0,100) for i in range(3)]

        ls = [[myRandom(10, 100) for i in range(3)] for i in range(2)]
        df = pd.DataFrame(ls)
        ic(df)

        return None

    '''
        데이터프레임 문제 Q04.
        국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
            단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

            ic| df4:        국어  영어  수학  사회
                        lDZid  57  90  55  24
                        Rnvtg  12  66  43  11
                        ljfJt  80  33  89  10
                        ZJaje  31  28  37  34
                        OnhcI  15  28  89  19
                        claDN  69  41  66  74
                        LYawb  65  16  13  20
                        QDBCw  44  32   8  29
                        PZOTP  94  78  79  96
                        GOJKU  62  17  75  49
    '''
    def quiz32(self) -> str:
        score = [[myRandom(0, 101) for i in range(4)] for i in range(10)]
        # a = ''.join([random.choice(string.ascii_letters) for i in range(5)])
        member = [''.join([random.choice(string.ascii_letters) for i in range(5)]) for i in range(10)]
        dict = {i: j for i, j in zip(member, score)}
        df = pd.DataFrame.from_dict(dict, orient='index', columns=['국어', '영어', '수학', '사회'])
        ic(df)
        return None

    def quiz33(self) -> str: return None

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None