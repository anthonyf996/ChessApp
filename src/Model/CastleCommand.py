from Command import Command

class CastleCommand(Command):
  def __init__(self, board, kingPos):
    self.board = board
    self.kingPos = kingPos
    self.kingNewPos = None
    self.rookPos = None
    self.rookNewPos = None
    self.prevKingHasMoved = None
    self.prevRookHasMoved = None

  def __repr__(self):
    return "CastleCommand(%s)" % ( str( self.kingPos ) )

  def __eq__(self, other):
    if isinstance(other, CastleCommand):
      return ( self.kingPos == other.kingPos )
    else:
      return False

  def __hash__(self):
    return hash( self.__repr__() )

  def execute(self):
    self.kingNewPos = self.getKingNewPos()
    self.rookPos = self.getRookPos()
    self.rookNewPos = self.getRookNewPos()

    king = self.board.getPiece( self.kingPos )
    rook = self.board.getPiece( self.rookPos )

    self.prevKingHasMoved = king.getHasMoved()
    self.prevRookHasMoved = rook.getHasMoved()

    self.board.addPiece( self.kingNewPos, king )
    self.board.addPiece( self.rookNewPos, rook )
    self.board.removePiece( self.kingPos )
    self.board.removePiece( self.rookPos )

    king.setHasMoved( True )
    rook.setHasMoved( True )

  def undo(self):
    king = self.board.getPiece( self.kingNewPos )
    rook = self.board.getPiece( self.rookNewPos )

    self.board.addPiece( self.kingPos, king )
    self.board.addPiece( self.rookPos, rook )
    self.board.removePiece( self.kingNewPos )
    self.board.removePiece( self.rookNewPos )

    king.setHasMoved( self.prevKingHasMoved )
    rook.setHasMoved( self.prevRookHasMoved )

  def getPosPair(self):
    raise NotImplementedError

  def getKingNewPos(self):
    raise NotImplementedError

  def getRookPos(self):
    raise NotImplementedError

  def getRookNewPos(self):
    raise NotImplementedError
