from .HumanPlayer import HumanPlayer

class SetPlayer:
    """
    Player Factory type
    """
    def set_type_player(self, player_type, board, index):
        if (player_type == "human"):
            return HumanPlayer(index, board)

        # only human implemented rn