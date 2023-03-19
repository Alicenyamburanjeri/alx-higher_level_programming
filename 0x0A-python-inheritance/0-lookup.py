#!/usr/bin/python3
""" Defines the list of available atrribute and methos of an object """


def lookup(obj):
    """ Return a list of an object's available attributes."""
    return (dir(obj))
