class Card():
    """
    class Card describes card object
    ToDo: karta jako krotka karta = (value, suit)
    """
    def __init__(self, value):
        self.value = value
        # self.suit = suit

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"{self.value}"
