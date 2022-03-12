"""
BLACK JACK GAME
PYCAMP
"""


class Card():
    """
    class Card describes card object
    """
    def __init__(self, value):
        self.value = value
        # self.suit = suit

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"{self.value}"


class Deck():
    """
    Deck class contains from 52 cards
    """
    def __init__(self):
        self.cards = self.create_deck()

    @staticmethod
    def create_deck() -> list:
        """
        Methods return deck contains of 52 Card objects.
        :return: list
        """
        values = [str(element) for element in range(2, 11)]
        rest_values = ['J', 'Q', 'K', 'A']
        [values.append(element) for element in rest_values]
        values = values * 4
        cards = [Card(element) for element in values]
        return cards

    def shuffle_deck(self):
        """
        Method to shuffle cards
        :return
        """

    def handing_out(self):
        """
        Handing out cards for players
        :return
        """


talia = Deck()
print(talia.cards)
