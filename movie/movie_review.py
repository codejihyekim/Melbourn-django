import matplotlib
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from icecream import ic
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib
import numpy as np
import math
import re
import jpype
from konlpy.tag import Okt
from context.domains import Reader, File
from collections import Counter

'''
예제 출처
https://prlabhotelshoe.tistory.com/21?category=1003351
'''
class Solution(Reader):

    def __init__(self):
        self.file = File()
        self.file.context = './data/'
        self.okt = Okt()

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. 텍스트 마이닝')
            print('2. preprocessing')
            print('3. visualization')
            print('4. draw_wordcloud')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.crawling()
                break
            if menu == '2':
                self.preprocessing()
                break
            if menu == '3':
                self.visualization()
                break
            if menu == '4':
                self.draw_wordcloud()
                break

    def crawling(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        f = open(path, 'w', encoding='UTF-8')
        for no in range(1, 501):
            url = 'https://movie.naver.com/movie/point/af/list.naver?&page=%d' % no
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')

            reviews = soup.select('tbody > tr > td.title')
            for rev in reviews:
                title = rev.select_one('a.movie').text.strip()
                score = rev.select_one('div.list_netizen_score > em').text.strip()
                comment = rev.select_one('br').next_sibling.strip()

                # -- 긍정/부정 리뷰 레이블 설정
                if int(score) >= 8:
                    label = 1  # -- 긍정 리뷰 (8~10점)
                elif int(score) <= 4:
                    label = 0  # -- 부정 리뷰 (0~4점)
                else:
                    label = 2

                f.write(f'{title}\t{score}\t{comment}\t{label}\n')
        f.close()

    def stereotype(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        data = pd.read_csv(path, delimiter='\t', names=['title', 'score', 'comment', 'label']) # 데이터프레임 타입으로 하기 위해서 스키마를 설정 파일내 구분자를 탭으로
        df_reviews = data.dropna()  # 코멘트 없는 리뷰 데이터 제거
        df_reviews = df_reviews.drop_duplicates(['comment'])  # 중복 리뷰 제거
        #print(df_reviews.info())
        #print(df_reviews.head(10))
        return df_reviews

    def preprocessing(self):
        df_reviews = self.stereotype()
        #print(df_reviews)
        #영화 리스트 확인
        movie_lst = df_reviews.title.unique()
        #print('전체 영화 편수 =', len(movie_lst))
        #print(movie_lst[:10])

        #각 영화 리뷰 수 계산
        cnt_movie = df_reviews.title.value_counts()
        #print(cnt_movie[:20])

        #각 영화 평점 분석
        info_movie = df_reviews.groupby('title')['score'].describe()
        info_movie.sort_values(by=['count'], axis=0, ascending=False)
        #print(info_movie)

        df_reviews.label.value_counts()
        #print(df_reviews)
        return df_reviews

    def visualization(self):
        df_reviews = self.preprocessing()
        self.ko_font()
        #상위 10개의 영화를 추출
        top10 = df_reviews.title.value_counts().sort_values(ascending=False)[:10]
        top10_title = top10.index.tolist()
        top10_reviews = df_reviews[df_reviews['title'].isin(top10_title)]
        print(top10_title)
        print(top10_reviews.info())

        #1. 평균 평점 계산
        movie_title = top10_reviews.title.unique().tolist() # 영화 제목 추출
        avg_score = {} # {제목: 평균} 저장
        for t in movie_title:
            avg = top10_reviews[top10_reviews['title'] == t]['score'].mean()
            avg_score[t] = avg

        plt.figure(figsize=(10, 5))
        plt.title('영화 평균 평점 (top 10: 리뷰 수)\n', fontsize=17)
        plt.xlabel('영화 제목')
        plt.ylabel('평균 평점')
        plt.xticks(rotation=20)

        for x, y in avg_score.items():
            color = np.array_str(np.where(y == max(avg_score.values()), 'orange', 'lightgrey'))
            plt.bar(x, y, color=color)
            plt.text(x, y, '%.2f' % y,
                     horizontalalignment='center',
                     verticalalignment='bottom')

        plt.show()

        #2. 평점 분포도 붉은 색 점선은 평균
        fig, axs = plt.subplots(5, 2, figsize=(15, 25))
        axs = axs.flatten()

        for title, avg, ax in zip(avg_score.keys(), avg_score.values(), axs):
            num_reviews = len(top10_reviews[top10_reviews['title'] == title])
            x = np.arange(num_reviews)
            y = top10_reviews[top10_reviews['title'] == title]['score']
            ax.set_title('\n%s (%d명)' % (title, num_reviews), fontsize=15)
            ax.set_ylim(0, 10.5, 2)
            ax.plot(x, y, 'o')
            ax.axhline(avg, color='red', linestyle='--')  # -- 평균 점선 나타내기

        plt.show()

        #3. 원형 차트 긍정리뷰 pink, 부정 리뷰 gold, 그외 whitesmoke
        fig, axs = plt.subplots(5, 2, figsize=(15, 25))
        axs = axs.flatten()
        colors = ['pink', 'gold', 'whitesmoke']
        labels = ['1 (8~10점)', '0 (1~4점)', '2 (5~7점)']

        for title, ax in zip(avg_score.keys(), axs):
            num_reviews = len(top10_reviews[top10_reviews['title'] == title])
            values = top10_reviews[top10_reviews['title'] == title]['label'].value_counts()
            ax.set_title('\n%s (%d명)' % (title, num_reviews), fontsize=15)
            ax.pie(values,
                   autopct='%1.1f%%',
                   colors=colors,
                   shadow=True,
                   startangle=90)
            ax.axis('equal')
        plt.show()

    def draw_wordcloud(self):
        df_reviews = self.preprocessing()
        okt = self.okt
        self.ko_font()
        #레이블링한 긍정 리뷰와 부정 리뷰를 활용하기 위한 변수 선언
        pos_reviews = df_reviews[df_reviews['label'] == 1]
        neg_reviews = df_reviews[df_reviews['label'] == 0]
        #긍정리뷰
        pos_reviews['comment'] = pos_reviews['comment'].apply(lambda x: re.sub(r'[^ㄱ-ㅣ가-힝+]', ' ', x))
        #부정리뷰
        neg_reviews['comment'] = neg_reviews['comment'].apply(lambda x: re.sub(r'[^ㄱ-ㅣ가-힝+]', ' ', x))

        pos_comment_nouns = []
        for cmt in pos_reviews['comment']:
            pos_comment_nouns.extend(okt.nouns(cmt))  # -- 명사만 추출
        pos_comment_nouns2 = []
        word = [w for w in pos_comment_nouns if len(w) > 1]
        pos_comment_nouns2.extend(word)
        pos_word_count = Counter(pos_comment_nouns2)
        #print(pos_word_count)

        #상위 20개의 빈도수를 가진 단어들을 나열
        max = 20
        pos_top_20 = {}
        for word, counts in pos_word_count.most_common(max):
            pos_top_20[word] = counts
           #print(f'{word} : {counts}')

        #추출한 상위 20개의 빈도수가 높은 단어들로 긍정 그래프를 생성
        plt.figure(figsize=(10, 5))
        plt.title('긍정 리뷰의 단어 상위 (%d개)' % max, fontsize=17)
        plt.ylabel('단어의 빈도수')
        plt.xticks(rotation=70)
        for key, value in pos_top_20.items():
            if key == '영화': continue
            plt.bar(key, value, color='lightgrey')
        plt.show()

        # 추출한 상위 20개의 빈도수가 높은 단어들로 부정 그래프를 생성
        neg_comment_nouns = []
        for cmt in neg_reviews['comment']:
            neg_comment_nouns.extend(okt.nouns(cmt))

        neg_comment_nouns2 = []
        word = [w for w in neg_comment_nouns if len(w) > 1]
        neg_comment_nouns2.extend(word)

        # -- 단어 빈도 계산
        neg_word_count = Counter(neg_comment_nouns2)

        # -- 빈도수가 많은 상위 20개 단어 추출
        neg_top_20 = {}
        for word, counts in neg_word_count.most_common(max):
            neg_top_20[word] = counts
            print(f'{word} : {counts}')


        # -- 그래프 작성
        plt.figure(figsize=(10, 5))
        plt.title('부정 리뷰의 단어 상위 (%d개)' % max, fontsize=17)
        plt.ylabel('단어의 빈도수')
        plt.xticks(rotation=70)
        for key, value in neg_top_20.items():
            if key == '영화': continue
            plt.bar(key, value, color='lightgrey')
        plt.show()

    def ko_font(self):
        font_path = "C:/Windows/Fonts/malgunsl.ttf"
        font = font_manager.FontProperties(fname=font_path).get_name()
        rc('font', family=font)
        # 그래프 마이너스 기호 표시 설정
        matplotlib.rcParams['axes.unicode_minus'] = False


if __name__ == '__main__':
    Solution().stereotype()
    Solution().hook()