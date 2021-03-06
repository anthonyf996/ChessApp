from CastleCommand import CastleCommand
from PieceColor import PieceColor

class CastleLeftCommand(CastleCommand):
  def getKingNewPos(self):
    kingX, kingY = self.kingPos
    if self.board.getPiece( self.kingPos ).getColor() == PieceColor.LIGHT:
      return ( kingX - 2, kingY )
    else:
      return ( kingX + 2, kingY )

  def getRookPos(self):
    if self.board.getPiece( self.kingPos ).getColor() == PieceColor.LIGHT:
      return ( 0, self.board.getNumRows() - 1 )
    else:
      return ( self.board.getNumCols() - 1, 0 )

  def getRookNewPos(self):
    kingX, kingY = self.getKingNewPos()
    if self.board.getPiece( self.kingPos ).getColor() == PieceColor.LIGHT:
      return ( kingX + 1, kingY )
    else:
      return ( kingX - 1, kingY )

  def getPosPair(self):
    if self.kingNewPos is None:
      self.kingNewPos = self.getKingNewPos()
    return self.kingPos, self.kingNewPos

  def getStartPos(self):
    start, end = self.getPosPair()
    return start

  def getEndPos(self):
    start, end = self.getPosPair()
    return end
