from deck import Deck

talia_kart = Deck()


def test_check_all_card_quantity():
    assert len(talia_kart.cards) == 52


def test_check_quantity_values_cards():
    all_cards = [str(element) for element in range(2, 11)]
    [all_cards.append(element) for element in ["J", "Q", "K", "A"]]
    temp = [str(karta) for karta in talia_kart.cards]
    print(temp)
    for karta in all_cards:
        # print(karta)
        assert temp.count(karta) == 4


def test_check_deck_length_after_hand_out_card():
    #TODO
    pass


def test_check_top_card():
    #TODO
    pass
