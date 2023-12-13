from board_config.Board import Board
from board_moves.Move import MakeMoves
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
        self._turn_count = 1

        self._curr_player = self._players[self._white_player_index] # start with white

        # only necessary depending on which setting it is on
        if self._undo_setting_enabled == "on"
            self._move_history
            self._move_history_strings = []


    def _set_curr_player(self):
        if self._curr_player._type == "white":
            self._curr_player = self._players[self._blue_player_index]
        elif self._curr_player._type == "blue":
            self._curr_player = self._players[self._white_player_index]


    # TODO - idk how to do this tbh
    def track_turns(self, curr_player):
        # get the current player, return next turn
        # array of array of turns
        if current_player._get_type == "white"
            
            string = f'Next Turn: {}'


    # ONLY a human
    def make_moves(self): #make Moves() object
        curr_player = self._players[self._curr_player_index]
        opponent = self._players[1 - self._curr_player] 

        if opponent.has_won():
            print(opponent._type + " has won")

        # run CLI to get inputs if HUMAN PLAYER
        # if self._player_setting == "human":
        selected_worker = curr_player.get_worker(opponent)
        move_direction = curr_player.get_move_direction(selected_worker)
        build_direction = curr_player.get_build_direction(selected_worker, opponent)


        move = MakeMoves(selected_worker, move_direction, build_direction)
        move.make_moves(self._board)
        move_string = f'{worker}, {m_dir}, {b_dir}'

        self._move_history_strings.append(move_string)
        self._move_history.append(move)

        print(move_string)
        print(self._board)

        # check if the player has won
 

def 


