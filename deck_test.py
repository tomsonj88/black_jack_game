"""
Module to test Deck class
"""

from deck import Deck

deck_of_cards = Deck()
ALL_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def test_check_all_card_quantity():
    """
    Test checks if all 52 cards exist in deck
    """
    assert len(deck_of_cards.cards) == 52


def test_check_quantity_values_cards():
    """
    Test checks if is correct quantity of cards from the same value
    """
    temp = [str(karta) for karta in deck_of_cards.cards]
    for card in ALL_CARDS:
        assert temp.count(card) == 4


def test_check_deck_length_after_hand_out_card():
    """
    Test checks if in deck there are correct number of cards after handing out some cards
    """
    cards_quantity = 13
    for _ in range(cards_quantity):
        deck_of_cards.hand_out()
    assert len(deck_of_cards.cards) == (52 - cards_quantity)


def test_check_top_card():
    """
    Test checks if hand_out method takes top card (card from the top)
    """
    deck_of_cards.shuffle_deck()
    top_card = deck_of_cards.cards[0]
    assert top_card == deck_of_cards.hand_out()


def test_check_if_deck_is_empty():
    """
    Test checks if deck is empty after hand out 52 cards
    """
    deck = Deck()  # cannot use global deck_of_cards, should be new object, because here is needed a new deck of cards
    for _ in range(52):
        deck.hand_out()
    assert len(deck.cards) == 0
