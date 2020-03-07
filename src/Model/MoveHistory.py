class MoveHistory:
  def __init__(self, Board):
    self.moves = []
    self.boardSnapshots = []
    self.Board = Board

  def add(self, move):
    self.moves.append( move )
    self.boardSnapshots.append( str( self.Board ) )

  def pop(self):
    if len( self.moves ) > 0:
      move = self.moves[-1]
      del self.moves[-1]
      del self.boardSnapshots[ -1 ]
    else:
      move = None
    return move

  # Returns last n snapshots. Defaults to 1.
  def getBoardSnapshot(self, n=1):
    return self.boardSnapshots[-n:]

  def reset(self):
    self.moves = []
    self.boardSnapshots = []
