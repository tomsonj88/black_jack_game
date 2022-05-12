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

    def add_card(self):
        self.cards.append(self.take_cards(1)[0])

    # def turn_pass(self):
    #     print("PASS")
    #     return "pass"

    def count_points(self):
        points = 0
        point_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                      "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": [1, 11]
                      }
        # ToDo: change points procedure for AS
        # A + A = 21 -> black Jack
        # A + 10 or J or Q or K -> 21
        values = [str(element) for element in range(2, 11)]
        rest_values = ['J', 'Q', 'K', 'A']
        values.extend(rest_values)

        # self.cards = [Card("A"), Card("A")]
        for element in self.cards:
            # if element.value == "A":
            #     points = self.as_counting_points(points, point_dict)
            for value in values:
                if element == Card(value):
                    if element.value == "A":
                        points = self.as_counting_points(points, point_dict)
                    else:
                        points += point_dict[value]
                        break
        return points

    def as_counting_points(self, current_points, point_dict):
        if 10 < current_points < 21:
            current_points += point_dict["A"][0]
        elif len(self.cards) == 2 and (self.cards[0] == self.cards[1]):
            current_points = 21
            return current_points
        else:
            current_points += point_dict["A"][1]
        return current_points

    def show_cards(self):
        print(f"{self.name} cards: {self.cards}, points: {self.count_points()}")


class Human(Player):
    def make_decision(self):
        decision = input(f"{self.name } make decision: c - take another cards or p - pass")
        return decision.lower()


class Dealer(Player):
    def dealer_game(self, opponent_points):
        while self.count_points() <= opponent_points and 17 >= self.count_points() <= 21: # ToDo check this change
            self.add_card()     # ToDo jesli remis po 21, to krupier powinien PASS i jest remis
            self.show_cards()
            if self.count_points() == 21:
                break

