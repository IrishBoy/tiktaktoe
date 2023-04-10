from vars import *


class GameSettings:
    def __init__(self, squares=None):
        self.squares = squares or [None] * 9

    def show_board(self):
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print(element)

    def available_moves(self):
        return [k for k, v in enumerate(self.squares) if v is None]

    def complete_board(self):
        return None not in self.squares or self.winner() is not None

    def winner(self):
        for player in ('X', 'O'):
            positions = self.get_all_squares(player)
            for combo in self.WINNING_COMBOS:
                if all(pos in positions for pos in combo):
                    return player
        return None

    def get_all_squares(self, player):
        return [k for k, v in enumerate(self.squares) if v == player]

    def make_move(self, position, player):
        self.squares[position] = player

    def is_game_over(self):
        return self.complete_board()

    def get_game_result(self):
        if self.winner() == 'X':
            return 'X-win'
        elif self.winner() == 'O':
            return 'O-win'
        elif self.complete_board():
            return 'Draw'
        else:
            return None

    def get_enemy_symbol(self, player):
        return 'O' if player == 'X' else 'X'
