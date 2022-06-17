"""
Module to test Game class
"""

from game import Game


def test_who_is_winner():
    """
    Test checks if procedure correct choose winner
    """
    game = Game("Adriano")
    assert game.who_is_winner(17, 18) == 2
    assert game.who_is_winner(17, 17) == 3
    assert game.who_is_winner(19, 16) == 1
    assert game.who_is_winner(21, 21) == 3
