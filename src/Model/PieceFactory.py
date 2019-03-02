from PieceType import PieceType
from King import King
from Queen import Queen
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Pon import Pon

class PieceFactory:
  def __init__(self):
    pass

  def getPiece(self, color, pieceType):
    if pieceType == PieceType.KING:
      return King( color )
    elif pieceType == PieceType.QUEEN:
      return Queen( color )
    elif pieceType == PieceType.ROOK:
      return Rook( color )
    elif pieceType == PieceType.BISHOP:
      return Bishop( color )
    elif pieceType == PieceType.KNIGHT:
      return Knight( color )
    elif pieceType == PieceType.PON:
      return Pon( color )

    return None
