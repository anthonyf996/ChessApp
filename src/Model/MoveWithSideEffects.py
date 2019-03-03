from MetaCommand import MetaCommand

class MoveWithSideEffects(MetaCommand):
  def __init__(self, move, commands):
    super().__init__(commands)
    self.move = move

  def __repr__(self):
    return "MoveWithSideEffects(%s,%s)" % ( self.getMove(), self.commands )

  def __eq__(self, other):
    if isinstance(other, MoveWithSideEffects):
      return ( self.getMove() == other.getMove() and \
               self.commands == other.commands )
    else:
      return False

  def __hash__(self):
    return hash( self.__repr__() )

  def execute(self):
    self.move.execute()
    for command in self.commands:
      command.execute()
    
  def undo(self):
    for command in self.commands:
      command.undo()
    self.move.undo()

  def getMove(self):
    return self.move

  def getPosPair(self):
    return self.move.getPosPair()

  def getStartPos(self):
    return self.move.getStartPos()

  def getEndPos(self):
    return self.move.getEndPos()
