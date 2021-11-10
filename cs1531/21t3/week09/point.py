class Point:
    def __init__(self, x, y):
        '''
        Initialises the point with the given co-ordinates
        '''
        self.x = x
        self.y = y

    def get_coords(self):
        '''
        Returns the co-ordinates as a tuple
        '''
        return (self.x, self.y)

    def set_x(self, x):
        '''
        Sets the x co-ordinate
        '''
        self.x = x

    def set_y(self, y):
        '''
        Sets the y co-ordinate
        '''
        self.y = y

    def __add__(self, point):
        '''
        Returns a new point which is the vector addition of this point,
        and the point given.

        Both this point and the point given remain unchanged.
        '''
        return Point(self.x + point.x, self.y + point.y)

    def __mul__(self, scalar):
        '''
        Returns a new point which is the scalar multiplication of this point and
        the given value.

        This point remains unchanged.
        '''
        return Point(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Point x: {self.x} and point y: {self.y}"
    

if __name__ == '__main__':
    a = Point(0, 0)
    b = Point(1, 2)
    c = a + b
    # print(c.get_coords())
    print(c)
    