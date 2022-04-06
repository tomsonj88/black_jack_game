"""
BLACK JACK GAME
PYCAMP
"""
import sys

from deck import Deck
from player import Player, Human, Dealer, InvalidCardQuantity
from game import Game

talia = Deck()
print(talia.cards)
talia.shuffle_deck()
print(talia.cards)
talia.hand_out()
print(talia.cards)

gracz = Player("Tomson")
try:
    karty_gracza = gracz.take_cards(2)
    # print(gracz.take_cards(2))
    #karty_gracza = gracz.take_cards(1)
    print(karty_gracza)
    punkty = gracz.count_points()
    print(f"Twoje punkty to: {punkty}")
except InvalidCardQuantity as error_text:
    print(error_text)




##################
print("################## New game ##################")
# gracz_stefan = Human("Stefan")
# krupier = Dealer("krupier")
# print(gracz_stefan)
# print(krupier)
# print(f"{gracz_stefan.name} turn")
# while True:
#     decision = gracz_stefan.make_decision()
#     if decision == "c":
#         gracz_stefan.add_card()
#         # ToDo check points: if are greater than 21, turn ends
#         print(gracz_stefan)
#         stefan_points = gracz_stefan.count_points()
#         if stefan_points > 21:
#             print("GAME OVER. Dealer wins.")
#             sys.exit()
#     elif decision == "p":
#         print(f"{gracz_stefan.name} PASS")
#         break
#     else:
#         print(f"{gracz_stefan.name} wrong choice. Try one more time")
# #ToDo Dealer turn
# print(gracz_stefan)
#################
gra = Game("Adam")
gra.player_turn()
gra.dealer_turn()
# krupier = Dealer("krupier")
# krupier.dealer_turn()

