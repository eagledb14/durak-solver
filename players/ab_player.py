from game import get_valid_attack_moves, get_valid_defense_moves
from heuristic import get_high_heuristic
from deck import suits, faces, Card, Deck
from copy import deepcopy

class AbNaivePlayer:
    def __init__(self, trump_card, id, num_players, deck):
        self.trump_card = trump_card
        self.id = id
        self.cards_left = deck
        self.hands = [[] for _ in range(num_players)]
        self.deck_size = 36 - (num_players * 6)

    def get_attack_move(self, player_hand_sizes, defending_player_id):
        valid_moves = get_valid_attack_moves(self.hands[self.id], player_hand_sizes[defending_player_id])

        best_value = -1000000
        best_move = valid_moves[0]
        for move in valid_moves:
            value = 0
            # value = self.ab_attack(deepcopy(self.hand), 3, move, player_hand_sizes, defending_player_id, deepcopy(self.player_cards), deepcopy(self.cards_left), self.deck_size, 1000, 1000, defending_player_id)
            if value > best_value:
                best_value = value
                best_move = move

        return best_move

    def ab_attack(self, hands, depth, move, cards_left, deck_size, a, b, id):
        if depth <= 0 or any(len(hand) == 0 for hand in hands):
            return get_high_heuristic(hands[self.id], self.trump_card)

        if id == self.id:
            v = -100000000
            valid_moves = []
            for move in valid_moves: 

                new_hand = self.update_hand(move, hands.copy())
                # new_player_hand_sizes = deepcopy(player_hand_sizes)
                # if deck_size == 0:
                    # new_player_hand_sizes[self.id] -= len(move)

                # v = max(v, self.ab_attack(new_hand, depth - 1, move, new_player_hand_sizes, , , , a, b, )
                a = max(a, v)
                if a >= b:
                    break

                return v

        else:
            v = 1000000
            valid_moves = []
            for move in valid_moves:

                b = min(b, v)
                if b <= a:
                    break

        return 0

    def get_defense_move(self, attack_hand, player_hand_sizes, attack_player_id):
        return []

    def draw_hand(self, deck):
        max_draw_size = 6
        # draw up to 6 cards
        drawn_cards = deck.draw(max(max_draw_size - len(self.hands[self.id]), 0))
        self.hands[self.id].extend(drawn_cards)
        self.hands[self.id].sort()
        self.deck_size = len(deck)

    def _draw_hand(self, hands, deck, id):
        max_draw_size = 6
        # draw up to 6 cards
        drawn_cards = deck.draw(max(max_draw_size - len(hands[id]), 0))
        hands[id].extend(drawn_cards)
        hands[id].sort()


    def update_hand(self, hand, move):
        for card in move:
            hand.remove(card)
        return hand


    def is_finished(self):
        return len(self.hands[self.id]) == 0

    def update_cards_used(self, cards, player_id):
        for card in cards:
            if card in self.hands[player_id]:
                self.hands.remove(card)
            self.cards_left.remove(card)

    def update_cards_picked_up(self, cards, player_id):
        for card in cards:
            self.hands[player_id].append(card)


    def update_player_finished(self, player_id):
        pass
