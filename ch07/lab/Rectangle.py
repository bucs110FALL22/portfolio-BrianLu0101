
class Rectangle:

    def __init__(self, x, y, h, w):
        '''
        Holds rectangle arguments for rectangle object

        Param:
        self = object
        x = x-coordinate upper left position
        y = y-coordinate upper left position
        h = height of rectangle
        w = width of rectangle

        Return:
        Arguments create rectangle object
        '''
        self.x = x
        self.y = y
        self.h = h
        self. w = w
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.h < 0:
            self.h = 0
        if self.w < 0:
            self.w = 0

    def __str__(self):
        '''
        Returns x,y,w,h of rectangle

        Param:
        self = object

        Return:
        A string with x, y, width, and height
        '''
        return f"(x:{self.x},y:{self.y},height:{self.h},width:{self.w})"