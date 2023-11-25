from game import get_valid_attack_moves, get_valid_defense_moves

class HumanPlayer:
    def __init__(self, trump_card, id):
        self.hand = []
        self.trump_card = trump_card
        self.id = id

    def get_attack_move(self, player_hand_sizes, defending_player_id):
        self.print_board_information(player_hand_sizes, defending_player_id)

        valid_moves = get_valid_attack_moves(self.hand, player_hand_sizes[defending_player_id])
        valid_moves = sorted(valid_moves, key=lambda x: len(x))

        move = self.choose_move(valid_moves)
        self.update_hand(move)
        return move

    def get_defense_move(self, attack_hand, player_hand_sizes, attack_player_id):
        self.print_board_information(player_hand_sizes, attack_player_id, attacking_hand=attack_hand, attacking=False)
        valid_moves = get_valid_defense_moves(self.hand, attack_hand, self.trump_card.suit)

        move = self.choose_move(valid_moves)

        if len(move) == 0:
            self.hand.extend(attack_hand)
            return []

        self.update_hand(move)
        return move

    def choose_move(self, valid_moves):
        for i, move in enumerate(valid_moves):
            print(i, move)

        choice = -1
        while choice > len(valid_moves) or choice < 0:
            try:
                choice = int(input("Please choose a valid move: "))
            except Exception:
                pass

        print("-------------------------------------")
        return valid_moves[choice]


    def print_board_information(self, player_hand_sizes, other_id, attacking_hand=[], attacking=True):
        print("-------------------------------------")
        print(f'Player {self.id}')
        if attacking:
            print("Attacking: ", other_id)
        else:
            print("Defending Against: ", other_id)
            print("Their Attack: ", attacking_hand)

        print("\nPlayers hand sizes")
        for i, p in enumerate(player_hand_sizes):
            print(f'{i}:', p)

        print(f'\nTrump Card: {self.trump_card}')
        print()


    def draw_hand(self, deck):
        max_draw_size = 6
        # draw up to 6 cards
        drawn_cards = deck.draw(max(max_draw_size - len(self.hand), 0))
        self.hand.extend(drawn_cards)
        self.hand.sort()

    def update_hand(self, move):
        for card in move:
            self.hand.remove(card)

    def is_finished(self):
        return len(self.hand) == 0

    def update_cards_used(self, cards, player_id):
        print(f'Player {player_id} played:')
        for i in cards:
            print(i)
        print()
        pass

    def update_cards_picked_up(self, cards, player_id):
        print(f'Player {player_id} picked up:')
        for i in cards:
            print(i)
        print()
