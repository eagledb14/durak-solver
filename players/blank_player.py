from game import get_valid_attack_moves, get_valid_defense_moves
from heuristic import get_high_heuristic

class AbNaivePlayer:
    def __init__(self, trump_card, id):
        self.hand = []
        self.trump_card = trump_card
        self.id = id

    def get_attack_move(self, player_hand_sizes, defending_player_id):

    def get_defense_move(self, attack_hand, player_hand_sizes, attack_player_id):

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
        pass

    def update_cards_picked_up(self, cards, player_id):
        pass

    def update_player_finished(self, player_id):
        pass
