from EatMove import EatMove
from PieceType import PieceType
from PieceColor import PieceColor
import random

class AI:
  def __init__(self, Model, Board, Game, color):
    self.Model = Model
    self.Board = Board
    self.Game = Game
    self.color = color
    self.encourageForwardMovementRate = 0.01

  def performMove(self, move):
    move.execute()
    self.Model.update()

  def undoMove(self, move):
    move.undo()
    self.Model.update()

  def getMove(self):
    weightedMoves = []
    for row in self.Board.getBoard():
      for piece in row:
        if piece is not None and piece.getColor() == self.color:
          for move in self.Board.getAllMoves( piece.getPos() ):
            weightedMoves.append( self.getWeightedMove( self.Board, self.Game, move ) )

    return self.getMaxMove( weightedMoves )

  def getWeightedMove(self, board, game, move):
    weight = 0

    weight += self.calculateForwardMovementScore( move )
    weight += self.calculateCaptureScore( board, move )

    self.performMove( move )

    weight += self.calculateInconsistentStateScore( board )
    weight += self.calculatePlaceOpponentInCheckScore( game )
    weight += self.calculateSacrificePieceScore( board )

    self.undoMove( move )

    return ( weight, move )

  def calculateForwardMovementScore(self, move):
    weight = 0
    # Encourage forward movements randomly
    if random.random() <= self.encourageForwardMovementRate:
      x1, y1 = move.getStartPos()
      x2, y2 = move.getEndPos()
      if self.color == PieceColor.LIGHT:
        if ( y2 < y1 ):
          weight += 20
      else:
        if ( y2 > y1 ):
          weight += 20

    return weight

  def calculateCaptureScore(self, board, move):
    weight = 0
    if isinstance( move, EatMove ):
      target = board.getPiece( move.getEndPos() )
      if target.getType() == PieceType.QUEEN:
        weight += 100
      elif target.getType() == PieceType.ROOK:
        weight += 80
      elif target.getType() == PieceType.BISHOP:
        weight += 60
      elif target.getType() == PieceType.KNIGHT:
        weight += 40
      elif target.getType() == PieceType.PON:
        weight += 20
    return weight

  def calculateInconsistentStateScore(self, board):
    if board.isInInconsistentState( self.color ):
      return -10000
    return 0

  def calculatePlaceOpponentInCheckScore(self, game):
    if game.getIsCheck():
      if game.getInCheck().getColor() == game.getOpponentColor():
        return 20
    return 0

  def calculateSacrificePieceScore(self, board):
    weight = 0
    for row in self.Board.getBoard():
      for piece in row:
        if piece is not None and piece.getColor() == self.color:
          if board.isInDanger( piece.getPos() ):
            # Discourage losing own piece
            if board.isProtected( piece.getPos() ):
              #print ( "PROTECTED %s %s" % ( str( piece.getPos() ), piece.getType() ) )
              if piece.getType() == PieceType.QUEEN:
                weight -= 50
              elif piece.getType() == PieceType.ROOK:
                weight -= 40
              elif piece.getType() == PieceType.BISHOP:
                weight -= 30
              elif piece.getType() == PieceType.KNIGHT:
                weight -= 20
              elif piece.getType() == PieceType.PON:
                weight -= 10
            # Discourage losing own piece without protection
            else:
              #print ( "NOT PROTECTED %s %s" % ( str( piece.getPos() ), piece.getType() ) )
              if piece.getType() == PieceType.QUEEN:
                weight -= 100
              elif piece.getType() == PieceType.ROOK:
                weight -= 80
              elif piece.getType() == PieceType.BISHOP:
                weight -= 60
              elif piece.getType() == PieceType.KNIGHT:
                weight -= 40
              elif piece.getType() == PieceType.PON:
                weight -= 20

    return weight

  def getMaxMove(self, weightedMoves):
    maxWeight = -500
    maxMoves = []
    for weightedMove in weightedMoves:
      weight, move = weightedMove
      if weight > maxWeight:
        maxWeight = weight
        maxMoves = [ move ]
      elif weight == maxWeight:
        maxMoves.append( move )
    print( maxMoves )
    
    if len( maxMoves ) == 0:
      move = None
    else:
      move = maxMoves[ random.randint( 0, len( maxMoves ) - 1 ) ]
    print( move )
    return move
