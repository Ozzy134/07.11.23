# def my_dec(func):
#     def wrapper():
#         print('before func')
#         func()
#         print('after func')
#     return wrapper
#
# @my_dec
# def hello():
#     print('hello')
#
# hello()

# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD < arg < cls.MAX_COORD
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
# v = Vector(1, -5)
# print(v.y)
#
# from math import pi
#
# class Cylinder:
#
#     @staticmethod
#     def make_area(d, h):
#         circle = pi * d ** 2 / 4
#         side = pi * d * h
#         return circle * 2 + side
#
#     def __init__(self, diametr, high):
#         self.diametr = diametr
#         self.high = high
#         self.area = self.make_area(diametr, high)
#
#     def __str__(self):
#         print(f'd = {self.diametr}, h = {self.high}, area = {self.area}')
#
#     def get_info(self):
#         print(f'd = {self.diametr}, h = {self.high}, area = {self.area}')
#
#     def __add__(self, other):
#         self.diametr = self.diametr + other.diametr
#         self.high = self.high + other.high
#         self.area = self.make_area(self.diametr, self.high)
#         return Cylinder(self.diametr, self.high)
#
# c = Cylinder(4, 2)
# print(c.get_info())

# class MyClass:
#     TOTAL_OBJECTS = 0
#
#     def __init__(self):
#         MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1
#
#     @classmethod
#     def total_objects(cls):
#         print('Total objects', cls.TOTAL_OBJECTS)
#
# class ChaildClass(MyClass):
#     TOTAL_OBJECTS = 0
#
#     def __init__(self):
#         ChaildClass.TOTAL_OBJECTS += 1
#
#
#
# m = MyClass()
# m1 = MyClass()
# cc = ChaildClass()
# MyClass.total_objects()
# ChaildClass.total_objects()

class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if Point.MIN_COORD < x < Point.MAX_COORD:
            self.x = x
            self.y = y

    def __str__(self):
        return f'x = {self.x}, y = {self.y}'

    @classmethod
    def set_bound(self, left):
        self.MIN_COORD = left

    def __getattribute__(self, item):
        print('get atribute')
        if item == '_Point__x':

        return object.__getattribute__()

    def __setattr__(self, key, value):
        print('set atribute')
        if key == 'z':
            raise AttributeError('Нельзя задавать данный атрибут')
        else:
            object.__setattr__(self, key, value)

p = Point(1,5)
p.set_bound(-100)
print(Point.__dict__)
print(p.__dict__)