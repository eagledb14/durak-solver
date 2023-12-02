from game import get_valid_attack_moves, get_valid_defense_moves
from heuristic import get_high_heuristic
from copy import deepcopy

# chooses only the move that will get the next best hand
class NaivePlayer:
    def __init__(self, trump_card, id):
        self.hand = []
        self.trump_card = trump_card
        self.id = id

    def get_attack_move(self, player_hand_sizes, defending_player_id):
        valid_moves = get_valid_attack_moves(self.hand, player_hand_sizes[defending_player_id])

        # gets the values of each hand after making the move
        move_values = []
        for move in valid_moves:
            copy_hand = self.update_hand(deepcopy(self.hand), move)
            move_values.append([move, get_high_heuristic(copy_hand, self.trump_card)])

        
        move_values = sorted(move_values, key=lambda x: x[1])
        move = move_values[-1][0]
        self.hand = self.update_hand(self.hand, move)

        # gets the highest hand from this list
        return move

    def get_defense_move(self, attack_hand, player_hand_sizes, attack_player_id):
        valid_moves = get_valid_defense_moves(self.hand, attack_hand, self.trump_card.suit)

        move_values = []
        for move in valid_moves:
            copy_hand = self.update_hand(deepcopy(self.hand), move)
            move_values.append([move, get_high_heuristic(copy_hand, self.trump_card)])

        # add option for picking up
        copy_hand = deepcopy(self.hand)
        copy_hand.extend(attack_hand)
        move_values.append([[], get_high_heuristic(copy_hand, self.trump_card)])

        move_values = sorted(move_values, key=lambda x: x[1])
        move = move_values[-1][0]

        if move == []:
            self.hand.extend(attack_hand)
            return move

        self.hand = self.update_hand(self.hand, move)

        # gets the highest hand from this list
        return move

    def draw_hand(self, deck):
        max_draw_size = 6
        # draw up to 6 cards
        drawn_cards = deck.draw(max(max_draw_size - len(self.hand), 0))
        self.hand.extend(drawn_cards)
        self.hand.sort()

    def update_hand(self, hand, move):
        for card in move:
            hand.remove(card)
        return hand

    def is_finished(self):
        return len(self.hand) == 0

    def update_cards_used(self, cards, player_id):
        pass

    def update_cards_picked_up(self, cards, player_id):
        pass

    def update_player_finished(self, player_id):
        pass
