from deck import faces, Deck, Card


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

# this rates the move from the list of attacks, according to me, the programmer
def get_play_heuristic(move, trump_card):
    heuristic = 0

    # prioritize lengths with more cards
    if len(move) == 0:
        return 0

    heuristic += len(move) ** 2

    # priotitize getting rid of lower cards first
    total = 0
    for card in move:
        total += (len(faces) - faces.index(card.face)) * 3
    heuristic += (total / len(move))

    # we don't want to use trump cards if we don't have to
    for card in move:
        if card.suit == trump_card.suit:
            heuristic -= 5

    return int(heuristic)


