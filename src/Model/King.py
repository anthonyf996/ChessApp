from Piece import Piece
from PieceType import PieceType
from PieceColor import PieceColor
from GetCollisionMovement import GetCollisionMovement
from CastleLeftCommand import CastleLeftCommand
from CastleRightCommand import CastleRightCommand 

class King( Piece ):
  def __init__(self, color, stepLimit = 1):
    super().__init__( color, stepLimit )
    self.movementVectors = { ( 1, 0 ), ( 0, 1 ), ( -1, 0 ), ( 0, -1 ), ( 1, 1 ), ( -1, 1 ), ( 1, -1 ), ( -1, -1 ) }

  def __str__(self):
    return "%s%s" % ( self.getColorStr(), "K" )

  def getType(self):
    return PieceType.KING

  def getSpecialMoves(self, board, currPos):
    moves = set()
    moves = self.tryToGetCastleMove(board, currPos, moves)
    return moves

  def tryToGetCastleMove(self, board, currPos, moves):
    if not board.isInDanger( currPos ):
      currPiece = board.getPiece( currPos )
      currX, currY = currPos

      if currPiece.getColor() == PieceColor.LIGHT:
        rightRookPos = board.getNumCols() - 1, currY
        leftRookPos = 0, currY
      else:
        leftRookPos = board.getNumCols() - 1, currY
        rightRookPos = 0, currY

      self.tryToAddCastleMove( board, moves, currPiece, leftRookPos, 
                                 CastleLeftCommand( board, currPos ) )
      self.tryToAddCastleMove( board, moves, currPiece, rightRookPos, 
                                 CastleRightCommand( board, currPos ) )
    return moves

  def tryToAddCastleMove(self, board, moves, currPiece, rookPos, castleCommand):
    rook = board.getPiece( rookPos )
    if rook is not None and not currPiece.getHasMoved() and not rook.getHasMoved():
      if currPiece.getPos() in GetCollisionMovement().getMoves( board, rook.getPos() ):
        if not ( board.stillInCheckAfterMove( currPiece, castleCommand ) or \
           board.stillInCheckAfterMove( rook, castleCommand ) ):
          moves.add( castleCommand )
    return moves
