from Piece import Piece

class King( Piece ):
  def __init__(self, color, stepLimit = 1):
    super().__init__( color, stepLimit )
    self.movementVectors = [ ( 1, 0 ), ( 0, 1 ), ( -1, 0 ), ( 0, -1 ), ( 1, 1 ), ( -1, 1 ), ( 1, -1 ), ( -1, -1 ) ]
