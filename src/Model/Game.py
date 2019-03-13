from PieceColor import PieceColor
from PieceType import PieceType
from SimpleMove import SimpleMove
from EatMove import EatMove
from EnPassantCommand import EnPassantCommand
from PieceUpgradeCommand import PieceUpgradeCommand
from MoveWithSideEffects import MoveWithSideEffects 

class Game:
  def __init__(self, startingColor = PieceColor.LIGHT, aiColor = PieceColor.DARK ):
    self.startingColor = startingColor
    self.aiColor = aiColor
    self.turnColor = self.startingColor
    self.turnCount = 0
    self.init()

  def init(self):
    self.gameOver = False
    self.isDraw = False
    self.isCheckMate = False
    self.isCheck= False
    self.inCheck = None
    self.inCheckMate = None

    self.turnsEnabled = True
    self.multiPlayer = False
    self.aiEnabled = self.turnsEnabled and not self.multiPlayer
    self.playersEnabled = False
    if not self.playersEnabled:
      self.aiColor = self.startingColor

  def reset(self):
    self.turnColor = self.startingColor
    self.turnCount = 0
    self.init()

  def resetTurnCount(self):
    self.turnCount = 0

  def getTurnColor(self):
    return self.turnColor

  def getOpponentColor(self):
    if self.turnColor == PieceColor.LIGHT:
      return PieceColor.DARK
    else:
      return PieceColor.LIGHT

  def getTurnCount(self):
    return self.turnCount

  def getAIColor(self):
    return self.aiColor

  def getIsAITurn(self):
    return self.aiColor == self.turnColor

  def getIsAIEnabled(self):
    return self.aiEnabled

  def getPlayersEnabled(self):
    return self.playersEnabled

  def getTurnsEnabled(self):
    return self.turnsEnabled

  def getInCheckMate(self):
    return self.inCheckMate

  def getInCheck(self):
    return self.inCheck

  def getIsDraw(self):
    return self.isDraw

  def getIsCheckMate(self):
    return self.isCheckMate

  def getIsCheck(self):
    return self.isCheck

  def setGameOver(self, b):
    self.gameOver = b

  def toggleAIColor(self):
    self.aiColor = self.getOpponentColor()

  def isGameOver(self):
    return self.gameOver

  def advanceTurn(self):
    if self.turnColor == PieceColor.LIGHT:
      self.turnColor = PieceColor.DARK
    else:
      self.turnColor = PieceColor.LIGHT
    self.turnCount += 1

  def update(self, board, game, gameRules):
    self.init()

    kings = board.getKings()

    for color,king in kings.items():
      if gameRules.isInCheckMate( board, king.getPos() ):
        self.setGameOver( True )
        self.isCheckMate = True
        self.inCheckMate = king
        break
      if gameRules.isInCheck( board, king.getPos() ):
        self.isCheck = True
        self.inCheck = king
        break

    if gameRules.isDraw( board, game, kings[ PieceColor.LIGHT ].getPos(), 
                         kings[ PieceColor.DARK ].getPos() ):
      self.isDraw = True
      self.setGameOver( True )

  def checkToResetTurnCount(self, board, move ):
    innerMove = move
    if isinstance( move, MoveWithSideEffects ):
      innerMove = move.getMove()
    self.checkToResetTurnCountForPieceUpgrade( move )
    self.checkToResetTurnCountForEat( innerMove )
    self.checkToResetTurnCountForPonMovement( board, innerMove )

  def checkToResetTurnCountForPieceUpgrade(self, move):
    if isinstance( move, MoveWithSideEffects ):
      command = move.getCommand( 0 )
      if isinstance( command, PieceUpgradeCommand ):
        self.resetTurnCount()

  def checkToResetTurnCountForEat(self, move):
    if isinstance( move, EatMove ):
      self.resetTurnCount()

  def checkToResetTurnCountForPonMovement(self, board, move):
    if isinstance( move, SimpleMove ) or \
      isinstance( move, EnPassantCommand ):
      piece = board.getPiece( move.getEndPos() )
      if piece.getType() == PieceType.PON:
        self.resetTurnCount()
