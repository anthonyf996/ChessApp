from Command import Command
from EnPassantDirection import EnPassantDirection

class UnsetEnPassantCommand(Command):
  def __init__(self, board, pons):
    self.board = board
    self.pons = pons
    self.EnPassantDirection = []

  def __repr__(self):
    return "UnsetEnPassantCommand(%s)" % ( str( self.pons ) )

  def __eq__(self, other):
    if isinstance(other, UnsetEnPassantCommand):
      return ( self.pons == other.pons )
    else:
      return False

  def __hash__(self):
    return hash( self.__repr__() )

  def execute(self):
    for i in range(0,len(self.pons)):
      self.EnPassantDirection.append( self.pons[ i ].getCanEnPassant() )
      self.pons[ i ].setCanEnPassant( EnPassantDirection.NONE )
    self.board.clearCanEnPassant()

  def undo(self):
    for i in range(0,len(self.pons)):
      self.pons[ i ].setCanEnPassant( self.EnPassantDirection[ i ] )
      self.board.registerCanEnPassant( pon )
