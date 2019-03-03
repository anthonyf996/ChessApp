from Command import Command
from PieceType import PieceType

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
    pos = currX - 1, currY 
    if self.board.isValidMove( pos ):
      self.checkToSetEnPassant( self.board.getPiece( pos ), True )
    pos = currX + 1, currY 
    if self.board.isValidMove( pos ):
      self.checkToSetEnPassant( self.board.getPiece( pos ), True )

  def undo(self):
    currX, currY = self.currPos
    self.checkToSetEnPassant( self.board.getPiece( ( currX - 1, currY ) ), False )
    self.checkToSetEnPassant( self.board.getPiece( ( currX + 1, currY ) ), False )
    
  def checkToSetEnPassant(self, piece, b):
    if piece is not None and piece.getType() == PieceType.PON:
      piece.setCanEnPassant( b )
