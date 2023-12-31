from dataclasses import dataclass
from functools import total_ordering
import random

suits = ['clubs', 'diamonds', 'heart', 'spades']
faces = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

class Deck:
    def __init__(self):
        self.reset()
        self.set_trump()

    def reset(self):
        self.cards = []
        for suit in suits:
            for face in faces:
                self.cards.append(Card(suit=suit, face=face))

    def set_trump(self):
        self.shuffle()
        trump = self.cards.pop()
        self.trump_card = trump
        self.cards.insert(0, trump)

        suits.remove(trump.suit)
        suits.insert(0, trump.suit)

    def draw(self, num):
        hand = []

        for _ in range(num):
            if len(self) == 0:
                break
            hand.append(self.cards.pop())

        return hand

    def sort(self):
        self.cards.sort()

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    # def __str__(self):
    #     string = ''
    #     for card in self.cards:
    #         string += f'{card}\n'
    #     return string


@dataclass(frozen=True)
@total_ordering
class Card:
    suit: str
    face: str

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return not self < other and not other < self

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        if self.suit == suits[0] and other.suit != suits[0]:
            return False
        if other.suit == suits[0] and self.suit != suits[0]:
            return True

        return faces.index(self.face) < faces.index(other.face)

    def __str__(self):
        return f'{self.face} of {self.suit}'

    def copy(self):
        return Card(suit=self.suit, face=self.face)
    
    def __hash__(self):
        return hash((self.suit, self.face))
        
