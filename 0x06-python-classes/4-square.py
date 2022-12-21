#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @propety
    def size(self):

        """Gets the value"""
        return (self.__size)

    @size.setter
    def size(self, value):

        """Sets the size"""

        if type(value) != int:
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >=0")
        self.__size = value

    def area(self):

        """Public instance method that returns the current sqr area"""

        return (self.__size * self__size)
