""""
Module contain Card class to create card object
"""


class Card:
    """
    class Card describes card object
    ToDo: karta jako krotka: karta = (value, suit)
    """

    POSSIBLE_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    POSSIBLE_COLORS = ["c", "d", "h", "s"]  # c - clubs, d - diamonds, h - hearts, s -spades

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.value + self.suit

    def __repr__(self):
        return f"{self.value}{self.suit}"

    def __eq__(self, other):
        return all([self.value == other.value])
