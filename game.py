from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.player_1 = Player("X")
        self.player_2 = Player("O")
        self.current_player = self.player_1.game_piece

    def alternate_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
