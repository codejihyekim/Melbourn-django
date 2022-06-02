import random
import string

import pandas as pd
from icecream import ic
import numpy as np
from context.models import Model
from hello.domains import myRandom, members


class Quiz30:
    '''
           데이터프레임 문제 Q02
       ic| df:     A   B   C
               1   1   2   3
               2   4   5   6
               3   7   8   9
               4  10  11  12
       '''
    def quiz30_df_4_by_3(self) -> str:
        '''
        l1 = [i for i in range(1, 4)]
        l2 = [i for i in range(4, 7)]
        l3 = [i for i in range(7, 10)]
        l4 = [i for i in range(10, 13)]
        d = {'1': range(1, 4),
             '2': range(4, 7),
             '3': range(7, 10),
             '4': range(10, 13)}
        '''
        ls1 = [[i for i in range(j*3+1, j*3+4)] for j in range(4)]
        df = pd.DataFrame(ls1, index=range(1, 5), columns=['A', 'B', 'C'])
        # 위 식을 리스트결합 형태로 분해해서 조립하시오
        ic(df)
        return None

    '''
            데이터프레임 문제 Q03.
            두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
            ic| df:     0   1   2
                    0  97  57  52
                    1  56  83  80
    '''
    def quiz31_rand_2_by_3(self) -> str:
        '''
        넘파이 사용한 예제
        df = pd.DataFrame(np.random.randint(10, 100, size=(2,3))
        '''
        ls = [[myRandom(10, 99) for i in range(3)] for i in range(2)]
        df = pd.DataFrame(ls, index=range(0, 2), columns=range(0, 3))
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
    @staticmethod
    def id(chr_size) -> str:
        return ''.join([random.choice(string.ascii_lowercase) for i in range(chr_size)])
    def quiz32_df_grade(self) -> str:
        col = ['국어', '영어', '수학', '사회']
        scores = [[myRandom(0, 100) for i in range(4)]for j in range(10)]
        scores = np.random.randint(0, 100, size=(10, 4))
        names = [self.id(chr_size=5) for i in range(10)]
        df1 = pd.DataFrame(scores, index=names, columns=col)
        ic(df1)
        ic('*'*30)
        dic = dict(zip(names, scores))
        dic = {i: j for i, j in zip(names, scores)}
        df2 = pd.DataFrame.from_dict(dic, orient='index', columns=col)
        ic(df2)
        return None

    def quiz33_df_loc(self) -> str:

        df2 = self.createDf(keys=['a', 'b', 'c', 'd'],
                           vals=np.random.randint(0, 100, 4),
                           len=3)
        #ic(df2)
        '''
        ic| df2:    a   b   c   d
                0  20  41  70  97
                1  20  41  70  97
                2  20  41  70  97
        '''

        '''
      자바  파이썬  자바스크립트  SQL
홍정명  61   93      24   16
노홍주  47   38      62   99
전종현  93   89      12   49
정경준  81   64       0   25
양정오  83   62      82   34
권혜민  67   82      47   35
서성민  82   50      67   89
조현국  56   23      38   38
김한슬  88   11      61   64
김진영  28   41      64   87
심민혜   0   37      99   52
권솔이  95   58      67   87
김지혜  32   40      45   97
하진희   8    0      90   34
최은아  50    6      91   62
최민서  85   48      50   12
한성수  92   15      35   17
김윤섭  63   55      26   95
김승현   7   18       9   12
강 민  24   40       5   47
최건일  55   46      85   27
유재혁  64    5      96   95
김아름  37    6      90   82
장원종  40   16      31   44
        '''

        subjects = ['자바', '파이썬', '자바스크립트', 'SQL']
        students = members()
        scores = np.random.randint(0, 100, (24, 4))
        students_scores = {students: scores for students, scores in zip(students, scores)}
        students_scores_df = pd.DataFrame.from_dict(students_scores, orient='index', columns=subjects)
        ic(students_scores_df)
        # students_scores_df.to_csv('./save/mygrade.csv', sep=',', na_rep='NaN')

        # grade.csv
        model = Model()
        grade_df = model.new_model('grade.csv')
        #ic(grade_df)

        print('파이썬의 점수만 출력하시오')
        python_scores = grade_df.loc[:, '파이썬']
        ic(type(python_scores))
        ic(python_scores)

        print('q2. 조현국의 점수만 출력하시오')
        cho_scores = grade_df.loc['조현국']
        ic(type(cho_scores))
        ic(cho_scores)

        print('q3 조현국의 과목별 점수를 출력하시오')
        cho_subjects_cores = grade_df.loc[['조현국']]
        ic(type(cho_subjects_cores))
        ic(cho_subjects_cores)
        return None

    @staticmethod
    def createDf(keys, vals, len):
        return pd.DataFrame([dict(zip(keys, vals)) for _ in range(len)])

    def quiz34_df_iloc(self) -> str:
        '''
        mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
        df = pd.DataFrame(mydict)
        df
             a     b     c     d
        0     1     2     3     4
        1   100   200   300   400
        2  1000  2000  3000  4000
        '''

        # ic(df2.iloc[0])
        '''
        ic| df2.iloc[0]: a    40
                 b    17
                 c    27
                 d    69
                 Name: 0, dtype: int32
        '''
        # ic(df2.iloc[[0]])
        '''
        ic| df2.iloc[[0]]:     a   b   c   d
                            0  50  59  10  74
        '''
        # ic(df2.iloc[[0, 1]])
        '''
        ic| df2.iloc[[0, 1]]:       a   b   c   d
                                0  29  11  13  21
                                1  29  11  13  21
        '''
        # ic(df2.iloc[:3])
        '''
        ic| df2.iloc[:3]:      a   b   c   d
                            0  66  95  81  44
                            1  66  95  81  44
                            2  66  95  81  44
        '''
        # ic(df2.iloc[[True, False, True]])
        '''
        ic| df2.iloc[[True, False, True]]:     a  b   c   d
                                            0  77  5  34  65
                                            2  77  5  34  65

        '''
        # ic(df2.iloc[lambda x: x.index % 2 == 0])
        '''
        ic| df2.iloc[lambda x: x.index % 2 == 0]:      a   b   c  d
                                                    0  80  74  44  6
                                                    2  80  74  44  6

        '''
        # ic(df2.iloc[0, 1])
        '''
        ic| df2.iloc[0, 1]: 3
        '''
        # ic(df2.iloc[[0, 2], [1, 3]])
        '''
        ic| df2.iloc[[0, 2], [1, 3]]:      b   d
                                        0  44  99
                                        2  44  99
        '''
        # ic(df2.iloc[1:3, 0:3])
        '''
        ic| df2.iloc[1:3, 0:3]:     a   b   c
                                1  83  90  78
                                2  83  90  78
        '''
        # ic(df2.iloc[:, [True, False, True, False]])
        '''
        ic| df2.iloc[:, [True, False, True, False]]:        a   c
                                                        0  49  29
                                                        1  49  29
                                                        2  49  29

        '''
        # ic(df2.iloc[:, lambda df: [0, 2]])
        '''
        ic| df2.iloc[:, lambda df: [0, 2]]:     a   c
                                            0  12  19
                                            1  12  19
                                            2  12  19
        '''
        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None