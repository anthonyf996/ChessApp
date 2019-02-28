from Piece import Piece
from EnPassantCommand import EnPassantCommand

class Pon( Piece ):
  def __init__(self, color, stepLimit = 1):
    super().__init__( color, stepLimit )
    self.movementVectors = { ( 0, 1 ) }
    self.canEnPassant = False

  def __str__(self):
    return "P"

  def getCanEnPassant(self):
    return self.canEnPassant

  def setCanEnPassant(self, b):
    self.canEnPassant = b

  def getMovementVectors(self):
    extraMoves = set()

    if not self.getHasMoved():
      extraMoves.add( ( 0, 2 ) )

    if not self.getHasMoved() and self.getCanEnPassant():
      extraMoves = extraMoves.union( { ( 1, 1 ), ( -1, 1 ) } )

    return self.movementVectors.union( extraMoves )

  def getEatVectors(self):
    return { ( 1, 1 ), ( -1, 1 ) }

  def getSpecialMoves(self, board, currPos):
    moves = set()

    moves = self.tryToGetEnPassantMove( board, currPos, moves )

    return moves

  def tryToGetEnPassantMove(self, board, currPos, moves):
    if self.getCanEnPassant():
      currX, currY = currPos
      leftPos = ( currX - 1, currY )
      rightPos = ( currX + 1, currY )

      if board.getPiece( leftPos ) is not None:
        moves.add( EnPassantCommand( board, currPos, leftPos ) )
      if board.getPiece( rightPos ) is not None:
        moves.add( EnPassantCommand( board, currPos, rightPos ) )

    return moves
