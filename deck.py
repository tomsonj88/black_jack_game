"""
Module contain Deck class to create deck of cards to use in game
"""

import sys
from random import shuffle
from card import Card


class Deck:
    """
    Deck class contains from 52 cards
    """
    def __init__(self):
        self.cards = self.create_deck()

    @staticmethod
    def create_deck() -> list:
        """
        Methods return deck contains of 52 Card objects.
        return: list
        """
        values = [str(element) for element in range(2, 11)]
        rest_values = ['J', 'Q', 'K', 'A']
        values.extend(rest_values)
        cards = []
        colors = ["c", "d", "h", "s"]
        for value in values:
            for color in colors:
                cards.append(Card(value, color))
        return cards

    def shuffle_deck(self) -> None:
        """
        Method to shuffle cards
        return: None
        """
        shuffle(self.cards)

    def hand_out(self):
        """
        Handing out card for players
        return
        """
        try:
            top_card = self.cards.pop(0)
            return top_card
        except IndexError:
            return sys.exit("Deck is empty. Game over!")
