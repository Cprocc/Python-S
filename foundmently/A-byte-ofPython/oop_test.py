class shape:
    shape_count = 0
    def __init__(self,edge):
        self.edge = edge
        shape.shape_count += 1
        print('(Initialized shape have {} edges)'.format(self.edge))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.shape_count))

class rectangle(shape):
    def __init__(self,edge,width,height):
        shape.__init__(self,edge)
        self.width = width
        self.height = height
        print('(Initialized rectangle_width is {},height is{})'.format(self.width,self.height))

class square(shape):
    def __init__(self,edge,weight):
        shape.__init__(self,edge)
        self.weight = weight
        print('(Initialized square_weight is{})'.format(self.weight))

shape1 = rectangle(4,2,3)
shape2 = square(4,4)
print(shape.shape_count)