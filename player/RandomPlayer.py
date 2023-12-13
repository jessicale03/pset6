from .Player import Player

class RandomPlayer(Player):
    """
    inherits from the abstract class
    represent human player interacting from the terminal 
    """

    def __init__(self, curr_player, board):
        super().__init__(curr_player, board)
        # self._worker_input = "Select a worker to move (A, B, Y, Z): "
        # # self._move_input = "Select a direction to move (n, ne, e, se, s, sw, w, nw): "
        # self._direction_input = "Select a direction to build (n, ne, e, se, s, sw, w, nw)"
        self._valid_workers = {'A', 'B', 'Y', 'Z'}
        self._valid_directions = {'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'}
        