import random


def deckrand(shuffle=True):
    deck = []
    for i in range(2, 11):
        deck.append(str(i))
    deck.extend(['J', 'Q', 'K'])
    deck.insert(0, 'A')
    deck = 4 * deck
    for card in deck:
        if deck.index(card) <= 12:
            deck[deck.index(card)] = '♥' + card
        elif deck.index(card) <= 25:
            deck[deck.index(card)] = '♦' + card
        elif deck.index(card) <= 38:
            deck[deck.index(card)] = '♣' + card
        else:
            deck[deck.index(card)] = '♠' + card
    if shuffle:
        deck = random.sample(deck, 52)
    return deck


def decksort(deck):
    deck = [tuple for card in deckrand(False) for tuple in deck if tuple == card]
    return deck
