# BLACKJACK

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random


def draw_card(deck):
    drawn_card = random.choice(cards)
    deck.append(drawn_card)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players_deck = []
players_deck_value = sum(players_deck)

dealers_deck = []
dealers_deck_value = sum(dealers_deck)

for i in range(2):
    draw_card(players_deck)
    draw_card(dealers_deck)

print(players_deck)
print(f"Value: {players_deck_value}")
print(dealers_deck)
print(f"Value: {dealers_deck_value}")
