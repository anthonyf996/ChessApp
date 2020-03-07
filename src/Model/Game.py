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
    self.turnCount = 0 # Used by the MoveHistory class in the Controller/ directory to implement the undo feature
    self.gameTurnCount = 0
    self.gameCount = 0
    self.drawCount = 0
    self.paused = False
    self.defaultPlayersEnabled = True
    self.defaultMultiplayer = False
    self.testing = False
    self.successfulMove = False
    self.init()
    if not self.playersEnabled:
      self.paused = True

  def __str__(self):
    s = ""
    s += ( "-" * 38 ) + "\n"
    s += "TESTING:         %20s\n" % ( self.getIsTesting() )
    s += ( "-" * 38 ) + "\n"
    s += "GAME COUNT:      %20d\n" % ( self.getGameCount() )
    s += ( "-" * 38 ) + "\n"
    s += "DRAW COUNT:      %20d\n" % ( self.getDrawCount() )
    s += ( "-" * 38 ) + "\n"
    s += "CHECKMATE COUNT: %20d\n" % ( self.getGameCount() - self.getDrawCount() )
    s += ( "-" * 38 ) + "\n"
    if self.getGameCount() == 0:
      s += "DRAW PERCT:     %20d%%\n" % ( 0 )
      s += ( "-" * 38 ) + "\n"
      s += "CHECKMATE PERCT:%20d%%\n" % ( 0 )
      s += ( "-" * 38 ) + "\n"
    else:
      s += "DRAW PERCT:     %20d%%\n" % ( round( 100 * ( self.getDrawCount() / ( self.getGameCount() ) ) ) )
      s += ( "-" * 38 ) + "\n"
      s += "CHECKMATE PERCT:%20d%%\n" % ( round( 100 * ( ( self.getGameCount() - self.getDrawCount() ) / ( self.getGameCount() ) ) ) )
      s += ( "-" * 38 ) + "\n"
    s += "PAUSE:           %20s\n" % ( self.getIsPaused() )
    s += ( "-" * 38 ) + "\n"
    s += "MULTIPLAYER:     %20s\n" % ( self.getIsMultiplayer() )
    s += ( "-" * 38 ) + "\n"
    s += "PLAYERS ENABLED: %20s\n" % ( self.getPlayersEnabled() )
    s += ( "-" * 38 ) + "\n"
    s += "TURN NUM:        %20d\n" % ( self.getGameTurnCount() + 1 )
    s += ( "-" * 38 ) + "\n"
    s += "TURN:            %20s\n" % ( self.getTurnColor() )
    s += ( "-" * 38 ) + "\n"
    s += "CHECK:           %20s\n" % ( self.getIsCheck() )
    s += ( "-" * 38 ) + "\n"
    s += "DRAW:            %20s\n" % ( self.getIsDraw() )
    s += ( "-" * 38 ) + "\n"
    s += "CHECKMATE:       %20s\n" % ( self.getIsCheckMate() )
    s += ( "-" * 38 ) + "\n"
    s += "GAMEOVER:        %20s\n" % ( self.isGameOver() )
    s += ( "-" * 38 )
    return s

  def init(self):
    self.gameOver = False
    self.isDraw = False
    self.isCheckMate = False
    self.isCheck= False
    self.inCheck = None
    self.inCheckMate = None

    self.turnsEnabled = True
    self.multiplayer = self.defaultMultiplayer
    self.playersEnabled = self.defaultPlayersEnabled
    self.aiEnabled = self.turnsEnabled and not self.multiplayer
    if not self.playersEnabled:
      self.aiColor = self.startingColor
    else:
      self.aiColor = self.getOpponentColor( self.startingColor )
    
    if self.testing and self.gameOver:
      self.reset()

  def reset(self):
    self.aiColor = self.getOpponentColor( self.startingColor )
    self.turnColor = self.startingColor
    self.turnCount = 0
    self.gameTurnCount = 0
    self.gameCount = self.gameCount + 1
    if self.isDraw:
      self.drawCount = self.drawCount + 1
    self.paused = False
    if not self.testing:
      self.defaultPlayersEnabled = True
      self.defaultMultiplayer = False
    self.init()
    if not self.testing and not self.playersEnabled:
      self.paused = True
    if self.testing:
      print ( self )

  def resetTurnCount(self):
    self.turnCount = 0

  def getTurnColor(self):
    return self.turnColor

  def getOpponentColor(self, color):
    if color == PieceColor.LIGHT:
      return PieceColor.DARK
    else:
      return PieceColor.LIGHT

  def getGameTurnCount(self):
    return self.gameTurnCount

  def getTurnCount(self):
    return self.turnCount

  def getGameCount(self):
    return self.gameCount

  def getDrawCount(self):
    return self.drawCount

  def getIsPaused(self):
    return self.paused

  def getIsTesting(self):
    return self.testing

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

  def setSuccessfulMove(self, b):
    self.successfulMove = b

  #def toggleAIColor(self):
  #  self.aiColor = self.getOpponentColor( self.aiColor )

  def togglePause(self):
    self.paused = not self.paused

  def toggleMultiplayer(self):
    self.defaultMultiplayer = not self.defaultMultiplayer

  def togglePlayersEnabled(self):
    self.defaultPlayersEnabled = not self.defaultPlayersEnabled

  def toggleIsTesting(self):
    self.testing = not self.testing

  def isGameOver(self):
    return self.gameOver

  def advanceTurn(self):
    if self.turnColor == PieceColor.LIGHT:
      self.turnColor = PieceColor.DARK
    else:
      self.turnColor = PieceColor.LIGHT
    self.turnCount += 1
    self.gameTurnCount += 1

  def update(self, board, game, gameRules):
    self.init()

    if not self.successfulMove:
      return
    else:
      self.successfulMove = False

    kings = board.getKings()

    for color,king in kings.items():
      if gameRules.isInCheckMate( board, king.getPos() ):
        self.setGameOver( True )
        self.isCheckMate = True
        self.inCheckMate = king
        self.successfulMove = True
        break
      if gameRules.isInCheck( board, king.getPos() ):
        self.isCheck = True
        self.inCheck = king
        self.successfulMove = True
        break

    if gameRules.isDraw( board, game, kings[ PieceColor.LIGHT ].getPos(), 
                         kings[ PieceColor.DARK ].getPos() ):
      self.isDraw = True
      self.setGameOver( True )
      self.successfulMove = True

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
