from EatMove import EatMove
from PieceType import PieceType
from PieceColor import PieceColor
from CastleCommand import CastleCommand
from EnPassantCommand import EnPassantCommand
from MoveWithSideEffects import MoveWithSideEffects
from PieceUpgradeCommand import PieceUpgradeCommand 
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

  def getMove(self, color):
    weightedMoves = []
    for row in self.Board.getBoard():
      for piece in row:
        if piece is not None and piece.getColor() == color:
          for move in self.Board.getAllMoves( piece.getPos() ):
            weightedMoves.append( self.getWeightedMove( self.Board, self.Game, move, color ) )

    return self.getMaxMove( weightedMoves )

  def getWeightedMove(self, board, game, move, color):
    weight = self.calculateForwardMovementScore( move, color )
    weight += self.calculateCaptureScore( board, move )

    self.performMove( move )

    weight += self.calculateInconsistentStateScore( board, color)
    weight += self.calculateCastleScore( move )
    weight += self.calculateEnPassantScore( move )
    weight += self.calculateProgressToUpgradePonScore( board, move, color )
    weight += self.calculateUpgradePieceScore( move )
    weight += self.calculatePlaceOpponentInCheckScore( game, color )
    weight += self.calculatePlaceOpponentInCheckMateScore( game, color )
    weight += self.calculateSacrificePieceScore( board, color )

    self.undoMove( move )

    return ( weight, move )

  def calculateForwardMovementScore(self, move, color):
    weight = 0
    # Encourage forward movements randomly
    if random.random() <= self.encourageForwardMovementRate:
      x1, y1 = move.getStartPos()
      x2, y2 = move.getEndPos()
      if color == PieceColor.LIGHT:
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
      weightsDict = { PieceType.QUEEN : 100, PieceType.ROOK : 80,
                      PieceType.BISHOP : 60, PieceType.KNIGHT : 40,
                      PieceType.PON : 20 }
      weight += self.getPieceTypeWeight( target, weightsDict )
    return weight

  def getPieceTypeWeight(self, piece, weightsDict):
    if piece.getType() not in weightsDict:
      return 0
    return weightsDict[ piece.getType() ]

  def calculateInconsistentStateScore(self, board, color):
    if board.isInInconsistentState( color ):
      return -10000
    return 0

  def calculateCastleScore(self, move):
    if isinstance( move, MoveWithSideEffects ):
      innerMove = move.getMove()
    else:
      innerMove = move
    if isinstance( innerMove, CastleCommand ):
      return 20
    return 0

  def calculateEnPassantScore(self, move):
    if isinstance( move, MoveWithSideEffects ):
      innerMove = move.getMove()
    else:
      innerMove = move
    if isinstance( innerMove, EnPassantCommand ):
      return 20
    return 0

  def calculateProgressToUpgradePonScore(self, board, move, color):
    if board.getPiece( move.getEndPos() ).getType() == PieceType.PON:
      currPos = move.getEndPos()
      if board.isEmptyFile( currPos, color ):
        x1, y1 = move.getStartPos()
        x2, y2 = move.getEndPos()
        if color == PieceColor.LIGHT:
          if ( y2 < y1 ):
            return 20
        else:
          if ( y2 > y1 ):
            return 20
    return 0

  def calculateUpgradePieceScore(self, move):
    if isinstance( move, MoveWithSideEffects ):
      command = move.getCommand( 0 )
      if isinstance( command, PieceUpgradeCommand ):
        return 20
    return 0

  def calculatePlaceOpponentInCheckScore(self, game, color):
    if game.getIsCheck():
      if game.getInCheck().getColor() == game.getOpponentColor( color ):
        return 20
    return 0

  def calculatePlaceOpponentInCheckMateScore(self, game, color):
    if game.getIsCheckMate():
      if game.getInCheckMate().getColor() == game.getOpponentColor( color ):
        return 1000
    return 0

  def calculateSacrificePieceScore(self, board, color):
    weight = 0
    for row in self.Board.getBoard():
      for piece in row:
        if piece is not None and piece.getColor() == color:
          if board.isInDanger( piece.getPos() ):
            # Discourage losing own piece
            if board.isProtected( piece.getPos() ):
              weightsDict = { PieceType.QUEEN : 90, PieceType.ROOK : 70,
                              PieceType.BISHOP : 60, PieceType.KNIGHT : 50,
                              PieceType.PON : 40 }
              weight -= self.getPieceTypeWeight( piece, weightsDict )
            # Further discourage losing own piece without protection
            else:
              weightsDict = { PieceType.QUEEN : 120, PieceType.ROOK : 100,
                              PieceType.BISHOP : 80, PieceType.KNIGHT : 60,
                              PieceType.PON : 40 }
              weight -= self.getPieceTypeWeight( piece, weightsDict )
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

    if len( maxMoves ) == 0:
      move = None
    else:
      move = maxMoves[ random.randint( 0, len( maxMoves ) - 1 ) ]

    return move
