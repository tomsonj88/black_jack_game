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
    the_highest = 50        # because two cards go to player, when object is initialized
    for _ in range(5):
        card_quantity = randint(1, the_highest)
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
    card_quantity = 50
    cards = gracz_vanessa.take_cards(card_quantity)
    assert len(cards) == card_quantity


def test_check_count_points():
    player_greg = Player("Greg")
    player_greg.cards =[Card("2"), Card("K")]
    assert player_greg.count_points() == 12
    player_greg.cards = [Card("10"), Card("K"), Card("9")]
    assert player_greg.count_points() == 29
    player_greg.cards = [Card("3"), Card("7")]
    assert player_greg.count_points() == 10
    player_greg.cards = [Card("Q"), Card("J")]
    assert player_greg.count_points() == 20
#     # cards = [Card("A"), Card("J")]
#     # assert player_greg.count_points(cards) == 20


def test_check_count_points_with_as():
    player = Player("Ignacy")
    player.cards = [Card("A"), Card("A")]
    assert player.count_points() == 21
    player.cards = [Card("K"), Card("A")]
    assert player.count_points() == 21
    player.cards = [Card("2"), Card("A")]
    assert player.count_points() == 13
    player.cards = [Card("10"), Card("A")]
    assert player.count_points() == 21
    player.cards = [Card("A"), Card("J")]
    assert player.count_points() == 21
    player.cards = [Card("6"), Card("A"), Card("3")]
    assert player.count_points() == 20
    player.cards = [Card("A"), Card("4"), Card("3")]
    assert player.count_points() == 18
    player.cards = [Card("6"), Card("J"), Card("A")]
    assert player.count_points() == 17
