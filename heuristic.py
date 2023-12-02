from deck import suits, faces, Deck, Card



# the point of this heuristic is to get the high values, higher the better
# I want the lower scores to be more frequent
def get_high_heuristic(hand, trump):
    heuristic = 0

    # reward lower hand counts
    if len(hand) == 0:
        return 1000
    else:
        heuristic += (100 / len(hand))

    # trump cards
    for card in hand:
        if card.suit == trump.suit:
            heuristic += 15

    # count the amount of double, triples, and quadruples you have
    count = {}
    for card in hand:
        if card.face in count:
            count[card.face] += 1
        else:
            count[card.face] = 1

    # higher cards
    # prioratize higher cards more than lower cards and average out that number
    # prioritize having multiples of cards, but more for the cards that are higher
    total = 0
    for cards in count.items():
        total += (faces.index(cards[0]) ** 1.5) * cards[1]

    heuristic += (total / len(hand))

    return int(heuristic)


# the point of this one is to get values closest to zero, so big positive and negative numbers are bad
def get_low_heuristic():
    pass
