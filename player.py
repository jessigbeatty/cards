import deck

class Player:
    """a card game player. has a "hand" and can draw cards into it"""

    def __init__(self):
        self.hand = []

    def draw(self, deck):
        """draws a card from the deck given as an argument"""
        drawn = deck.draw()
        self.hand.append(drawn)

    def show_hand(self):
        for card in self.hand:
            card.show()
