import sys
from deck import Deck
from game import play_game
from players.random_player import RandomPlayer
from players.human_player import HumanPlayer
from players.naive_player import NaivePlayer
from players.naive_move_player import NaiveMovePlayer

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('Format: python main.py p1 p2 p3 p4')
        print('Player options: random, human, naive, nm')
        print('Min is 2 players, max is 4')
        exit(1)

    deck = Deck()

    players = []
    for i, player in enumerate(sys.argv[1:]):
        if player == 'random':
            players.append(RandomPlayer(deck.trump_card, i))
        elif player == 'human':
            players.append(HumanPlayer(deck.trump_card, i))
        elif player == 'naive':
            players.append(NaivePlayer(deck.trump_card, i))
        elif player == 'nm':
            players.append(NaiveMovePlayer(deck.trump_card, i))
        else:
            print(f'Unknown player: {player}, exiting')
            exit(1)

    if len(players) > 4:
        print('Too many players, max is 4, exiting')
        exit(1)

    print("\nGame starting: ")
    print("Players: ")
    for i, player in enumerate(players):
        print(f'{i}: {type(player).__name__}')
    print()

    play_game(players, deck)
