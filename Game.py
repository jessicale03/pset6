from board_config.Board import Board
from board_moves.Move import MakeMoves
from player.Player import Player
from player.PlayerManager import SetPlayer

class Santorini:
    """
    combines all classes to set up the Santorini game
    Singleton design pattern since we are creating one instance of the game that isopen
    to reference
    """
    def __init__(self, white_type, blue_type):
        self._board = Board()
        # pass in the type of player (human, heursitics, random)
        self._white_type = white_type
        self._blue_type = blue_type
        self._white = "white"
        self._blue = "blue"
        self._white_player_index = 0
        self._blue_player_index = 1
        self._players = [Player(None, None) for _ in range(2)] # an array of type Player
        # self._players.append(Player(self.white_player))
        # self._players.append(Player(self.blue_player))
        self._player_setting = SetPlayer()
        # set player type using the manager
        self._players[self._white_player_index] = self._player_setting.set_type_player(self._white, self._white_type, self._board)

        self._players[self._blue_player_index] = self._player_setting.set_type_player(self._blue, self._blue_type, self._board)
        self._turn_count = 1

        self._curr_player = self._players[self._white_player_index] # start with white


    def _set_next_player(self):
        if self._curr_player._type == "white":
            self._curr_player = self._players[self._blue_player_index]
        elif self._curr_player._type == "blue":
            self._curr_player = self._players[self._white_player_index]


    # TODO - idk how to do this tbh
    def track_turns(self, curr_player):
        # get the current player, return next turn
        # array of array of turns
        if curr_player._get_type == "white":
            string1 = "Turn: ", self._turn_count, "white (AB)"
            self._set_next_player()
        else:
            string2 = "Turn: ", self._turn_count, "blue (YZ)"
            self._set_next_player()
        self._turn_count += 1
        self.history_turns(curr_player, self._turn_count)
        if curr_player._get_type == "white":
            return string2
        else:
            return string1

    #todo: turns w the scores 

    def history_turns(self, curr_player, turn):
        self._make_moves

    def history_turns(self, curr_player, turn):
        self._make_moves 

    # ONLY a human
    def make_moves(self): #make Moves() object

        curr_player = self._curr_player
        opponent = self._players[1 - self._curr_player.curr_player_index] 

        if opponent._has_won():
            print(opponent._type + " has won")

        # run CLI to get inputs if HUMAN PLAYER
        # if self._player_setting == "human":
        selected_worker = curr_player.get_worker(opponent)
        move_direction = curr_player.get_move_direction(selected_worker)
        build_direction = curr_player.get_build_direction(selected_worker, opponent)


        move = MakeMoves(selected_worker, move_direction, build_direction)
        move.make_moves(self._board)
        move_string = f'{selected_worker}, {move_direction}, {build_direction}'

        self._move_history_strings.append(move_string)
        self._move_history.append(move)
        string_turns = self.track_turns()
        print(move_string)
        print(self._board)
        print(string_turns)

        # check if the player has won 



