"""
ToDo: Make docstring
"""
import sys

from deck import Deck
from player import Player, Human, Dealer


class GameOver(Exception):
    pass


class Game:
    def __init__(self, player):
        self.player = Human(player)
        self.deck = Deck()
        self.dealer = Dealer("Dealer")

    def player_turn(self):
        self.player.show_cards()
        while self.player.count_points() <= 21:
            decision = self.player.make_decision()
            if decision == "c":
                self.player.add_card()
                self.player.show_cards()
                try:
                    self.check_early_end_game()
                except GameOver as exception:
                    print(exception)
                    sys.exit()
            elif decision == "p":
                print(f"{self.player.name} PASS")
                break
            else:
                print(f"{self.player.name} wrong choice. Try one more time")

    def dealer_turn(self):
        self.dealer.show_cards()
        self.dealer.dealer_game(self.player.count_points())

    def who_is_winner(self):
        dealer_points = self.dealer.count_points()
        player_points = self.player.count_points()
        if 21 >= dealer_points > player_points:
        # if dealer_points <= 21 and dealer_points > player_points:
            print(f"{self.dealer.name} wins !!!")
        elif player_points <= 21 and player_points < dealer_points:
            print(f"{self.player.name} wins !!!")
        else:
            print("It's draw")

    def check_early_end_game(self):
        player_points = self.player.count_points()
        if player_points > 21:
            raise GameOver("GAME OVER. Dealer wins.")
            # print("GAME OVER. Dealer wins.")
            # sys.exit()  # ToDo change to exception