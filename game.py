from deck import faces, Card
from itertools import product, combinations


def play_game(players, deck):
    winners = []

    setup_game(players, deck)
    skip = False

    attacker = 0
    while len(players) > 1:

        # skip turn if picked up
        if skip == True:
            skip = False
            attacker = (attacker + 1) % len(players)
            continue

        # get defender index
        defending_player = (attacker + 1) % len(players)
        attack_move = players[attacker].get_attack_move(get_player_hand_sizes(players), defending_player)
        defense_move = players[defending_player].get_defense_move(attack_move, get_player_hand_sizes(players), attacker)

        # this means the player picked up, and skips their next attack turn
        if defense_move == []:
            skip = True

        # shows the rest of the players which cards were played
        update_players_moves(players, attack_move, players[attacker].id)
        if defense_move == []:
            update_players_picked_up(players, attack_move, players[defending_player].id)
        else:
            update_players_moves(players, defense_move, players[defending_player].id)

        # pop off anyone who has run out of cards
        if players[attacker].is_finished():
            update_players_finished(players, players[attacker].id)
            winners.append(players.pop(attacker))
            attacker -= 1
            defending_player -= 1
        else:
            players[attacker].draw_hand(deck)

        if len(players) == 1:
            break

        if players[defending_player].is_finished():
            update_players_finished(players, players[defending_player].id)
            winners.append(players.pop(defending_player))
            attacker -= 1
            defending_player -= 1
        else:
            players[defending_player].draw_hand(deck)

        attacker = (attacker + 1) % len(players)

    print("Winner:", ', '.join(str(player.id) for player in winners))
    print("\nDurak:", ', '.join(str(player.id) for player in players))
    return [winners, players]

def update_players_moves(players, move, id):
    for p in players:
        p.update_cards_used(move, id)

def update_players_picked_up(players, move, id):
    for p in players:
        p.update_cards_picked_up(move, id)

def update_players_finished(players, player_id):
    for p in players:
        p.update_player_finished(player_id)

def setup_game(players, deck):
    for player in players:
        player.draw_hand(deck)

def get_player_hand_sizes(players):
    sizes = []
    for p in players:
        sizes.append(len(p.hand))

    return sizes

# has a bug where it doesn't do single cards, and sometimes does double cards where the second option is None
def get_valid_attack_moves(hand, defender_hand_size):
    valid_moves = []
    attack_size = min(4, defender_hand_size)

    # Group cards by face
    moves = {}
    for card in hand:
        moves.setdefault(card.face, []).append(card.copy())

    # Generate combinations for each face
    for cards in moves.values():
        for i in range(0, min(len(cards), attack_size) + 1):
            valid_moves.extend(combinations(cards, i))

    valid_moves = [combo for combo in valid_moves if None not in combo and len(combo) > 0]

    return valid_moves

def get_valid_defense_moves(hand, attack_hand, trump_suit):
    if len(attack_hand) > len(hand):
        print(attack_hand, hand)
        exit(0)

    valid_defense = [[] for _ in range(len(attack_hand))]
    # creates all possible cards that can defend against each card in each index
    for i, a_card in enumerate(attack_hand):
        for card in hand:
            if card.suit == trump_suit and a_card.suit != trump_suit:
                valid_defense[i].append(card.copy())
            elif faces.index(card.face) > faces.index(a_card.face) and (card.suit == a_card.suit):
                valid_defense[i].append(card.copy())

    # if any of the options are empty, return
    if any(len(options) == 0 for options in valid_defense):
        return [[]]

    # Generate all possible combinations
    valid_combinations = list(product(*valid_defense))

    # filter out combinations that have duplicates
    valid_combinations = [combo for combo in valid_combinations if len(set(combo)) == len(combo)]

    # change the tuples to lists
    valid_moves = [list(combo) for combo in valid_combinations]

    # add option to pick up attacking cards
    valid_moves.insert(0, [])

    return valid_moves
