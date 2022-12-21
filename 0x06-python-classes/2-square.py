#!/usr/bin/python3
class Square:
    def __init__(self, size=0):

        """Private instance attribute: size"""

        if type(size) != int:
            raise TypeError("Size must be an int")
        if size < 0:
            raise ValueError("Size  must be >=0")
        self.__size = size
