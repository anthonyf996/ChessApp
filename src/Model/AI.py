from EatMove import EatMove
from PieceType import PieceType
from PieceColor import PieceColor
from CastleCommand import CastleCommand
from EnPassantCommand import EnPassantCommand
from MoveWithSideEffects import MoveWithSideEffects
from PieceUpgradeCommand import PieceUpgradeCommand 
import random

class AI:
  def __init__(self, Model, Board, Game):
    self.Model = Model
    self.Board = Board
    self.Game = Game
    self.encourageForwardMovementRate = 0.01
    self.encourageCastlingRate = 0.8
    self.FORWARD_MOVEMENT_WEIGHT = 20
    self.CASTLE_WEIGHT = 20
    self.EN_PASSANT_WEIGHT = 20
    self.UPGRADE_PIECE_WEIGHT = 20
    self.PLACE_IN_CHECK_WEIGHT = 20
    self.PLACE_IN_CHECKMATE_WEIGHT = 1000
    self.INCONSISTENT_STATE_WEIGHT = -10000

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
    weight = 0
    originalMove = move

    if random.random() <= self.encourageForwardMovementRate:
      weight += self.calculateForwardMovementScore( move, color )
    weight += self.calculateCaptureScore( board, move )
    weight += self.calculateProgressToUpgradePonScore( board, move, color )

    move = self.Board.checkToWrapMoveToUnsetEnPassant( move )

    self.performMove( move )

    #weight += self.calculateInconsistentStateScore( board, color)
    if board.isInInconsistentState( color ):
      self.undoMove( move )
      return ( self.INCONSISTENT_STATE_WEIGHT, None )

    if random.random() <= self.encourageCastlingRate:
      weight += self.calculateCastleScore( move )
    weight += self.calculateEnPassantScore( move )
    weight += self.calculateUpgradePieceScore( move )
    weight += self.calculatePlaceOpponentInCheckScore( game, color )
    weight += self.calculatePlaceOpponentInCheckMateScore( game, color )
    weight += self.calculateSacrificePieceScore( board, color )

    self.undoMove( move )

    return ( weight, originalMove )

  def calculateForwardMovementScore(self, move, color):
    x1, y1 = move.getStartPos()
    x2, y2 = move.getEndPos()
    if color == PieceColor.LIGHT:
      if ( y2 < y1 ):
        return self.FORWARD_MOVEMENT_WEIGHT
    else:
      if ( y2 > y1 ):
        return self.FORWARD_MOVEMENT_WEIGHT
    return 0

  def calculateCaptureScore(self, board, move):
    weight = 0
    if isinstance( move, EatMove ):
      target = board.getPiece( move.getEndPos() )
      weightsDict = { PieceType.QUEEN : 100, PieceType.ROOK : 80,
                      PieceType.BISHOP : 60, PieceType.KNIGHT : 40,
                      PieceType.PON : 20 }
      if target is not None:
        weight += self.getPieceTypeWeight( target, weightsDict )
    return weight

  def getPieceTypeWeight(self, piece, weightsDict):
    if piece.getType() not in weightsDict:
      return 0
    return weightsDict[ piece.getType() ]

  def calculateInconsistentStateScore(self, board, color):
    if board.isInInconsistentState( color ):
      return self.INCONSISTENT_STATE_WEIGHT
    return 0

  def calculateCastleScore(self, move):
    if isinstance( move, MoveWithSideEffects ):
      innerMove = move.getMove()
    else:
      innerMove = move
    if isinstance( innerMove, CastleCommand ):
      return self.CASTLE_WEIGHT
    return 0

  def calculateEnPassantScore(self, move):
    if isinstance( move, MoveWithSideEffects ):
      innerMove = move.getMove()
    else:
      innerMove = move
    if isinstance( innerMove, EnPassantCommand ):
      return self.EN_PASSANT_WEIGHT
    return 0

  def calculateProgressToUpgradePonScore(self, board, move, color):
    if board.getPiece( move.getStartPos() ).getType() == PieceType.PON:
      currPos = move.getStartPos()
      if board.isEmptyFile( currPos, color ):
        return self.calculateForwardMovementScore( move, color )
    return 0

  def calculateUpgradePieceScore(self, move):
    if isinstance( move, MoveWithSideEffects ):
      command = move.getCommand( 0 )
      if isinstance( command, PieceUpgradeCommand ):
        return self.UPGRADE_PIECE_WEIGHT
    return 0

  def calculatePlaceOpponentInCheckScore(self, game, color):
    if game.getIsCheck():
      if game.getInCheck().getColor() == game.getOpponentColor( color ):
        return self.PLACE_IN_CHECK_WEIGHT
    return 0

  def calculatePlaceOpponentInCheckMateScore(self, game, color):
    if game.getIsCheckMate():
      if game.getInCheckMate().getColor() == game.getOpponentColor( color ):
        return self.PLACE_IN_CHECKMATE_WEIGHT
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

    move = None
    if len( maxMoves ) > 0:
      move = maxMoves[ random.randint( 0, len( maxMoves ) - 1 ) ]

    return move
