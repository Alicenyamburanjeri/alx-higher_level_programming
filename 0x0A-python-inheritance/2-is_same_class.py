#!/usr/bin/python3
""" Defines a class that checks a function """


def is_same_class(obj, a_class):
    """ Checks if an object is an instance of a specific class.
    Args:
        obj (any): The object to be checked
        a_class (type): The class to match the object.
    Returns:
        True if obj is exactly an instance of a_class
        False if otherwise """
    if type(obj) == a_class:
        return True
    return False
