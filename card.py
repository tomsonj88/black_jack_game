""""
Module contain Card class to create card object
"""


class Card:
    """
    class Card describes card object
    ToDo: karta jako krotka: karta = (value, suit)
    """
    def __init__(self, value):
        self.value = value
        # self.suit = suit

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"{self.value}"

    def __eq__(self, other):
        return all([self.value == other.value])
