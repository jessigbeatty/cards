import random

class Card:
    """an individual card"""
    def __init__(self, suit, value, name):
        self.suit = suit
        self.value = value
        self.name = name

    def show(self):
        print(f"{self.name} of {self.suit}")

class Deck:
    """a standard deck of playing cards"""
    def __init__(self):
        self.cards = []
        Deck.build(self)

    def build(self):
        """builds a deck of standard cards and names the cards appropriately"""
        suits = ["spades", "clubs", "diamonds", "hearts"]
        for suit in suits:
            for i in range(1,14):
                self.cards.append(Card(suit, i, i))
        # assigning proper card names
        for card in self.cards:
            if card.value == 1:
                card.name = "ace"
            elif card.value == 11:
                card.name = "jack"
            elif card.value == 12:
                card.name = "queen"
            elif card.value == 13:
                card.name = "king"

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def show_all(self):
        for card in self.cards:
            card.show()

    def count(self):
        print(len(self.cards))
