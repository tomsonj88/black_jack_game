"""
BLACK JACK GAME
PYCAMP
"""

from deck import Deck
from player import Player, Human, Dealer, InvalidCardQuantity

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
gracz_stefan = Human("Stefan")
print(gracz_stefan)
gracz_stefan.make_decision()
print(gracz_stefan)
#################


