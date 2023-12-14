from .Player import Player

class HumanPlayer(Player):
    """
    inherits from the abstract class
    represent human player interacting from the terminal 
    """

    def __init__(self, curr_player_index, board):
        super().__init__(curr_player_index, board)
        # self._worker_input = "Select a worker to move (A, B, Y, Z): "
        # # self._move_input = "Select a direction to move (n, ne, e, se, s, sw, w, nw): "
        # self._direction_input = "Select a direction to build (n, ne, e, se, s, sw, w, nw)"
        # self._board = board
        # self.curr_player = curr_player
        # if self.curr_player == "white":
        #     self.curr_player_index = 0
        # else:
        #     self.curr_player_index = 1
        self._valid_workers = {'A', 'B', 'Y', 'Z'}
        self._valid_directions = {'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'}


    def get_worker(self, opponent):
        while True:
            selected_worker = input("Select a worker to move\n")

            if selected_worker not in self._valid_workers:
                print("Not a valid worker")
                continue
            elif selected_worker not in self._workers:
                print("This is not your worker")
                continue
            elif not self._board.check_valid_move_AND_buid(selected_worker): 
                print("There are no possible moves for this worker")
                continue
            else:
                break  # Exit the loop if the right input is provided

        return selected_worker

    def get_move_direction(self, worker):
        # check if valid direction
        # check if they can move in that direction
        
        # direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")

        # if direction not in self._valid_directions:
            # print("Not a valid direction.")

        # elif not self._board.is_valid_direction(worker, direction):
            # print("This worker is unable to move to " + direction)
        # else:
            # return direction
        while True:
            direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)      \n")

            if direction not in self._valid_directions:
                print("Not a valid direction.")
                continue  # Continue to the next iteration of the loop
            # elif not self._board.is_valid_direction(worker, direction):
            #     print("valid? ", self._board.is_valid_direction(worker, direction))
            #     print(f"This worker is unable to move to {direction}")
            else:
                break  # Exit the loop if the right input is provided
        return direction


    
    def get_build_direction(self, worker, opponent):
        while True:
            build_direction = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")

            if build_direction not in self._valid_directions:
                print("Not a valid direction.")
                continue  # Continue to the next iteration of the loop
            # elif not self._board.is_valid_direction(worker, build_direction):
            #     print(f"This worker is unable to move to {build_direction}")
            else:
                break  # Exit the loop if the right input is provided
        return build_direction

    