# -*- coding: utf-8 -*-
import cv2
from matplotlib import pyplot as plt

class CVTest:
    def __init__(self, filename):
        self.im = cv2.imread(filename)
        self.reset_data()

    def reset_data(self):
        self.gray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
        self.height = self.im.shape[0]
        self.width = self.im.shape[1]

    def resize(self, dsize, fx=None, fy=None):
        self.im = cv2.resize(self.im, dsize, fx=fx, fy=fy)
        self.reset_data()

    def show_im(self):
        plt.imshow(self.im[:,:,::-1])
        plt.show()

    def show_gray(self):
        plt.imshow(cv2.cvtColor(self.gray, cv2.COLOR_GRAY2RGB))
        plt.show()

    @staticmethod
    def show_pic(pic, code=None):
        if not code:
            plt.imshow(pic)
        else:
            plt.imshow(cv2.cvtColor(pic, code))
        plt.show()
