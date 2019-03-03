from Piece import Piece
from PieceType import PieceType

class Rook( Piece ):
  def __init__(self, color, stepLimit = 8):
    super().__init__( color, stepLimit )
    self.movementVectors = { ( 1, 0 ), ( 0, 1 ), ( -1, 0 ), ( 0, -1 ) }

  def __str__(self):
    return "R"

  def getType(self):
    return PieceType.ROOK
