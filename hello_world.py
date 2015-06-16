__author__ = 'Scott'


class hello_class():
    def __init__(self):
        self.user_string = ''

    def hello_world(self):
        print('hello world')

    def main(self):
        while True:
            arg = input('-> ')
            if (arg == 'quit'):
                print(self.user_string)
                break
            else:
                self.user_string += arg


if __name__ == '__main__':
    hc = hello_class()
    hc.hello_world()
    hc.main()