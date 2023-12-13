from .HumanPlayer import HumanPlayer

class SetPlayer:
    """
    Player Factory type
    """
    def set_type_player(self, color, player_type, board):
        if (player_type == "human"):
            return HumanPlayer(color, board)

        # only human implemented rn