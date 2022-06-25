"""
Module Player contains classes: Player, Human and Dealer.
"""
from deck import Deck
from card import Card


class InvalidCardQuantity(Exception):
    """Exception if number of handing card is less than 0 or bigger than 52"""


class Player:
    """"
    class Player is responsible for player game such as
    count point, take cards, show cards
    """
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.cards = self.take_cards(2)

    def __str__(self):
        return f"{self.name} has cards: {self.cards}. Points: {self.count_points()}"

    def take_cards(self, quantity):
        """
        Method taking cards from deck. Before taking cards,
        deck is shuffled. Method is using, when Player object is created
        """
        if quantity < 0 or quantity > 52:
            raise InvalidCardQuantity("Invalid number of cards")
        cards = []
        self.deck.shuffle_deck()
        while quantity:
            cards.append(self.deck.hand_out())
            quantity -= 1
        return cards

    def add_card(self):
        """
        Take one additional card from deck
        """
        self.cards.append(self.take_cards(1)[0])

    def count_points(self):
        """
        Method counts points: cards from 2 to 10 have points same like it number,
        J,Q,K - 10 points
        A - 1 or 11 (depend what is better for player)
        """
        points = 0
        point_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                      "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": [1, 11]
                      }
        # A + A = 21 -> black Jack
        # A + 10 or J or Q or K -> 21
        values = [str(element) for element in range(2, 11)]
        rest_values = ['J', 'Q', 'K', 'A']
        values.extend(rest_values)

        for element in self.cards:
            for value in values:
                if element == Card(value, suit="a"):
                    if element.value == "A":
                        points = self.as_counting_points(points, point_dict)
                    else:
                        points += point_dict[value]
                        break
        return points

    def as_counting_points(self, current_points, point_dict):
        """
        Procedure to counting points for AS card:
        AS has score 1 or 11, depend what is better for player
        """
        if 10 < current_points < 21:
            current_points += point_dict["A"][0]
        elif len(self.cards) == 2 and (self.cards[0] == self.cards[1]):
            current_points = 21
            return current_points
        else:
            current_points += point_dict["A"][1]
        return current_points

    def show_cards(self):
        """
        Method is for display player's cards and points
        """
        print(f"{self.name} cards: {self.cards}, points: {self.count_points()}")


class Human(Player):
    """
    class Human contains method to make decision for human player
    """
    def make_decision(self):
        """
        Make decision by player: pass or take one more card
        """
        decision = input(f"{self.name } make decision: c - take another cards or p - pass")
        return decision.lower()


class Dealer(Player):
    """
    Class Dealer contains procedure of dealer game
    """
    def dealer_game(self, opponent_points):
        """
        Dealer game procedure. Dealer should be better than human ;)
        He always want to win
        """
        while (self.count_points() <= opponent_points <= 21) or (17 > self.count_points() <= 21):
            if self.count_points() == 21:
                break
            self.add_card()
            self.show_cards()

    def show_hidden_cards(self):
        """
        Show first dealer's card, second card is hidden
        """
        print(f"{self.name} cards: [{self.cards[0]}, X]")
