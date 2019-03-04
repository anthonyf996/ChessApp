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
    self.checkToSetEnPassant( ( currX - 1, currY ), True )
    self.checkToSetEnPassant( ( currX + 1, currY ), True )

  def undo(self):
    currX, currY = self.currPos
    self.checkToSetEnPassant( ( currX - 1, currY ), False )
    self.checkToSetEnPassant( ( currX + 1, currY ), False )
    self.board.clearCanEnPassant()
    
  def checkToSetEnPassant(self, pos, b):
    if self.board.isValidMove( pos ):
      piece = self.board.getPiece( pos )
      if piece is not None and piece.getType() == PieceType.PON:
        piece.setCanEnPassant( b )
        self.board.registerCanEnPassant( piece )
