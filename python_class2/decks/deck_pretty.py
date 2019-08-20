from collections import namedtuple, UserList


TheCard = namedtuple("Card", ["rank", "suit"])

class Card(TheCard):

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


class CardDeck(UserList):

    """Class for creating a deck of cards, shuffling and dealing them."""

    # RANKS = [str(n) for n in range(2, 11)] + list("JQKA")
    RANKS = "2 3 4 5 6 7 8 9 10 Jack Queen King Ace".split()
    SUITS = ["Diamonds", "Clubs", "Hearts", "Spades"]

    def __init__(self):
        """Start deck with all 52 cards."""
        super().__init__([
            Card(rank, suit)
            for suit in self.SUITS
            for rank in self.RANKS
        ])

    def deal(self, num_cards=5):
        """Deals num_cards from deck. Returns list of cards."""
        return [self.data.pop() for dummy in range(num_cards)]


"""
from deck_pretty import CardDeck
cards = CardDeck()
import random
random.shuffle(cards)
cards[0]
hand = cards.deal()
for card in hand:
    print(card)

"""
