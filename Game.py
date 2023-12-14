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
        # self._players[self._white_player_index] = self._player_setting.set_type_player(self._white, self._white_type, self._board)

        # self._players[self._blue_player_index] = self._player_setting.set_type_player(self._blue, self._blue_type, self._board)
        self._players[self._white_player_index] = self._player_setting.set_type_player(self._white_type, self._board, 0)
        self._players[self._blue_player_index] = self._player_setting.set_type_player(self._blue_type, self._board, 1)

        self._turn_count = 1

        self._curr_player = self._players[self._white_player_index] # start with white


    # def _set_next_player(self):
    #     if self._curr_player._get_type() == "white":
    #         print("we made it!!!")
    #         self._curr_player = self._players[self._blue_player_index]
    #         self._curr_player = self._players[1]
    #         print(self._players[1].curr_player)
    #     elif self._curr_player._get_type() == "blue":
    #         self._curr_player = self._players[1 - self._white_player_index]
    #         self._curr_player = self._players[0]
            # self._curr_player._set_type(0)
    def _set_next_player(self):
        # print("color before: ", self._curr_player._get_type())
        if self._curr_player._get_type() == "white":
            self._curr_player = self._players[self._blue_player_index]
        elif self._curr_player._get_type() == "blue":
            self._curr_player = self._players[self._white_player_index]
        # print("color after: ", self._curr_player._get_type())


    # TODO - idk how to do this tbh
    def track_turns(self):
        # print()
        # get the current player, return next turn
        # array of array of turns
        # print("befpre set fxn", self._curr_player._get_type())
        if self._curr_player._get_type() == "white":
            
            print(f'Turn: {self._turn_count}, white (AB)')
            self._set_next_player()
        elif self._curr_player._get_type() == "blue":
            self._set_next_player()
            print(f'Turn: {self._turn_count}, blue (YZ)')
        self._turn_count += 1
        self.history_turns(self._curr_player, self._turn_count)

    def history_turns(self, curr_player, turn):
        # self.make_moves
        pass

    def history_turns(self, curr_player, turn):
        # self.make_moves 
        pass

    # ONLY a human
    def make_moves(self): #make Moves() object
        curr_player = self._curr_player
        self.track_turns()
        opponent = self._players[1 - self._curr_player._curr_player_index] 

        if curr_player._has_won():
            print(curr_player._type + " has won")

        # run CLI to get inputs if HUMAN PLAYER
        # if self._player_setting == "human":
        selected_worker = curr_player.get_worker(opponent)
        move_direction = curr_player.get_move_direction(selected_worker)
        build_direction = curr_player.get_build_direction(selected_worker, opponent)


        move = MakeMoves(selected_worker, move_direction, build_direction)
        move.make_moves(selected_worker, self._board)
        # self._board.build(selected_worker, build_direction)

        move_string = f'{selected_worker}, {move_direction}, {build_direction}'

        # self._move_history_strings.append(move_string)
        # self._move_history.append(move)
        # string_turns = self.track_turns()
        print(move_string)
        print(self._board)
        # print(string_turns)

        # check if the player has won 



