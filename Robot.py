class Robot:

    COORDS_MAX = 20
    COORDS_MIN = -20

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left(self):
        if self.x > Robot.COORDS_MIN:
            self.x -= 1
            print(f'x = {self.x}, y = {self.y}')

    def right(self):
        if self.x < Robot.COORDS_MAX:
            self.x += 1
            print(f'x = {self.x}, y = {self.y}')

    def up(self):
        if self.y > Robot.COORDS_MIN:
            self.y -= 1
            print(f'x = {self.x}, y = {self.y}')

    def down(self):
        if self.y < Robot.COORDS_MAX:
            self.y += 1
            print(f'x = {self.x}, y = {self.y}')

    def move(self, message):
        for i in message:
            if i == 'N':
                self.up()
            elif i == 'S':
                self.down()
            elif i == 'W':
                self.left()
            else:
                self.right()


