## deck.py

import random
from card import Card

class Deck:
    def __init__(self):
        """Initializes a deck of 52 cards."""
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """Deals a card from the deck.

        Returns:
            Card: The card dealt from the deck.
        """
        if not self.cards:
            raise ValueError("All cards have been dealt")
        return self.cards.pop()
