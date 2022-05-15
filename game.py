"""
ToDo: Make docstring
"""

from deck import Deck
from player import Human, Dealer


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
            elif decision == "p":
                print(f"{self.player.name} PASS")
                break
            else:
                print(f"{self.player.name} wrong choice. Try one more time")

    def dealer_turn(self):
        self.dealer.show_cards()
        self.dealer.dealer_game(self.player.count_points())

    def who_is_winner(self, dealer_points, player_points):
        winner_dict = {1: str(self.dealer.name), 2: str(self.player.name), 3: "draw"}
        if dealer_points <= 21 and (dealer_points > player_points or player_points > 21):
            winner = 1
        elif player_points <= 21 and (player_points > dealer_points or dealer_points > 21):
            winner = 2
        else:
            winner = 3

#        if winner == 1 or winner == 2:
        if winner in (1, 2):
            print(f"{winner_dict[winner]} wins !!!")
        else:
            print("It's draw")
        return winner
