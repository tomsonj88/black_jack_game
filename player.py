"""
class Player
"""
from deck import Deck
from card import Card


class Player:
    """"
    class Player
    ToDo: finish docstring !!!
    """
    def __init__(self, name):
        self.name = name
        self.deck = Deck()

    def take_cards(self, quantity):
        # TODO: quantity should be positive value
        #  and not greater than 52 -> make exception throw
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

    def count_points(self, cards):
        point = 0
        point_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
                      "K": 10, "A": 1}
        values = [str(element) for element in range(2, 11)]
        rest_values = ['J', 'Q', 'K', 'A']
        [values.append(element) for element in rest_values]

        for element in cards:
            for value in values:
                if element == Card(value):
                    point += point_dict[value]
        return point
