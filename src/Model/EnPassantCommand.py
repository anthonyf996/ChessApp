from Command import Command
from PieceColor import PieceColor
from MoveType import MoveType

class EnPassantCommand(Command):
  def __init__(self, board, ponPos, targetPos):
    self.board = board
    self.ponPos = ponPos
    self.targetPos = targetPos
    self.newPonPos = None
    self.target = None

  def __repr__(self):
    return "EnPassantCommand(%s,%s)" % ( str( self.ponPos ), str( self.targetPos ) )

  def __eq__(self, other):
    if isinstance(other, EnPassantCommand):
      return ( self.ponPos == other.ponPos and \
               self.targetPos == other.targetPos )
    else:
      return False

  def __hash__(self):
    return hash( self.__repr__() )

  def execute(self):
    pon = self.board.getPiece( self.ponPos )
    self.target = self.board.getPiece( self.targetPos )

    targetX, targetY = self.targetPos
    if pon.getColor() == PieceColor.LIGHT:
      self.newPonPos = ( targetX, targetY - 1 )
    else:
      self.newPonPos = ( targetX, targetY + 1 )
   
    self.board.addPiece( self.newPonPos, pon )
    self.board.removePiece( self.ponPos )
    self.board.removePiece( self.targetPos )

  def undo(self):
    pon = self.board.getPiece( self.newPonPos )

    self.board.addPiece( self.ponPos, pon )
    self.board.addPiece( self.targetPos, self.target )
    self.board.removePiece( self.newPonPos )

  def getMoveType(self):
    return MoveType.EAT

  def getPosPair(self):
    if self.newPonPos is not None:
      return self.ponPos, self.newPonPos

    pon = self.board.getPiece( self.ponPos )
    targetX, targetY = self.targetPos
    if pon.getColor() == PieceColor.LIGHT:
      self.newPonPos = ( targetX, targetY - 1 )
    else:
      self.newPonPos = ( targetX, targetY + 1 )
    return self.ponPos, self.newPonPos

  def getStartPos(self):
    start, end = self.getPosPair()
    return start

  def getEndPos(self):
    start, end = self.getPosPair()
    return end
