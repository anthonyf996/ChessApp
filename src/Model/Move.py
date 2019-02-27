class Move:
  def __init__(self, startPos, endPos):
    self.startPos = startPos
    self.endPos = endPos

  def __repr__(self):
    return "Move(%s,%s)" % ( self.getStartPos(), self.getEndPos() )

  def __eq__(self, other):
    if isinstance(other, Move):
      return ( self.getStartPos() == other.getStartPos() and \
               self.getEndPos() == other.getEndPos() )
    else:
      return False

  def __hash__(self):
    return hash( self.__repr__() )

  def getStartPos(self):
    return self.startPos

  def getEndPos(self):
    return self.endPos

  def getPosPair(self):
    return self.getStartPos(), self.getEndPos()
