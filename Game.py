from board_config.Board import Board
from board_moves.Move import Move
from player.Player import Player
from player.PlayerManager import SetPlayer

class Santorini:
    """
    combines all classes to set up the Santorini game
    """
    def __init__(self):
        self._board = Board()
        self._white = "white"
        self._blue = "blue"
        self._white_player_index = 0
        self._blue_player_index = 1
        self._players = [Player(none,none)] # an array of type Player
        # self._players.append(Player(self.white_player))
        # self._players.append(Player(self.blue_player))
        self._player_setting = SetPlayer()
        # set player type using the manager
        self._players[self._white_player_index] = self._player_settings.set_type_player(self._white, self._white_player_index, self._board)

        self._players[self._blue_player_index] = self._player_settings.set_type_player(self._blue, self._blue_player_index, self._board)
        self._turn_count = 0


    # TODO - idk how to do this tbh
    def track_turns(self, curr_player):
        # get the current player, return next turn
        # array of array of turns
        if current_player._get_type == "white"
            
            string = f'Next Turn: {}'

        
        

    def _switch_player(self):
        curr_player = self._players[self._curr_player_index]
        next_player = self._players[1 - self._curr_player_index]
        return next_player

    def execute_move(self):