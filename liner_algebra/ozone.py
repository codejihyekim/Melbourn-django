import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

class Ozone:
    def __init__(self):
        df = pd.read_csv('../liner_algebra/data/ozone.csv')
        training_data = df[['temp', 'ozone']]
        print(training_data)
        training_data = training_data.dropna(how='any')
        self.x_data = training_data['temp'].values.reshape(-1, 1)
        self.t_data = training_data['ozone'].values.reshape(-1, 1)

    def solution(self):
        xdata = self.x_data
        tdata = self.t_data
        model = linear_model.LinearRegression()
        model.fit(xdata, tdata)
        print('W : {}, b : {}'.format(model.coef_, model.intercept_))
        predict_val = model.predict([[62]])
        print(predict_val)
        plt.scatter(xdata, tdata)
        plt.plot(xdata, np.dot(xdata, model.coef_) + model.intercept_, color='r')
        plt.show()

if __name__ == '__main__':
    Ozone().solution()
