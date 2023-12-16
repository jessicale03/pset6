from board_config.Board import Board
from board_moves.Move import MakeMoves
from player.Player import Player
from player.PlayerManager import SetPlayer
from copy import deepcopy

class Santorini:
    """
    combines all classes to set up the Santorini game
    Singleton design pattern since we are creating one instance of the game that isopen
    to reference
    """
    def __init__(self, white_type, blue_type, undo_redo, score):
        self._board = Board()
        # pass in the type of player (human, heursitics, random)
        self._white_type = white_type
        self._blue_type = blue_type
        self._undo_redo_setting = undo_redo
        self._score_setting = score
        self._white = "white"
        self._blue = "blue"
        self._white_player_index = 0
        self._blue_player_index = 1
        self._players = [Player(None, None) for _ in range(2)] # an array of type Player
        self._player_setting = SetPlayer()
        self._players[self._white_player_index] = self._player_setting.set_type_player(self._white_type, self._board, 0)
        self._players[self._blue_player_index] = self._player_setting.set_type_player(self._blue_type, self._board, 1)
        self._turn_count = 1
        self._curr_player = self._players[self._white_player_index] # start with white
        self._move_history = [] # save ALL MOVES
        self._score = 0
        self._undo_history_index = -1
        self._undo_history = [] # save all UNDOS
        self._history_index = 0 # start at turn one, used to move thru the history array
        # redo --> moves index back 1 to get the previous history item, returns that item 


    def _set_next_player(self):
        if self._curr_player._get_type() == "white":
            self._curr_player = self._players[self._blue_player_index]
        elif self._curr_player._get_type() == "blue":
            self._curr_player = self._players[self._white_player_index]

    def switch_turns(self):
        """
        switch the turn when called
        """
        if self._curr_player._get_type() == "white":
            self._set_next_player()
        elif self._curr_player._get_type() == "blue":
            self._set_next_player()
        self._turn_count += 1
    
    def switch_backwards_turns(self):
        """
        switch the turn when called
        """
        if self._curr_player._get_type() == "white":
            self._set_next_player()
        elif self._curr_player._get_type() == "blue":
            self._set_next_player()
        self._turn_count -= 1
    
    
    def display_turns(self):
        """
        display the turn
        """
        blue_height, blue_center, blue_distance = self._board.get_blue_scores()
        white_height, white_center, white_distance = self._board.get_white_scores()
        score_format1 = (blue_height, blue_center, blue_distance)
        score_format2 = (white_height, white_center, white_distance)
        if self._curr_player._get_type() == "white":
            print(f'Turn: {self._turn_count}, white (AB)', score_format2)

        elif self._curr_player._get_type() == "blue":
            
            print(f'Turn: {self._turn_count}, blue (YZ)', score_format1)
        # self._turn_count += 1

    def add_move_history(self, move):
        self._move_history.append(move)
        self._history_index += 1


    def undo(self, worker):
        # assume alr checked what the undo setting is on
        self._history_index -= 1
        # self._turn_count -= 1
        # add the moves 
        self._undo_history.append(self._move_history[self._history_index])
        # self._board = deepcopy(self._move_history[self._history_index - 1]) # recalling what is in the move_history
        self._move_history[self._history_index].oopsies_undo(worker, self._board)
        print(f"Undone to turn {self._history_index - 1}.")
        self.switch_backwards_turns()
        self._undo_history_index += 1
        
        # print(self._board)
        # self.display_turns()
        # print(self._turn_count)

    def redo(self, worker):

        # self._board = deepcopy(self._move_history[self._history_index - 1])
        # self._move_history[self._history_index].make_moves(worker, self.
        # _board)
        print("len", len(self._undo_history))
        print("index", self._undo_history_index)

        self._undo_history[self._undo_history_index].make_moves(worker, self._board)
        print(f"Redone to turn {self._undo_history_index}.")
        # self._turn_count += 1
        self.switch_turns()
        # print(self._board)
        # self.display_turns()
        
        # print(self._turn_count)

    def prompt_undo_redo(self, worker):
        command = input("undo, redo, or next\n")
        opponent = self._players[1 - worker._curr_player_index]
        if command == "undo" and self._history_index > 1:
            self.undo(worker) 
            self.make_moves()
            # print(self._board)
            # self.display_turns()
            # self.prompt_undo_redo(worker)
            return True

        elif command == "redo" and self._history_index < self._turn_count:
            self.redo(worker)
            self.make_moves()
            # print(self._board)
            # self.display_turns()
            # self.prompt_undo_redo(worker)
            return True
        elif command == "next":
            pass
        else:
            print("Invalid option. Please enter undo, redo, or next.")
            self.prompt_undo_redo(worker)


    def make_moves(self): #make Moves() object
        curr_player = self._curr_player
        print(self._board)
        self.display_turns()
        if self._undo_redo_setting == 'on':
            if self.prompt_undo_redo(curr_player) == True:
                exit
            # else: 
        opponent = self._players[1 - self._curr_player._curr_player_index] 
        if curr_player.type == "human":
            selected_worker = curr_player.get_worker()
            move_direction = curr_player.get_move_direction(selected_worker)
            build_direction = curr_player.get_build_direction(selected_worker, move_direction, opponent)

            move = MakeMoves(selected_worker, move_direction, build_direction)
            move.make_moves(selected_worker, self._board)

            move_string = f'{selected_worker}, {move_direction}, {build_direction}'
            print(move_string)
            self.switch_turns()
            # self.add_move_history(move_string)
            self.add_move_history(move)
            print(self._board)

        if curr_player.type == "random":
            random_worker = curr_player._get_random_worker()
            random_move = curr_player._get_random_move_direction(random_worker)
            print(f'get random move{random_move}')
            random_build = curr_player._get_random_build_direction(random_worker, random_move)

            move = MakeMoves(random_worker, random_move, random_build)
            move.make_moves(random_worker, self._board)
            move_string = f'{random_worker}, {random_move},{random_build}'
            print(move_string)
            self.switch_turns()
            print(self._board)





