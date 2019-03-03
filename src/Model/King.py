from Piece import Piece
from PieceColor import PieceColor
from GetCollisionMovement import GetCollisionMovement
from CastleLeftCommand import CastleLeftCommand
from CastleRightCommand import CastleRightCommand 

class King( Piece ):
  def __init__(self, color, stepLimit = 1):
    super().__init__( color, stepLimit )
    self.movementVectors = { ( 1, 0 ), ( 0, 1 ), ( -1, 0 ), ( 0, -1 ), ( 1, 1 ), ( -1, 1 ), ( 1, -1 ), ( -1, -1 ) }

  def __str__(self):
    return "K"

  def getSpecialMoves(self, board, currPos):
    moves = set()

    moves = self.tryToGetCastleMove(board, currPos, moves)

    return moves

  def tryToGetCastleMove(self, board, currPos, moves):
    currPiece = board.getPiece( currPos )
    currX, currY = currPos
    rightRookPos = board.getNumCols() - 1, currY
    leftRookPos = 0, currY
    rightRook = None
    leftRook = None

    if board.isInDanger( currPos ):
      return moves

    if currPiece.getColor() == PieceColor.DARK:
      temp = leftRookPos
      leftRookPos = rightRookPos
      rightRookPos = temp

    if board.isOccupied( rightRookPos ):
      rightRook = board.getPiece( rightRookPos )
    if board.isOccupied( leftRookPos ):
      leftRook = board.getPiece( leftRookPos )

    if leftRook is not None and not currPiece.getHasMoved() and not leftRook.getHasMoved():
      # Try to castle left
      if currPos in GetCollisionMovement().getMoves( board, leftRookPos ):
        castleCommand = CastleLeftCommand( board, currPos )
        if board.stillInCheckAfterMove( currPiece, castleCommand ) or \
           board.stillInCheckAfterMove( leftRook, castleCommand ):
          return moves
        moves.add( castleCommand )
    if rightRook is not None and not currPiece.getHasMoved() and not rightRook.getHasMoved():
      # Try to castle right
      if currPos in GetCollisionMovement().getMoves( board, rightRookPos ):
        castleCommand = CastleRightCommand( board, currPos )
        if board.stillInCheckAfterMove( currPiece, castleCommand ) or \
           board.stillInCheckAfterMove( rightRook, castleCommand ):
          return moves
        moves.add( castleCommand )

    return moves
