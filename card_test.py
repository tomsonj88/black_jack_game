"""
Test for Card class
"""
import pytest
from card import Card, InvalidValue, InvalidColor


def test_check_value():
    """ Test to check if good value was chosen"""
    card = Card("3", "c")
    assert card.value in card.possible_values


def test_check_color():
    """ Test to check if good color was chosen"""
    card = Card("5", "d")
    assert card.suit in card.possible_colors


def test_wrong_value_card():
    """ Test when invalid value was chosen and check if exception procedure will work"""
    with pytest.raises(InvalidValue) as message:
        Card("1", "s")
        assert message == "Wrong card value"


def test_wrong_color_card():
    """ Test when invalid color was chosen and check if exception procedure will work"""
    with pytest.raises(InvalidColor) as message:
        Card("A", "b")
        assert message == "Wrong card color"
