from BoardQuery import BoardQuery

class BoardQueryIsKingTrapped(BoardQuery):
  def __init__(self):
    super().__init__()
    self.default = True

  def shouldSkipPiece(self, subjectPiece, currPiece):
    if currPiece is None or currPiece.getColor() != subjectPiece.getColor():
      return True
    return False

  def query(self, board, subjectPos, currPos):
    if board.canStopCheck( currPos, board.getPiece( subjectPos ) ):
      return True
    return False
