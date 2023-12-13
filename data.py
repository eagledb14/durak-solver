from deck import Deck
from game import play_game
import random
from players.random_player import RandomPlayer
from players.naive_player import NaivePlayer
from players.naive_move_player import NaiveMovePlayer
results = {}

for i in range(10_000):
    d = Deck()

    players = [NaivePlayer(d.trump_card, 0), RandomPlayer(d.trump_card, 1)]
    random.shuffle(players)

    game_res = play_game(players, d)

    for player in game_res[0]:
        if player.id not in results:
            results[player.id] = 0
        else:
            results[player.id] += 1

for player, res in results.items():
    print(player, (res / 10_000) * 100)

