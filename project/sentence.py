import pandas as pd
import numpy as np
import math
import re
from konlpy.tag import Okt
from collections import Counter, defaultdict

from context.domains import Reader, File


class Solution(Reader):

    def __init__(self, k=0.5):
        self.file = File()
        self.file.context = './data/'
        self.okt = Okt()
        self.k = k

    def preprocessing(self):
        file = self.file
        df = pd.read_excel('./data/감성대화말뭉치(원시데이터)_Validation.xlsx', engine='openpyxl')
        df = df.drop(['번호', 'value', '연령', '성별', '상황키워드', '신체질환', '감정_소분류', '시스템응답1', '사람문장2', '시스템응답2','사람문장3','시스템응답3'], axis=1)
        df = df[df['감정_대분류'] == '기쁨']
        df.rename(columns={'감정_대분류': 'point', '사람문장1': 'doc'}, inplace=True)
        df['point'] = 0
        df = np.array(df)
        print(df)
        return df

    def count_words(self, training_set):
        counts = defaultdict(lambda : [0, 0])
        for point, doc in training_set:
            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][point] += 1
        return counts


    def isNumber(self, f):
        try:
            float(f)
            return True
        except ValueError:
            return False

    def word_probabilities(self, counts, total_class0, total_class1, k):
        return [(w, (class0 + k) / (total_class0 + 2 * k), (class1 + k) / (total_class1 + 2 * k)) for w, (class0, class1) in counts.items()]


    def class0_probabilities(self, word_probs, doc):
        docwords = doc.split()
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        for word, prob_if_class0, prob_if_class1 in word_probs:
            if word in docwords:
                log_prob_if_class0 += math.log(prob_if_class0)
                log_prob_if_class1 += math.log(prob_if_class1)
            else:
                log_prob_if_class0 += math.log(1.0 - prob_if_class0)
                log_prob_if_class1 += math.log(1.0 - prob_if_class1)
        prob_if_class0 = math.exp(log_prob_if_class0)
        prob_if_class1 = math.exp(log_prob_if_class1)
        return prob_if_class0 / (prob_if_class0 + prob_if_class1)

    def train(self):
        print('-------- 훈련시작 ---------')
        training_set = self.preprocessing()
        num_class0 = len(training_set)
        print(num_class0)





if __name__ == '__main__':
    Solution().preprocessing()
    Solution().train()