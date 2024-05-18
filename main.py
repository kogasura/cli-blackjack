## main.py

from game import Game
from utils import display_message, get_user_input

class Main:
    @staticmethod
    def main():
        """Main function to start the Blackjack game."""
        while True:
            game = Game()
            game.start_game()
            replay = get_user_input("もう一度プレイしますか？ (y/n): ")
            if replay.lower() != 'y':
                display_message("ゲームを終了します。")
                break

if __name__ == "__main__":
    Main.main()
