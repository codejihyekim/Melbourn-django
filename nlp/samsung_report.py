from konlpy.tag import Okt

from nltk.tokenize import word_tokenize
import nltk
import re
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from icecream import ic

from context.domains import File, Reader

'''
  문장 형태의 문자 데이터를 전처리할 때 많이 사용되는 방법이다. 
  말뭉치(코퍼스 corpus)를 어떤 토큰의 단위로 분할하냐에 따라 
  단어 집합의 크기, 단어 집합이 표현하는 토크의 형태가 다르게 나타나며 

  이는 모델의 성능을 좌지우지하기도 한다. 
  이때 텍스트를 토큰의 단위로 분할하는 작업을 토큰화라고 한다. 
  토큰의 단위는 보통 의미를 가지는 최소 의미 단위로 선정되며, 
  토큰의 단위를 단어로 잡으면 Word Tokenization이라고 하고, 
  문장으로 잡으면 Sentence Tokeniazation이라고 한다. 

  영어는 주로 띄어쓰기 기준으로 나누고, 
  한글은 단어 안의 형태소를 최소 의미 단위로 인식해 적용한다.
  형태소(形態素, 영어: morpheme)는 언어학에서 의미가 있는 가장 작은 말의 단위이다.
  말뭉치는 언어학에서 주로 구조를 이루고 있는 텍스트 집합이다.
  
  1. Preprocessing
  2. Tokenization
  3. Token Embedding
  4. Document Embedding
  '''

class Solution(Reader):

    def __init__(self):
        self.okt = Okt()
        self.file = File()
        self.file.context = './data/'

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. kr-Report_2018.txt 파일을 읽는다.')
            print('2. Tokenization')
            print('3. Token Embedding')
            print('4. Document Embedding')
            print('5. 2018년 삼성사업계획서를 분석해서 워드클라우드를 작성하시오')
            print('6. ')
            print('9. nltk 다운로드')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.preprocessing()
                break
            if menu == '2':
                self.tokenization()
                break
            if menu == '3':
                self.token_embedding()
                break
            if menu == '4':
                self.document_embedding()
                break
            if menu == '5':
                self.draw_wordcloud()
                break
            if menu == '6':
                self.read_stopword()
                break
            if menu == '7':
                self.remove_stopword()
                break
            if menu == '9':
                Solution.download()


    @staticmethod
    def download():
        nltk.download('punkt')

    def preprocessing(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        f1 = self.file
        f1.fname = 'kr-Report_2018.txt'
        file = self.new_file(f1)
        with open(file, 'r', encoding='utf-8') as f:
            texts = f.read()
        texts = texts.replace('\n', ' ') # 반드시 공백을 주어야 띄어쓰기가 가능하다
        tokenizer = re.compile(r'[^ㄱ-힣]+') # 한글이 아닌 것들 제거
        return tokenizer.sub(' ', texts)

    def tokenization(self):
        noun_tokens = []
        # 토큰이라는 것은 문장을 기준을 두고 쪼개는 것
        tokens = word_tokenize(self.preprocessing()) #여기서는 단어를 기준으로 쪼갠다.
        #ic(tokens[:100])
        for i in tokens:
            pos = self.okt.pos(i)
            _ = [j[0] for j in pos if j[1] == 'Noun']
            if len(''.join(_)) > 1:
                noun_tokens.append(' '.join(_))
        texts = ' '.join(noun_tokens)
        #ic(texts[:100])
        return texts

    def read_stopword(self):
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        file = self.file
        file.fname = 'stopwords.txt'
        path = self.new_file(file)
        with open(path, 'r', encoding='utf-8') as f:
            texts = f.read()
        #ic(texts)
        return texts

    def remove_stopword(self):
        tokens = self.tokenization()
        stopwords = self.read_stopword()
        texts = [i for i in tokens.split() if not i in stopwords.split()]
        ic(texts)

    def token_embedding(self):
        pass

    def document_embedding(self):
        pass

    def draw_wordcloud(self):
        pass

if __name__ == '__main__':
    Solution().hook()