from Piece import Piece

class Pon( Piece ):
  def __init__(self, color, stepLimit = 1):
    super().__init__( color, stepLimit )
    self.movementVectors = [ ( 0, 1 ) ]
