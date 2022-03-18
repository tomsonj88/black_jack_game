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
print(gracz.take_cards(2))



##################

#################


