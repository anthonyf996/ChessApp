from CastleCommand import CastleCommand
from BoardOrientation import BoardOrientation

class CastleRightCommand(CastleCommand):
  def getKingNewPos(self):
    kingX, kingY = self.kingPos

    if self.board.getOrientation() == BoardOrientation.LIGHT_TILE_RIGHT:
      return ( kingX + 2, kingY )
    else:
      return ( kingX - 2, kingY )

  def getRookPos(self):
    if self.board.getOrientation() == BoardOrientation.LIGHT_TILE_RIGHT:
      return ( self.board.getNumCols() - 1, self.board.getNumRows() - 1 )
    else:
      return ( 0, 0 )

  def getRookNewPos(self):
    kingX, kingY = self.getKingNewPos()
    if self.board.getOrientation() == BoardOrientation.LIGHT_TILE_RIGHT:
      return ( kingX - 1, kingY )
    else:
      return ( kingX + 1, kingY )
