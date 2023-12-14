from .Player import Player
import random 

class RandomPlayer(Player):
    """
    inherits from the abstract class
    represent random player
    """

    def __init__(self, curr_player, board):
        super().__init__(curr_player, board)
        # self._random_worker = ''
        self.type = "random"


    # random worker
    def _get_random_worker(self):
        random_worker = random.choice(self.useable_workers())
        return random_worker

    # random move direction - called once worker is set
    def _get_random_move_direction(self, worker):
        random_move = random.choice(self.playable_moves(worker))
        return random_move

    # random build direction
    def _get_random_build_direction(self, worker):
        random_build = random.choice(self.playable_build(worker))
        return random_build

    # executable 
    def random_player_choice_str(self):
        random_worker = self._get_random_worker()
        random_move = self._get_random_move_direction(random_worker)
        random_build = self._get_random_build_direction(random_move)
        return (random_worker + "," + random_move + "," + random_build)