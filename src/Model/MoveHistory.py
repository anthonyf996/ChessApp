class MoveHistory:
  def __init__(self):
    self.moves = []

  def add(self, move):
    self.moves.append( move )

  def pop(self):
    if len( self.moves ) > 0:
      move = self.moves[-1]
      del self.moves[-1]
    else:
      move = None
    return move
