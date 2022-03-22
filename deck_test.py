"""
Module to test Deck class
"""

from deck import Deck

talia_kart = Deck()


def test_check_all_card_quantity():
    """
    Test checks if all 52 cards exist in deck
    """
    assert len(talia_kart.cards) == 52


def test_check_quantity_values_cards():
    """
    Test checks if is correct quantity of cards from the same value
    """
    all_cards = [str(element) for element in range(2, 11)]
    [all_cards.append(element) for element in ["J", "Q", "K", "A"]]
    temp = [str(karta) for karta in talia_kart.cards]
    for karta in all_cards:
        assert temp.count(karta) == 4


def test_check_deck_length_after_hand_out_card():
    """
    Test checks if in deck there are correct number of cards after handing out some cards
    """
    deck = Deck()
    cards_quantity = 13
    for _ in range(cards_quantity):
        deck.hand_out()
    assert len(deck.cards) == (52 - cards_quantity)


def test_check_top_card():
    """
    Test checks if hand_out method takes top card (card from the top)
    """
    deck = Deck()
    deck.shuffle_deck()
    top_card = deck.cards[0]
    assert top_card == deck.hand_out()


def test_check_if_deck_is_empty():
    """
    Test checks if deck is empty after hand out 52 cards
    """
    deck = Deck()
    for _ in range(52):
        deck.hand_out()
    assert len(deck.cards) == 0
