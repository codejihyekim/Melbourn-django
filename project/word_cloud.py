import itertools

from konlpy.tag import Okt

from nltk.tokenize import word_tokenize
import nltk
import re
import pandas as pd
import numpy as np
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from icecream import ic

from context.domains import File, Reader

class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'
        self.okt = Okt()

    def h_preprocessing(self):
        df = pd.read_excel('./data/감성대화말뭉치(원시데이터)_Validation.xlsx', engine='openpyxl')
        df_happy = df.drop(
            ['번호', 'value', '연령', '성별', '상황키워드', '신체질환' ,'감정_소분류', '시스템응답1', '사람문장2', '시스템응답2', '사람문장3', '시스템응답3'],
            axis=1)
        df_happy = df_happy[df_happy['감정_대분류'] == '기쁨']
        df_happy = df_happy.drop(['감정_대분류'], axis=1)
        #print(df_happy)
        df_happy.rename(columns={'사람문장1': 'doc'}, inplace=True)
        #print(df_happy)
        df_happy = np.array(df_happy)
        #print(df_happy)
        df_happy = list(itertools.chain(*df_happy))
        #print(df)
        #df = "".join(map(str, df))
        happy_texts = ''
        for i in df_happy:
            happy_texts += i + ""
        #print(happy_texts)
        happy_texts = happy_texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ㄱ-힣]+')
        #print(tokenizer.sub(' ', happy_texts))
        return tokenizer.sub(' ', happy_texts)

    def s_preprocessing(self):
        df = pd.read_excel('./data/감성대화말뭉치(원시데이터)_Validation.xlsx', engine='openpyxl')
        df_sad = df.drop(
            ['번호', 'value', '연령', '성별', '상황키워드', '신체질환', '감정_소분류', '시스템응답1', '사람문장2', '시스템응답2', '사람문장3',
             '시스템응답3'],
            axis=1)
        df_sad = df_sad[df_sad['감정_대분류'] == '슬픔']
        df_sad = df_sad.drop(['감정_대분류'], axis=1)
        #print(df_sad)
        df_sad.rename(columns={'사람문장1': 'doc'}, inplace=True)
        df_sad = np.array(df_sad)
        #print(df_sad)
        df_sad = list(itertools.chain(*df_sad))
        #print(df_sad)
        sad_texts = ''
        for i in df_sad:
            sad_texts += i + ""
        sad_texts = sad_texts.replace('\n', ' ')
        #print(len(sad_texts))
        tokenizer = re.compile(r'[^ㄱ-힣]+')
        return tokenizer.sub(' ', sad_texts)

    def h_noun_embedding(self):
        noun_tokens = []
        tokens = word_tokenize(self.h_preprocessing())
        for i in tokens:
            pos = self.okt.pos(i)
            _ = [j[0] for j in pos if j[1] == 'Noun']
            if len(''.join(_)) > 1:
                noun_tokens.append(' '.join(_))
        #print(noun_tokens)
        return noun_tokens

    def s_noun_embedding(self):
        noun_tokens = []
        tokens = word_tokenize(self.s_preprocessing())
        for i in tokens:
            pos = self.okt.pos(i)
            _ = [j[0] for j in pos if j[1] == 'Noun']
            if len(''.join(_)) > 1:
                noun_tokens.append(' '.join(_))
        return noun_tokens

    def h_draw_wordcloud(self):
        _ = self.h_noun_embedding()
        freqtxt = pd.Series(dict(FreqDist(_))).sort_values(ascending=False)
        wcloud = WordCloud('../nlp/data/D2Coding.ttf', relative_scaling=0.2,
                           background_color='white').generate(" ".join(_))
        plt.figure(figsize=(12, 12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def s_draw_wordcloud(self):
        _ = self.s_noun_embedding()
        freqtxt = pd.Series(dict(FreqDist(_))).sort_values(ascending=False)
        wcloud = WordCloud('../nlp/data/D2Coding.ttf', relative_scaling=0.2,
                           background_color='white').generate(" ".join(_))
        plt.figure(figsize=(12, 12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    #Solution().s_preprocessing()
    #Solution().noun_embedding()
    Solution().h_draw_wordcloud()
    Solution().s_draw_wordcloud()