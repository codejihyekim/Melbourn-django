from sklearn.datasets import load_iris

class Isis:
    def __init__(self):
        self.isis = load_iris()

    def main(self):
        print(self.isis.date[0, :])

if __name__ == '__main__':
    Isis().main()
    

