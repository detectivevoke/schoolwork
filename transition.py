

class swap(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.temp = None

    def swap(self):

        self.temp = self.x
        print('Your new "x" is {}'.format(self.temp))
        self.temp = self.y
        print('Your new "y" is {}'.format(self.temp))


x = input("X value: ")
y = input("Y value: ")

swap(x,y).swap()
