import numpy as np
import matplotlib.pyplot as plt

class Study:

    def __init__(self):
        self.W = np.random.rand(1, 1)
        self.b = np.random.rand(1)
        self.x_data = np.array([1, 2, 3, 4, 5, 7, 8, 10, 12, 13, 14, 15, 18, 20, 25, 28, 30]).reshape(-1, 1)
        self.t_data = np.array([5, 7, 20, 31, 40, 44, 46, 49, 60, 62, 70, 80, 85, 91, 92, 97, 98]).reshape(-1, 1)

    def loss_func(self, x, t):
        y = np.dot(x, self.W) + self.b
        return np.mean(np.power((t-y), 2))

    def numerical_derivative(self, f, x):
        delta_x = 1e-4
        derivative_x = np.zeros_like(x)
        it = np.nditer(x, flags=['multi_index'])

        while not it.finished:
            idx = it.multi_index
            tmp = x[idx]
            x[idx] = tmp + delta_x
            fx_plus_delta = f(x)
            x[idx] = tmp - delta_x
            fx_minus_delta = f(x)
            derivative_x[idx] = (fx_plus_delta - fx_minus_delta) / (2 * delta_x)
            x[idx] = tmp
            it.iternext()
        return derivative_x

    def predict(self, x):
        return np.dot(x, self.W) + self.b

    def study(self):
        learning_rate = 0.0001
        xdata = self.x_data
        tdata = self.t_data
        f = lambda x: self.loss_func(xdata, tdata)
        for step in range(90000):
            self.W = self.W - learning_rate * self.numerical_derivative(f, self.W)  # W의 편미분
            self.b = self.b - learning_rate * self.numerical_derivative(f, self.b)  # b의 편미분

            if step % 9000 == 0:
                print('W : {}, b : {}, loss : {}'.format(self.W, self.b, self.loss_func(xdata, tdata)))
        print(self.predict(19))
        plt.scatter(xdata.ravel(), tdata.ravel())
        plt.plot(xdata.ravel(), np.dot(xdata, self.W) + self.b)  # 직선
        plt.show()

if __name__ == '__main__':
    Study().study()


