__author__ = 'Scott'
import random
import csv

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import numpy as np


class random_class():
    def __init__(self):
        self.high = -1
        self.low = -1
        self.number = -1
        self.array = np.array([])

    def main(self):
        self.high = int(input('High range of random -> '))
        self.low = int(input('low range of random -> '))
        self.number = int(input('number of randoms -> '))

        # for i in range(0, self.number):
        print(random.randrange(self.low, self.high))
        f = open('numbers.txt', 'wt')
        try:
            for i in range(0, self.number):
                f.write(str(random.randrange(self.low, self.high)) + '\n')
        finally:
            f.close()

        self.plot()

    def plot(self):
        mu, sigma = 100, 15
        #x = mu + sigma * np.random.randn(10000)
        #print(type(x))
        theta=[]
        with open("numbers.txt") as f:
            for line in f:
                theta.append(float(line))
        print(theta)
        print('Standard deviation ' + str(np.std(theta)))
        print('Mean ' + str(np.mean(theta)))
        print('Median ' + str(np.median(theta)))
        # the histogram of the data
        n, bins, patches = plt.hist(theta, 50, normed=1, facecolor='green', alpha=0.75)
        plt.title('Histogram')
        plt.axis([self.low, self.high, 0.0, .05])

        plt.savefig('foo.png')


if __name__ == '__main__':
    rand = random_class()
    rand.main()

