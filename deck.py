class Deck:
    """a deck of cards"""
    def __init__(self):
        pass

class Card:
    """an individual card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"the {self.value} of {self.suit}")

# making cards
suits = ["spades", "clubs", "diamonds", "hearts"]
cards = []
for suit in suits:
    for i in range(1,14):
        cards.append(Card(suit, i))

# show the cards you just created
for card in cards:
    card.show()

