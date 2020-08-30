import deck
import player

# implements the game 'War'

player1 = player.Player()
player2 = player.Player()

my_deck = deck.Deck()

my_deck.shuffle()

# deals all the cards out
while len(my_deck.cards) != 0:
    player1.draw(my_deck)
    player2.draw(my_deck)

# one turn
p1_played = player1.hand.pop()
p2_played = player2.hand.pop()
print("Player 1 plays: ", end='')
p1_played.show()
print("Player 2 plays: ", end='')
p2_played.show()

if p1_played.value > p2_played.value:
    print("Player 1 wins.")
elif p1_played.value < p2_played.value:
    print("Player 2 wins.")
else:
    print("This means WAR!!!")
