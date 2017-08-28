"""Exemplary functions to sort objects alphabetically considering diactric marks."""
import locale
locale.setlocale(locale.LC_ALL, '')


class Person:
    """Exemplary class for creating objects."""
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return self.first + " " + self.last


def sort_by_first(inputdata):
    """Return objects sorted alphabetically by firstname."""
    return sorted(inputdata, key=lambda x: (locale.strxfrm(x.first)))


def sort_by_last(inputdata):
    """Return objects sorted alphabetically by lastname."""
    return sorted(inputdata, key=lambda x: (locale.strxfrm(x.last)))
