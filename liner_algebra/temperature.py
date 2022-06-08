import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from liner_algebra.study import Study


class Temperature:

    def __init__(self):
        df = pd.read_csv('../liner_algebra/data/ozone.csv')
        training_data = df[['temp', 'ozone']]
        training_data = training_data.dropna(how='any')
        self.x_data = training_data['temp'].values.reshape(-1, 1)
        self.t_data = training_data['ozone'].values.reshape(-1, 1)
        self.W = np.random.rand(1, 1)
        self.b = np.random.rand(1)

    def loss_func(self, x, t):
        y = np.dot(x, self.W) + self.b
        return np.mean(np.power((t - y), 2))

    def predict(self, x):
        return np.dot(x, self.W) + self.b

    def solution(self):
        xdata = self.x_data
        tdata = self.t_data
        learning_rate = 1e-5
        f = lambda x: self.loss_func(xdata, tdata)
        for step in range(90000):
            self.W -= learning_rate * Study.numerical_derivative(self, f, self.W)
            self.b -= learning_rate * Study.numerical_derivative(self, f, self.b)

            if step % 9000 == 0:
                print('W : {}, b : {}, loss : {}'.format(self.W, self.b, self.loss_func(xdata, tdata)))
        result = self.predict(62)
        print(result)
        plt.scatter(xdata, tdata)
        plt.plot(xdata, np.dot(xdata, self.W) + self.b, color='r')
        plt.show()

if __name__ == '__main__':
    Temperature().solution()