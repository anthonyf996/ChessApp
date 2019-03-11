from PieceColor import PieceColor

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
