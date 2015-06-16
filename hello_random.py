__author__ = 'Scott'
import random


class random_class():
    def __init__(self):
        self.high = -1
        self.low = -1
        self.number = -1

    def main(self):
        self.high = int(input('High range of random -> '))
        self.low = int(input('low range of random -> '))
        self.number = int(input('number of randoms -> '))

        for i in range(0, self.number):
            print(random.randrange(self.low, self.high))


if __name__ == '__main__':
    rand = random_class()
    rand.main()