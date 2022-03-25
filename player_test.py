"""
Module to test Player module
"""
from random import randint

from player import Player
from card import Card


def test_quantity_of_take_cards():
    """
    Purpose of this test is to check if take_cards method return
    good quantity of cards. Using for loop it let check more
    function calls defined in for loop range. Quantity of cards
    is drawn by randint.
    """
    player_stefan = Player("Stefan")
    the_highest = 52
    for element in range(5):
        card_quantity = randint(0, the_highest)
        cards = player_stefan.take_cards(card_quantity)
        assert len(cards) == card_quantity
        the_highest = the_highest - card_quantity
        if not the_highest:
            break


def test_lower_range_of_take_cards():
    gracz_robin = Player("Robin")
    card_quantity = 0
    cards = gracz_robin.take_cards(card_quantity)
    assert len(cards) == card_quantity


def test_higher_range_of_take_cards():
    gracz_vanessa = Player("Vanessa")
    card_quantity = 52
    cards = gracz_vanessa.take_cards(card_quantity)
    assert len(cards) == card_quantity


def test_check_count_points():
    player_greg = Player("Greg")
    cards = [Card("2"), Card("K")]
    assert player_greg.count_points(cards) == 12
    cards = [Card("10"), Card("K"), Card("9")]
    assert player_greg.count_points(cards) == 29
    cards = [Card("3"), Card("7")]
    assert player_greg.count_points(cards) == 10
    cards = [Card("Q"), Card("J")]
    assert player_greg.count_points(cards) == 20


#test_check_count_points_with_As()us
