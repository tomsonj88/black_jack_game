"""
Module to test Player class
"""
from random import randint

from player import Player
from card import Card

suit = "c"


def test_quantity_of_take_cards():
    """
    Purpose of this test is to check if take_cards method return
    good quantity of cards. Using for loop it let check more
    function calls defined in for loop range. Quantity of cards
    is drawn by randint.
    """
    player_stefan = Player("Stefan")
    the_highest = 50        # because two cards go to player, when object is initialized
    for _ in range(5):
        card_quantity = randint(1, the_highest)
        cards = player_stefan.take_cards(card_quantity)
        assert len(cards) == card_quantity
        the_highest = the_highest - card_quantity
        if not the_highest:
            break


def test_lower_range_of_take_cards():
    """
    Test for checking take_cards method.
    It takes 0 cards and check if quantity is good after taken 0 cards
    """
    gracz_robin = Player("Robin")
    card_quantity = 0
    cards = gracz_robin.take_cards(card_quantity)
    assert len(cards) == card_quantity


def test_higher_range_of_take_cards():
    """
    Test for checking take_cards method. It takes 50 cards (because 2 cards has got player)
    and check if quantity is good after taken 50 cards
    """
    gracz_vanessa = Player("Vanessa")
    card_quantity = 50
    cards = gracz_vanessa.take_cards(card_quantity)
    assert len(cards) == card_quantity


def test_check_count_points():
    """
    Test for checking count_points method. Player took two cards and after this test checks
    if points are correct counted
    """
    player_greg = Player("Greg")
    player_greg.cards =[Card("2", suit), Card("K", suit)]
    assert player_greg.count_points() == 12
    player_greg.cards = [Card("10", suit), Card("K", suit), Card("9", suit)]
    assert player_greg.count_points() == 29
    player_greg.cards = [Card("3", suit), Card("7", suit)]
    assert player_greg.count_points() == 10
    player_greg.cards = [Card("Q", suit), Card("J", suit)]
    assert player_greg.count_points() == 20
    player_greg.cards = [Card("A", suit), Card("J", suit)]
    assert player_greg.count_points() == 21


def test_check_count_points_with_as():
    """
    Test for checking count_points method with AS card. In all cases at least one card is AS
    """
    player = Player("Ignacy")
    player.cards = [Card("A", suit), Card("A", suit)]
    assert player.count_points() == 21
    player.cards = [Card("K", suit), Card("A", suit)]
    assert player.count_points() == 21
    player.cards = [Card("2", suit), Card("A", suit)]
    assert player.count_points() == 13
    player.cards = [Card("10", suit), Card("A", suit)]
    assert player.count_points() == 21
    player.cards = [Card("A", suit), Card("J", suit)]
    assert player.count_points() == 21
    player.cards = [Card("6", suit), Card("A", suit), Card("3", suit)]
    assert player.count_points() == 20
    player.cards = [Card("A", suit), Card("4", suit), Card("3", suit)]
    assert player.count_points() == 18
    player.cards = [Card("6", suit), Card("J", suit), Card("A", suit)]
    assert player.count_points() == 17
