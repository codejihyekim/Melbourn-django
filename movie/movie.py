import re
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

from konlpy.tag import Mecab

class Solution:
    def __init__(self):
        pass

    def preprocessing(self):
        train_file = urllib.request.urlopen("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt")
        test_file = urllib.request.urlopen("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt")
        train_data = pd.read_table(train_file)
        test_data = pd.read_table(test_file)
        #print(train_data[:10])

        #print(train_data['document'].nunique()) #중복확인
        #print(train_data['label'].nunique()) #중복확인
        train_data.drop_duplicates(subset=['document'], inplace=True) # document의 중복을 제거
        #print(train_data.isnull().sum()) # null의 개수를 출력
        train_data = train_data.dropna(how='any') # null값을 제거

        train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅣ가-힣 ]", "") #한글 아닌 것은 제거
        #print(train_data[:10])

        train_data['document'].replace('', np.nan, inplace=True) # 전처리
        #print(len(train_data))
        #print(train_data.isnull().sum())

        train_data = train_data.dropna(how='any') # 전처리 후 생기는 null값 제거
        #print(len(train_data))

        #test_data 전처리
        test_data.drop_duplicates(subset=['document'], inplace=True)
        test_data['document'] = test_data['document'].str.replace("[^ㄱ-ㅣ가-힣 ]", "")
        test_data['document'].replace('', np.nan, inplace=True)
        test_data = test_data.dropna(how='any')

        stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', ' 과', '도', '를', '으로', '자', '에', '와', '한', '하다']
        mecab = Mecab()
        X_train = []
        for sentence in train_data['document']:
            X_train.append([word for word in mecab.morphs(sentence) if not word in stopwords]) # 토큰작업와 불용어 처리
        print(X_train[:1])



if __name__ == '__main__':
    s = Solution()
    s.preprocessing()