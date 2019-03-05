from Command import Command
from PieceType import PieceType
from EnPassantDirection import EnPassantDirection

class SetEnPassantCommand(Command):
  def __init__(self, board, currPos):
    self.board = board
    self.currPos = currPos

  def __repr__(self):
    return "SetEnPassantCommand(%s)" % ( str( self.currPos ) )

  def __eq__(self, other):
    if isinstance(other, SetEnPassantCommand):
      return ( self.currPos == other.currPos )
    else:
      return False

  def __hash__(self):
    return hash( self.__repr__() )

  def execute(self):
    currX, currY = self.currPos
    self.checkToSetEnPassant( ( currX - 1, currY ), EnPassantDirection.RIGHT )
    self.checkToSetEnPassant( ( currX + 1, currY ), EnPassantDirection.LEFT )

  def undo(self):
    currX, currY = self.currPos
    self.checkToSetEnPassant( ( currX - 1, currY ), EnPassantDirection.NONE )
    self.checkToSetEnPassant( ( currX + 1, currY ), EnPassantDirection.NONE )
    self.board.clearCanEnPassant()
    
  def checkToSetEnPassant(self, pos, d):
    if self.board.isValidMove( pos ):
      piece = self.board.getPiece( pos )
      currPiece = self.board.getPiece( self.currPos )
      if piece is not None and piece.getType() == PieceType.PON and\
        piece.getColor() != currPiece.getColor():
        piece.setCanEnPassant( d )
        self.board.registerCanEnPassant( piece )
