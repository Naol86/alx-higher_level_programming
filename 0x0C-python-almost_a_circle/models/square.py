#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        Square.validator(self, "width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs[i]
                elif i == "size":
                    self.width = self.height = kwargs[i]
                elif i == "x":
                    self.x = kwargs[i]
                elif i == "y":
                    self.y = kwargs[i]
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        tem = {'id': self.id, 'size': self.width,
               'x': self.x, 'y': self.y}
        return tem
