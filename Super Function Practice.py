
class Rectangle:
    pass

class Square(Rectangle):

    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        self.length = length