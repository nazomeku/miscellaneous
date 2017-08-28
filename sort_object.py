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


def sort_by_first(information):
    """Return information sorted alphabetically by firstname."""
    return sorted(information, key=lambda x: (locale.strxfrm(x.first)))


def sort_by_last(information):
    """Return information sorted alphabetically by lastname."""
    return sorted(information, key=lambda x: (locale.strxfrm(x.last)))
