class RandomActor:
  def __init__(self, board):
    self.board = board
    self.random_count = 0

  def random_action_func(self):
    self.random_count += 1
    return self.board.get_empty_pos()