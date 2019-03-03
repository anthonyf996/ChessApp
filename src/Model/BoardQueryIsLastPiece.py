from BoardQuery import BoardQuery
from King import King

class BoardQueryIsLastPiece(BoardQuery):
  def __init__(self):
    super().__init__()
    self.default = True

  def shouldSkipPiece(self, subjectPiece, currPiece):
    if currPiece is None or isinstance( currPiece, King ):
      return True
    return False

  def query(self, board, subjectPos, currPos):
    piece = board.getPiece( currPos )
    if piece.getColor() == board.getPiece( subjectPos ).getColor():
      return True
    return False
