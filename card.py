""""
Module contain Card class to create card object
"""


class InvalidValue(Exception):
    """Exception when wrong value card will be choosen"""


class InvalidColor(Exception):
    """Exception when wrong color card will be choosen"""


class Card:
    """
    class Card describes card object
    ToDo: karta jako krotka: karta = (value, suit)
    """

    possible_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    possible_colors = ["c", "d", "h", "s"]  # c - clubs, d - diamonds, h - hearts, s -spades

    def __init__(self, value, suit):
        if value not in self.possible_values:
            raise InvalidValue("Wrong card value")
        self.value = value

        if suit not in self.possible_colors:
            raise InvalidColor("Wrong card color")
        self.suit = suit

    def __str__(self):
        return self.value + self.suit

    def __repr__(self):
        return f"{self.value}{self.suit}"

    def __eq__(self, other):
        return all([self.value == other.value])
