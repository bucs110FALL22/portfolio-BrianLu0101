import Rectangle

class Surface:
    def __init__(self,filename,x,y,h,w):
        '''
        Create rectangle object and image file name

        Param:
        self = object
        filename = name of file as string
        x = x-coordinate of upper left position
        y = y-coordinate of upper left position
        h = height of rectangle
        w = width of rectangle
        
        Return:
        Store value for created rectangle object and image file
        '''
        self.rect = Rectangle.Rectangle(x,y,h,w)
        self.image = filename

    def getRect(self):
        '''
        Create the rectangle visual

        Param:
        self = object

        Return:
        Rectangle image
        '''
        return self.rect