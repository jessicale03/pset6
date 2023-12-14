from .HumanPlayer import HumanPlayer
from .RandomPlayer import RandomPlayer
from .HeuristicPlayer import HeuristicPlayer

class SetPlayer:
    """
    Player Factory type
    """
    def set_type_player(self, player_type, board, index):
        if (player_type == "human"):
            return HumanPlayer(index, board)
        elif (player_type == "heuristic"):
            return HeuristicPlayer(index, board)
        elif (player_type == "random"):
            return RandomPlayer(index, board)

        # only human implemented rn