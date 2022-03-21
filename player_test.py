from player import Player
from random import randint


def test_quantity_of_take_cards():
    """
    Purpose of this test is to check if take_cards method return
    good quantity of cards. Using for loop it let check more
    function calls defined in for loop range. Quantity of cards
    is drawn by randint.
    """
    gracz = Player("Stefan")
    the_highest = 52
    for element in range(5):
        card_quantity = randint(0, the_highest)
        cards = gracz.take_cards(card_quantity)
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


# def test_check_if_deck_is_empty():
# TODO: consider to check here or in player test

#     player_pablo = Player("Pablo")
#     card_quantity = 52
#     cards = player_pablo.take_cards(card_quantity)
#     card_quantity = 1
#     cards = player_pablo.take_cards(card_quantity)

# def test_sum_of_taken_cards():
#     pass

# def test_check_count_points():
#     pass