from PieceColor import PieceColor
from PieceType import PieceType
from SimpleMove import SimpleMove
from EatMove import EatMove
from EnPassantCommand import EnPassantCommand
from PieceUpgradeCommand import PieceUpgradeCommand
from MoveWithSideEffects import MoveWithSideEffects 

class Game:
  def __init__(self, startingColor = PieceColor.LIGHT):
    self.startingColor = startingColor
    self.aiColor = self.getOpponentColor( self.startingColor )
    self.turnColor = self.startingColor
    self.turnCount = 0
    self.paused = False
    self.init()
    if not self.playersEnabled:
      self.paused = True

  def init(self):
    self.gameOver = False
    self.isDraw = False
    self.isCheckMate = False
    self.isCheck= False
    self.inCheck = None
    self.inCheckMate = None

    self.turnsEnabled = True
    self.multiplayer = False
    self.playersEnabled = False
    self.aiEnabled = self.turnsEnabled and not self.multiplayer
    if not self.playersEnabled:
      self.aiColor = self.startingColor

  def reset(self):
    self.turnColor = self.startingColor
    self.turnCount = 0
    self.paused = False
    if not self.playersEnabled:
      self.paused = True
    self.init()

  def resetTurnCount(self):
    self.turnCount = 0

  def getTurnColor(self):
    return self.turnColor

  def getOpponentColor(self, color):
    if color == PieceColor.LIGHT:
      return PieceColor.DARK
    else:
      return PieceColor.LIGHT

  def getTurnCount(self):
    return self.turnCount

  def getIsPaused(self):
    return self.paused

  def getAIColor(self):
    return self.aiColor

  def getIsAITurn(self):
    return self.aiColor == self.turnColor

  def getIsAIEnabled(self):
    return self.aiEnabled

  def getIsMultiplayer(self):
    return self.multiplayer

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

  def setTurnCount(self, count):
    self.turnCount = count

  def setTurnColor(self, color):
    self.turnColor = color

  #def toggleAIColor(self):
  #  self.aiColor = self.getOpponentColor( self.aiColor )

  def togglePause(self):
    self.paused = not self.paused

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
