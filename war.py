import deck
import player

# implements the game 'War'

# one turn
def play_turn():
    global pot; pot = []
    p1_played = player1.hand.pop()
    p2_played = player2.hand.pop()
    pot.append(p1_played)
    pot.append(p2_played)
    print("Player 1 plays: ", end='')
    p1_played.show()
    print("Player 2 plays: ", end='')
    # it breaks here on the second time through looping and i don't get whyyyy
    p2_played.show()
    return p1_played, p2_played

# compare card values
def compare(p1, p2):
    if p1.value > p2.value:
        print("Player 1 wins.")
        player1.hand.append(pot)
    elif p1.value < p2.value:
        print("Player 2 wins.")
        player2.hand.append(pot)
    else:
        print("This means WAR!!!")
        # implement WAR

player1 = player.Player()
player2 = player.Player()

my_deck = deck.Deck()

my_deck.shuffle()

# deals all the cards out
while len(my_deck.cards) != 0:
    player1.draw(my_deck)
    player2.draw(my_deck)

# plays hands in a loop
while len(player1.hand) != 0 and len(player2.hand) != 0:
    p1, p2 = play_turn()
    compare(p1, p2)

