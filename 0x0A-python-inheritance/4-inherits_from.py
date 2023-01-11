#!/usr/bin/python3
""" Defines an inherited class-checking funtion """


def inherits_from(obj, a_class):
    """ Checks if an object is an inherited instance of a class.
    Args:
        obj: the object
        a_class (type): The class to match the obj type
    Returns:
        True if an obj is an inherited instance of a_class
        False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
