"""
BLACK JACK GAME
PYCAMP
"""
from game import Game

game = Game("Adam")
game.player_turn()
game.dealer_turn()
game.who_is_winner(game.dealer.count_points(), game.player.count_points())
