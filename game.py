## game.py

from deck import Deck
from player import Player
from dealer import Dealer
from utils import display_message, get_user_input

class Game:
    def __init__(self):
        """Initializes the game with a deck, player, and dealer."""
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game by dealing initial cards and managing turns."""
        display_message("ゲームを開始します。")
        self.deck.shuffle()
        
        # Deal initial cards
        for _ in range(2):
            self.player.hit(self.deck.deal_card())
            self.dealer.hit(self.deck.deal_card())
        
        self.player_turn()
        if self.player.calculate_score() <= 21:
            self.dealer_turn()
        
        self.check_winner()

    def player_turn(self):
        """Manages the player's turn."""
        while True:
            display_message(f"あなたの手札: {' '.join(map(str, self.player.hand))}, スコア: {self.player.calculate_score()}")
            if self.player.calculate_score() >= 21:
                break
            action = get_user_input("ヒットしますか？ (y/n): ")
            if action.lower() == 'y':
                self.player.hit(self.deck.deal_card())
            else:
                break

    def dealer_turn(self):
        """Manages the dealer's turn."""
        display_message(f"ディーラーの手札: {' '.join(map(str, self.dealer.hand))}, スコア: {self.dealer.calculate_score()}")
        while self.dealer.calculate_score() < 17:
            display_message("ディーラーがヒットしました。")
            self.dealer.hit(self.deck.deal_card())
            display_message(f"ディーラーの手札: {' '.join(map(str, self.dealer.hand))}, スコア: {self.dealer.calculate_score()}")

    def check_winner(self):
        """Checks and announces the winner of the game."""
        player_score = self.player.calculate_score()
        dealer_score = self.dealer.calculate_score()
        
        display_message(f"最終的なあなたのスコア: {player_score}")
        display_message(f"最終的なディーラーのスコア: {dealer_score}")
        
        if player_score > 21:
            display_message("あなたはバストしました。ディーラーの勝ちです。")
        elif dealer_score > 21 or player_score > dealer_score:
            display_message("あなたの勝ちです！")
        elif player_score < dealer_score:
            display_message("ディーラーの勝ちです。")
        else:
            display_message("引き分けです。")
