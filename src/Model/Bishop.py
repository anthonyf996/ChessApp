from Piece import Piece

class Bishop( Piece ):
  def __init__(self, color, stepLimit = 8):
    super().__init__( color, stepLimit )
    self.movementVectors = { ( 1, 1 ), ( -1, 1 ), ( 1, -1 ), ( -1, -1 ) }

  def __str__(self):
    return "B"
