from Piece import Piece
from PieceType import PieceType

class Bishop( Piece ):
  def __init__(self, color, stepLimit = 8):
    super().__init__( color, stepLimit )
    self.movementVectors = { ( 1, 1 ), ( -1, 1 ), ( 1, -1 ), ( -1, -1 ) }

  def __str__(self):
    return "%s%s" % ( self.getColorStr(), "B" )

  def getType(self):
    return PieceType.BISHOP
