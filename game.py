"""
ToDo: Make docstring
"""
import sys

from deck import Deck
from player import Player, Human, Dealer


class Game():
    def __init__(self, player):
        self.player = Human(player)
        self.deck = Deck()
        self.dealer = Dealer("Dealer")

    def player_turn(self):
        self.player.show_cards()
        while True:
            decision = self.player.make_decision()
            if decision == "c":
                self.player.add_card()
                # ToDo check points: if are greater than 21, turn ends
                print(self.player)
                points = self.player.count_points()
                if points > 21:
                    print("GAME OVER. Dealer wins.")
                    sys.exit()  #ToDo change to exception
            elif decision == "p":
                print(f"{self.player.name} PASS")
                break
            else:
                print(f"{self.player.name} wrong choice. Try one more time")

    def dealer_turn(self):
        self.dealer.show_cards()
        self.dealer.dealer_game(self.player.count_points())
# ToDo who win or maybe it is draw