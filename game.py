from numpy import copy
from deck import Deck


def play_game(players):
    deck = Deck()
    winners = []



def get_valid_attack_moves(hand, defender_hand_size):
    valid_moves = []
    attack_size = min(4, defender_hand_size)

    # sorts the cards by the face
    moves = {}
    for card in hand:
        if card.number not in moves:
            moves[card.number] = []

        moves[card.number].append(card.copy())

    # gets every substring of each face
    for key in moves.keys():
        size = min(attack_size, len(moves[key]))
        for i in range(len(moves[key])):
            for j in range(i, size):
                valid_moves.append(moves[key][i:j + 1])

    return valid_moves

