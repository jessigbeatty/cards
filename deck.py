import random

class Deck:
    """a standard deck of playing cards"""
    def __init__(self):
        self.cards = []

        # creates ordered deck
        suits = ["spades", "clubs", "diamonds", "hearts"]
        for suit in suits:
            for i in range(1,14):
                self.cards.append(Card(suit, i))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def show_all(self):
        for card in self.cards:
            card.show()

    def count(self):
        print(len(self.cards))

class Card:
    """an individual card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")
