from Piece import Piece
from PieceType import PieceType

class Knight( Piece ):
  def __init__(self, color, stepLimit = 1):
    super().__init__( color, stepLimit )
    self.movementVectors = { ( 1, 2 ), ( 2, 1 ), ( -1, 2 ), ( -2, 1 ), ( 1, -2 ), ( 2, -1 ), ( -1, -2 ), ( -2, -1 ) }

  def __str__(self):
    return "N"

  def getType(self):
    return PieceType.KNIGHT
