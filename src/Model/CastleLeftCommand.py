from CastleCommand import CastleCommand
from BoardOrientation import BoardOrientation

class CastleLeftCommand(CastleCommand):
  def getKingNewPos(self):
    kingX, kingY = self.kingPos

    if self.board.getOrientation() == BoardOrientation.LIGHT_TILE_RIGHT:
      return ( kingX - 2, kingY )
    else:
      return ( kingX + 2, kingY )

  def getRookPos(self):
    if self.board.getOrientation() == BoardOrientation.LIGHT_TILE_RIGHT:
      return ( 0, self.board.getNumRows() - 1 )
    else:
      return ( self.board.getNumCols() - 1, 0 )

  def getRookNewPos(self):
    kingX, kingY = self.getKingNewPos()
    if self.board.getOrientation() == BoardOrientation.LIGHT_TILE_RIGHT:
      return ( kingX + 1, kingY )
    else:
      return ( kingX - 1, kingY )
