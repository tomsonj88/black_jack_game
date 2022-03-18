"""
class Player
"""
from deck import Deck


class Player():
    """"
    class Player
    ToDo: finish docstring !!!
    """
    def __init__(self, name):
        self.name = name
        self.deck = Deck()

    def take_cards(self, quantity):
        cards = []
        self.deck.shuffle_deck()
        while quantity:
            cards.append(self.deck.hand_out())
            quantity -= 1
        return cards

    def show_cards(self):
        pass

    def stop(self):
        pass

    def count_points(self):
        pass