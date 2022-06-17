import tensorflow as tf

class Solution:
    def __init__(self):
        self.mnist = tf.keras.datasets.mnist
        self.x_test = None
        self.x_train = None
        self.model = None

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. 데이터 로드')
            print('2. 모델생성')
            print('3. 모델을 훈련하고 평가')
            print('4. 손글씨 테스트')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.dataload()
            if menu == '2':
                self.create_model()
            if menu == '3':
                self.training_evaluaion_model()
            if menu == '3':
                self.test()

    def dataload(self):
        mnist = self.mnist
        #x는 독립변수, y는 종속변수
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        self.x_train, self.x_test = x_train / 255.0, x_test / 255.0 # 255 픽셀로 생성

    def create_model(self):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)), #input 레이어 첫번째
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation='softmax') # output 레이어 마지막
        ])
        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',  #sparse는 dense의 반대말로 손실을 많이 없게
                      metrics=['accuracy']) #매트릭스 정확도

    def training_evaluaion_model(self): # 훈련과 평가
        self.model.fit(self.x_train, self.y_train, epochs=5) # fit은 내부적으로 룹을 돌리고 있다. 정확도를 높이는 과정
        self.model.evaluate(self.x_test, self.y_test, verbose=2) #verbose는 세세한것을 단순하게 하나로 나타내는 것 에시로 평균

    def test(self):
        pass




if __name__ == '__main__':
    pass