from matplotlib import pyplot as plt
from sklearn.datasets import load_digits
import matplotlib.gridspec as gridspec

class Similarity:

    @staticmethod
    def image():
        plt.figure(figsize=(9, 9))
        gs = gridspec.GridSpec(1, 8, height_ratios=[1],
                               width_ratios=[9, 1, 9, 1, 9, 1, 9, 1])
        for i in range(4):
            plt.subplot(gs[2 * i])
            plt.imshow(eval("d" + str(i + 1)), aspect=1,
                       interpolation='nearest', cmap=plt.cm.bone_r)
            plt.grid(False)
            plt.xticks([])
            plt.yticks([])
            plt.title("image {}".format(i + 1))
            plt.subplot(gs[2 * i + 1])
            plt.imshow(eval("v" + str(i + 1)), aspect=0.25,
                       interpolation='nearest', cmap=plt.cm.bone_r)
            plt.grid(False)
            plt.xticks([])
            plt.yticks([])
            plt.title("vector {}".format(i + 1))
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    digits = load_digits()
    d1 = digits.images[0]
    d2 = digits.images[10]
    d3 = digits.images[1]
    d4 = digits.images[11]
    v1 = d1.reshape(64, 1)
    v2 = d2.reshape(64, 1)
    v3 = d3.reshape(64, 1)
    v4 = d4.reshape(64, 1)
    Similarity().image()