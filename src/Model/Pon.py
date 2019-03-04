from Piece import Piece
from EnPassantCommand import EnPassantCommand
from SetEnPassantCommand import SetEnPassantCommand
from SimpleMove import SimpleMove
from EatMove import EatMove
from MoveWithSideEffects import MoveWithSideEffects
from PieceColor import PieceColor
from PieceType import PieceType
from PieceUpgradeCommand import PieceUpgradeCommand
from GetSimpleMovement import GetSimpleMovement
from GetEatMovement import GetEatMovement

class Pon( Piece ):
  def __init__(self, color, stepLimit = 1):
    super().__init__( color, stepLimit )
    self.movementVectors = { ( 0, 1 ) }
    self.canEnPassant = False

  def __str__(self):
    return "P"

  def getType(self):
    return PieceType.PON

  def getCanEnPassant(self):
    return self.canEnPassant

  def setCanEnPassant(self, b):
    self.canEnPassant = b

  def getEatVectors(self):
    return { ( 1, 1 ), ( -1, 1 ) }

  def getMoves(self, board, currPos):
    moves = GetSimpleMovement().getMoves( board, currPos )
    return self.tryToGetUpgradeMoves( board, currPos, moves )

  def getEatMoves(self, board, currPos):
    moves = GetEatMovement().getMoves( board, currPos )
    return self.tryToGetUpgradeMoves( board, currPos, moves )

  def getSpecialMoves(self, board, currPos):
    moves = set()
    moves = self.tryToGetEnPassantMove( board, currPos, moves )
    moves = self.tryToGetDoubleMove( board, currPos, moves )
    return moves

  def tryToGetEnPassantMove(self, board, currPos, moves):
    if self.getCanEnPassant():
      currX, currY = currPos
      leftPos, rightPos = ( currX - 1, currY ), ( currX + 1, currY )
      self.tryToAddEnPassantMove( board, currPos, moves, leftPos )
      self.tryToAddEnPassantMove( board, currPos, moves, rightPos )
    return moves

  def tryToAddEnPassantMove(self, board, currPos, moves, pos):
    if board.isValidMove( pos ):
      if board.getPiece( pos ) is not None:
        moves.add( EnPassantCommand( board, currPos, pos ) )
    return moves

  def tryToGetDoubleMove(self, board, currPos, moves):
    if not self.getHasMoved():
      currX, currY = currPos
      if board.getPiece( currPos ).getColor() == PieceColor.LIGHT:
        endPos = ( currX, currY - 2 )
      else:
        endPos = ( currX, currY + 2 )

      if board.isValidMove( endPos ):
        moves.add( MoveWithSideEffects( SimpleMove( board, currPos, endPos ),
                   [ SetEnPassantCommand( board, endPos ) ] ) )
    return moves

  def tryToGetUpgradeMoves(self, board, currPos, moves):
    newMoves = set()
    for move in moves:
      move = self.tryToGetUpgradeMove( board, currPos, move )
      newMoves.add( move )
    return newMoves

  def tryToGetUpgradeMove(self, board, currPos, move):
    endX, endY = move.getEndPos()
    if endY == board.getNumRows() - 1 or endY == 0:
      return MoveWithSideEffects( move, [ PieceUpgradeCommand( board, 
                                            ( endX, endY ), PieceType.QUEEN ) ] )
    return move
