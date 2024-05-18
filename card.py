## card.py

class Card:
    def __init__(self, suit: str, value: str):
        """Initializes a card with a suit and a value.

        Args:
            suit (str): The suit of the card (e.g., 'Hearts', 'Diamonds', 'Clubs', 'Spades').
            value (str): The value of the card (e.g., '2', '3', '4', ..., '10', 'J', 'Q', 'K', 'A').
        """
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        """Returns a string representation of the card.

        Returns:
            str: The string representation of the card in the format 'Value of Suit'.
        """
        return f"{self.value} of {self.suit}"

    def __repr__(self) -> str:
        """Returns a formal string representation of the card.

        Returns:
            str: The formal string representation of the card.
        """
        return f"Card(suit='{self.suit}', value='{self.value}')"
