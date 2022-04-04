"""
class Player
"""
from deck import Deck
from card import Card


class InvalidCardQuantity(Exception):
    """Exception if number of handing card is less than 0 or bigger than 52"""


class Player:
    """"
    class Player
    ToDo: finish docstring !!!
    """
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.cards = self.take_cards(2)

    def __str__(self):
        return f"{self.name} has cards: {self.cards}. Points: {self.count_points()}"

    def take_cards(self, quantity):
        if quantity < 0 or quantity > 52:
            raise InvalidCardQuantity("Invalid number of cards")
        cards = []
        self.deck.shuffle_deck()
        while quantity:
            cards.append(self.deck.hand_out())
            quantity -= 1
        return cards


    def turn_pass(self):
        print("PASS")
        return "pass"

    def count_points(self):
        point = 0
        point_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
                      "K": 10, "A": 1}
        values = [str(element) for element in range(2, 11)]
        rest_values = ['J', 'Q', 'K', 'A']
        [values.append(element) for element in rest_values]

        for element in self.cards:
            for value in values:
                if element == Card(value):
                    point += point_dict[value]
        return point


class Human(Player):
    def make_decision(self):
        decision = input("Make decision: t - take another cards or p - pass")
        if decision == "t":
            self.cards.append(self.take_cards(1)[0])
            print("dupa")
        elif decision == "p":
            self.turn_pass()
        else:
            print("bad choice")


class Dealer(Player):
    # ToDo: make here dealer game algorithm
    pass
