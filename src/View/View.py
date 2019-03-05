class View:
  def __init__(self):
    pass

  def finish(self):
    raise NotImplementedError

  def display(self, board, game, moves = set()):
    raise NotImplementedError
