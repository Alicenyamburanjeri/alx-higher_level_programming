#!/usr/bin/python3
""" Defines a class and inherited class that checks a function """


def is_kind_of_class(obj, a_class):
    """ Checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of object.
    Returns:
        True if object is an instance or inherited instance of a_class.
        False if otherwise """
    if isinstance(obj, a_class):
        return True
    return False
