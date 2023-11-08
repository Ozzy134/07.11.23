class SnowFlake:

    def __init__(self, number):
        self.number = number

    def snow(self):
        k = 0
        st = ''
        for i in range(self.number):
            for j in range(self.number):
                if j == k or j == k + 1:
                    st += '*'
                elif self.number - j == k + 1 or self.number - j == k + 2:
                    st += '*'
                elif j == self.number // 2:
                    st += '*'
                elif i == self.number // 2:
                    st += '*'
                else:
                    st += ' '
            print(st)
            st = ''
            k += 1

    def thaw(self):
        self.number = self.number - 2

    def frezee(self):
        self.number = self.number * 2

s = SnowFlake(11)
s.snow()
s.thaw()
s.frezee()