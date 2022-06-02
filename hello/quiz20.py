import random
import string
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from hello.domains import my100, myRandom, members
from hello.quiz00 import Quiz00

class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])
        list2 = ['math', 'english']
        print(list2[0])
        print(list2[0][1])
        list3 = [1, '2', [1, 2, 3]]
        print(list3)
        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2*list4)
        list4.append(list5)
        print(list4)
        list4[-2:] = []
        print(list4)
        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print(c[0][1])
        c[0][1] = 10
        print(c)
        a =range(10)
        print(a)
        print(sum(a))
        b = [2, 10, 0, -2]
        print(sorted(b))
        b.index(0)
        len(b)
        print(b.index(0), len(b))


    def quiz21tuple(self) -> str:
        a = (1, 2)
        print(a, type(a))
        a = (1, 2)
        b = (0,(1, 4))
        print(a + b)


    def quiz22dict(self) -> str:
        a = {"class":['deep learning', 'machine learning'], "num_students":[40, 20]}
        print(a)
        print(type(a))
        print(a["class"])
        a['grade'] = ['A', 'B', 'C']
        print(a)
        print(a.keys())
        print(list(a.keys()))
        print(a.values())
        print(a.items())
        print(a.get('class'))
        print("class" in a)



    def quiz23listcom(self) -> str:
        print('--------- legacy ---------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)

        print('--------- comprehension ---------')
        a2 = [i for i in range(5)]
        print(a2)


    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml') # html.parser vs lxml
        '''
        3개의 파라미터를 준 버전 
        self.find(soup, 'p', 'class', 'artist')
        print('*'*100)
        self.find(soup, 'p', 'class', 'title')
        
        artist와 title를 합친 버전
        for i, j in enumerate(['artist', 'title']):
            print('\n\n\n'.join(i for i in [i for i in self.find(soup, j)]))
            print('*'*100)
        '''

        ls1 = self.find(soup, 'title')
        ls2 = self.find(soup, 'artist')
        dt = {i: j for i, j in zip(ls1, ls2)}
        l = [i + j for i, j in zip(ls1, ls2)]
        l2 = dict(zip(ls1, ls2))
        d1 = dict(zip(ls1, ls2))
        print(d1)
        return d1
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        # self.dict3(ls1, ls2)

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    # 두개를 연달아 출력하는 range() 활용 리팩토링
    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    # class 각각 출력하는 리팩토링
    @staticmethod
    def find(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in ls]
        # print('\n'.join(i.get_text().strip() for i in ag))

    # print_music_list 메소드
    def print_music_list(self, soup):
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))
        # print(soup.prettify())
        # print(type(artists)
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i for i in titles]
        print('\n'.join(i.get_text().strip() for i in titles))

    # find_rank 메소드
    def find_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.find(soup, j)):
                print(f'{i}위 : {j}')
            print('#' * 100)

    @staticmethod
    def quiz25dictcom() -> str:
        m = Quiz00()
        s = set([m.quiz06memberChoice() for i in range(5)])
        while len(s) < 5:
            s.add(m.quiz06memberChoice())
        students = list(s)
        scores = [myRandom(1, 100) for i in range(5)]
        grades = {i: j for i, j in zip(students, scores)}
        print(grades)
        return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> {}:
        headers = {'User-Agent': 'Mozilla/5.0 '}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        ls1 = self.find_music(soup, 'ellipsis rank01')
        ls2 = self.find_music(soup, 'ellipsis rank02')
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict


    @staticmethod
    def find_music(soup, a) -> []:
        ls = soup.find_all('div', {'class': a})
        return [i.get_text() for i in ls]


    def quiz28dataframe(self) -> None:
        # dict = self.quiz24zip()
        #df = pd.DataFrame.from_dict(dict, orient='index')
        #print(df)
        #df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

        dict1 = self.quiz27melon()
        df = pd.DataFrame.from_dict(dict1, orient='index')
        print(df)
        df.to_csv('./save/melon.csv', sep=',', na_rep='NaN')

    ''' 
    다음 결과 출력
        a   b   c
    1   1   3   5
    2   2   4   6   
    '''
    def quiz29_pandas_01(self) -> object:
        d1 = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        df1 = pd.DataFrame(d1, index=[1, 2])
        '''
        df1 출력결과
           a  b  c
        1  1  3  5
        2  2  4  6
        '''
        d2 = {'1': [1, 3, 5], '2': [2, 4, 6]}
        df2 = pd.DataFrame(d2)
        '''
        df2 출력결과
           1  2
        0  1  2
        1  3  4
        2  5  6
        '''
        di3 = {'1': [1, 3, 5], '2': [2, 4, 6]}
        df3 = pd.DataFrame.from_dict(di3, orient='index')
        '''
        df3 출력결과
           0  1  2
        1  1  3  5
        2  2  4  6
        '''
        di4 = {'1': [1, 3, 5], '2': [2, 4, 6]}
        df4 = pd.DataFrame.from_dict(di4, orient='index', columns=['A', 'B', 'C'])
        '''
        df4 출력결과
           A  B  C
        1  1  3  5
        2  2  4  6
        '''

        c = [chr(i) for i in range(97, 100)]  # ['a','b','c']
        evens = [] # 짝수 리스트
        odds = [] # 홀수 리스트
        [evens.append(i) if i % 2 == 0 else odds.append(i) for i in range(1, 7)]
        d5 = ['1', '2']
        d6 = [evens, odds]
        d7 = {i: j for i, j in zip(d5, d6)}
        df5 = pd.DataFrame.from_dict(d7, orient='index', columns=c)
        '''
        df5 출력결과
           a  b  c
        1  2  4  6
        2  1  3  5
        '''
        print(df5)

        return None
