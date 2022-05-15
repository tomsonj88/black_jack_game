"""
BLACK JACK GAME
PYCAMP
"""
import sys

from deck import Deck
from player import Player, Human, Dealer, InvalidCardQuantity
from game import Game

# talia = Deck()
# print(talia.cards)
# talia.shuffle_deck()
# print(talia.cards)
# talia.hand_out()
# print(talia.cards)
#
# gracz = Player("Tomson")
# try:
#     karty_gracza = gracz.take_cards(2)
#     # print(gracz.take_cards(2))
#     #karty_gracza = gracz.take_cards(1)
#     print(karty_gracza)
#     punkty = gracz.count_points()
#     print(f"Twoje punkty to: {punkty}")
# except InvalidCardQuantity as error_text:
#     print(error_text)

#################
game = Game("Adam")
game.player_turn()
game.dealer_turn()
game.who_is_winner(game.dealer.count_points(), game.player.count_points())
# krupier = Dealer("krupier")
# krupier.dealer_turn()

