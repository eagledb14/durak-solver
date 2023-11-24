from numpy import copy
from deck import Deck, faces
from itertools import product, combinations


def play_game(players):
    deck = Deck()
    winners = []


def get_valid_attack_moves(hand, defender_hand_size):
    valid_moves = []
    attack_size = min(4, defender_hand_size)

    # Group cards by face
    moves = {}
    for card in hand:
        moves.setdefault(card.face, []).append(card.copy())

    # Generate combinations for each face
    for cards in moves.values():
        for i in range(1, min(len(cards), attack_size) + 1):
            valid_moves.extend(combinations(cards, i))

    return valid_moves

def get_valid_defense_moves(hand, attack_hand, trump_suit):
    valid_defense = [[] for _ in range(len(attack_hand))]
    # creates all possible cards that can defend against each card in each index
    for i, a_card in enumerate(attack_hand):
        for card in hand:

            # if that face is too small, continue
            if faces.index(card.face) <= faces.index(a_card.face):
                continue

            # if the card is not either the same suit nor the trump suit, continue
            if card.suit != a_card.suit and card.suit != trump_suit:
                continue

            valid_defense[i].append(card.copy())

    # if any of the options are empty, return
    if any(len(options) == 0 for options in valid_defense):
        return []

    # Generate all possible combinations
    valid_combinations = list(product(*valid_defense))

    # change the tuples to lists
    valid_moves = [list(combo) for combo in valid_combinations]

    return valid_moves
