from Piece import Piece

class Knight( Piece ):
  def __init__(self, color, stepLimit = 1):
    super().__init__( color, stepLimit )
    self.movementVectors = [ ( 1, 1 ), ( -1, 1 ), ( 1, -1 ), ( -1, -1 ) ]
