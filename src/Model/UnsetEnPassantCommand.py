from Command import Command

class UnsetEnPassantCommand(Command):
  def __init__(self, board, pons):
    self.board = board
    self.pons = pons

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
    for pon in self.pons:
      pon.setCanEnPassant( False )
    self.board.clearCanEnPassant()

  def undo(self):
    for pon in self.pons:
      pon.setCanEnPassant( True )
      self.board.registerCanEnPassant( pon )
