from Command import Command
from PieceType import PieceType
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen

class PieceUpgradeCommand(Command):
  def __init__(self, board, currPiecePos, upgradeType):
    self.board = board
    self.currPiecePos = currPiecePos
    self.currPiece = board.getPiece( currPiecePos )
    self.upgradeType = upgradeType

  def __repr__(self):
    return "PieceUpgradeCommand(%s,%s)" % ( str( self.currPiecePos ), str( upgradeType ) )

  def __eq__(self, other):
    if isinstance(other, PieceUpgradeCommand):
      return ( self.currPiecePos == other.currPiecePos and \
               self.upgradeType == other.upgradeType )
    else:
      return False

  def __hash__(self):
    return hash( self.__repr__() )

  def execute(self):
    newPiece = None

    if self.upgradeType == PieceType.KNIGHT:
      newPiece = Knight( self.currPiece.getColor() )
    elif self.upgradeType == PieceType.BISHOP:
      newPiece = Bishop( self.currPiece.getColor() )
    elif self.upgradeType == PieceType.ROOK:
      newPiece = Rook( self.currPiece.getColor() )
    elif self.upgradeType == PieceType.QUEEN:
      newPiece = Queen( self.currPiece.getColor() )

    self.board.addPiece( self.currPiecePos, newPiece )

  def undo(self):
    self.board.addPiece( self.currPiecePos, self.currPiece )

  def getStartPos(self):
    return self.currPiecePos

  def getEndPos(self):
    return self.getStartPos()
