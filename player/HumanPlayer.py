from .Player import Player

class HumanPlayer(Player):
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


    def get_worker(self, opponent):
        # check if valid worker
        # check if the worker selected is theirs, 
        # check if there are available moves + build for that worker - build!!!
        selected_worker = input("Select a worker to move (A, B, Y, Z): ").
        if selected_worker not in self._valid_workers:
            print("Not a valid worker")
        elif selected_worker not in opponent.workers:
            print("This is not your worker")
        elif not self._board.check_valid_move_AND_buid(worker): # check build 
            print("There are no possible moves for this worker")

        else:
            return selected_worker

    def get_move_direction(self, worker):
        # check if valid direction
        # check if they can move in that direction
        direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw): ")

        if direction not in self._valid_directions:
            print("Not a valid direction.")

        elif not direction.valid_move(worker, direction):
            print("This worker is unable to move to " + direction)
        else:
            return direction

    
    def get_build_direction(self, worker, opponent):
        build_direction = input("Select a direction to build (n, ne, e, se, s, sw, w, nw): ")

        if build_direction not in self._valid_directions:
            print("Not a valid direction.")
        elif not build_direction.valid_move(worker, build_direction):
            print("This worker is unable to build in "+ build_direction)
        else:
            return build_direction
    