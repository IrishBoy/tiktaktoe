import random
from game import GameSettings

class Minimax:
    def __init__(self):
        self.board = GameSettings()

    def alphabeta(self, node, player, alpha, beta):
        if node.complete_board():
            if node.X_won():
                return -1
            elif node.tied():
                return 0
            elif node.O_won():
                return 1
        else:
            for move in node.available_moves():
                node.make_move(move, player)
                val = self.alphabeta(node, self.board.set_enemy(player), alpha, beta)
                node.make_move(move, None)
                
                if player == 'O':
                    alpha = max(alpha, val)
                    if alpha >= beta:
                        return beta
                else:
                    beta = min(beta, val)
                    if beta <= alpha:
                        return alpha

        if player == 'O':
            return alpha
        else:
            return beta

    def determine(self, board, player):
        a = -2
        choices = []

        if len(board.available_moves()) == 9:
            return 4

        for move in board.available_moves():
            board.make_move(move, player)
            val = self.alphabeta(board, self.board.set_enemy(player), -2, 2)
            board.make_move(move, None)

            if val > a:
                a = val
                choices = [move]
            elif val == a:
                choices.append(move)

        return random.choice(choices)
