## dealer.py

from card import Card

class Dealer:
    def __init__(self):
        """Initializes a dealer with an empty hand."""
        self.hand = []

    def hit(self, card: Card):
        """Adds a card to the dealer's hand.

        Args:
            card (Card): The card to add to the hand.
        """
        self.hand.append(card)

    def calculate_score(self) -> int:
        """Calculates the score of the dealer's hand.

        Returns:
            int: The score of the hand.
        """
        score = 0
        ace_count = 0
        value_map = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 10, 'Q': 10, 'K': 10, 'A': 11
        }

        for card in self.hand:
            score += value_map[card.value]
            if card.value == 'A':
                ace_count += 1

        # Adjust for aces if score is over 21
        while score > 21 and ace_count:
            score -= 10
            ace_count -= 1

        return score
