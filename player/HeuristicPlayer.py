from .Player import Player

class HeuristicPlayer(Player):
    """
    inherits from the abstract class
    represent heuristic player
    """
    def __init__(self, curr_player, board):
        super().__init__(curr_player, board)
