"""
BLACK JACK GAME
PYCAMP
"""

from deck import Deck
from player import Player

talia = Deck()
print(talia.cards)
talia.shuffle_deck()
print(talia.cards)
talia.hand_out()
print(talia.cards)

gracz = Player("Tomson")
karty_gracza = gracz.take_cards(2)
# print(gracz.take_cards(2))
print(karty_gracza)
punkty = gracz.count_points(karty_gracza)
print(f"Twoje punkty to: {punkty}")



##################

#################


