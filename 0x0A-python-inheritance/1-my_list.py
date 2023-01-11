#!/usr/bin/python3
""" Contains a class called MyList """


Class MyList(list):
    """ A subclass of list """
    def __init__(self):
        """ initializes the object """
        super().__init__()

    def print_sorted(self):
        """ Prints the sorted list """
        print(sorted(self))
