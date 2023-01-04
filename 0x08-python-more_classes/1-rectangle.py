#!/usr/bin/python3
"""

This module is composed of a class that defines a Rectangle


"""


class Rectangle:
    """ Class that defines a Rectangle """

    def __init__(self, width=0, height=0):
        """ Method that initalises the instance

        Args:
            width: the rectangle's width
            height: the rectangle's height


        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """ method that returns the value of the width

            Returns:
                width of the rectangle

            """

            return self.__width

        @width.setter
        def width(self, value):
            """ This method defines the width

            Args:
                value: width


            Raises:
                TypeError: if width is not an int
                ValueError: if width < 0


            """

            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ method that returns the value of height

            Returns:
                height of rectangle


            """

            return self.__height

        @height.setter
        def height(self, value):
            """ method that defines the height

            Args:
                value: height

                Raises:
                    TypeError: if height is not an integer
                    ValueError: if height is less than zero


            """

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value
