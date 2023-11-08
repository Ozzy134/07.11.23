class Snow:

    def __init__(self, num):
        self.num = num

    def makeSnow(self, snow):

        for i in range(self.num // snow ):
            print('*' * snow)

        print('*' * (self.num % snow))

    def __add__(self, other):
        if not isinstance(other, (Snow, int)):
            raise TypeError('NO')
        if not isinstance(other, int):
            return Snow(self.num + other)
        else:
            return Snow(self.num + other.num)

    def __sub__(self, other):
        if not isinstance(other, (Snow, int)):
            raise TypeError('NO')
        if not isinstance(other, int):
            return Snow(self.num - other)
        else:
            return Snow(self.num - other.num)

    def __mul__(self, other):
        if not isinstance(other, (Snow, int)):
            raise TypeError('NO')
        if not isinstance(other, int):
            return Snow(self.num * other)
        else:
            return Snow(self.num * other.num)

    def __floordiv__(self, other):
        if not isinstance(other, (Snow, int)):
            raise TypeError('NO')
        if not isinstance(other, int):
            return Snow(self.num / other)
        else:
            return Snow(self.num / other.num)

num = Snow(112)
num.makeSnow(10)
num = num + 100
num.makeSnow(10)
pip = Snow(15)
num = num + pip
num.makeSnow()
num.makeSnow(13)