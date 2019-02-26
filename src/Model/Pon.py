from Piece import Piece

class Pon( Piece ):
  def __init__(self, color, stepLimit = 1):
    super().__init__( color, stepLimit )
    self.movementVectors = { ( 0, 1 ) }
    self.canEnPassant = False

  def getCanEnPassant(self):
    return self.canEnPassant

  def setCanEnPassant(self, b):
    self.canEnPassant = b

  def getExtraMoves(self):
    extraMoves = set()

    if not self.getHasMoved():
      extraMoves.add( ( 0, 2 ) )

    if not self.getHasMoved() and self.getCanEnPassant():
      extraMoves = extraMoves.union( { ( 1, 1 ), ( -1, 1 ) } )

    return extraMoves
