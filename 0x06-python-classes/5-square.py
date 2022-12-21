#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    def size(self):

        """gets the value"""
        return (self.__size)

    def size(self, value):

        """sets the size"""

        if type(value) != int:
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):

        """prints in stdout the sqr with chr #"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print()
