"""
BLACK JACK GAME
PYCAMP

# Todo: Add features: 1 - tokens, 2 - player name choosing at the game beginning
"""
from game import Game

game = Game("Adam")
game.player_turn()
game.dealer_turn()
game.who_is_winner(game.dealer.count_points(), game.player.count_points())
