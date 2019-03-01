from PieceColor import PieceColor

class Game:
  def __init__(self, startingColor = PieceColor.LIGHT):
    self.turnColor = startingColor
    self.gameOver = False
    self.isDraw = False
    self.isCheckMate = False
    self.isCheck= False
    self.turnsEnabled = False
    self.inCheck = None
    self.inCheckMate = None

  def getTurnColor(self):
    return self.turnColor

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
    if not self.gameOver:
      print ( "GAME OVER" )
    self.gameOver = b

  def isGameOver(self):
    return self.gameOver

  def update(self, board, gameRules):
    kings= board.getKings()

    lightKingPos = kings[ PieceColor.LIGHT ].getPos()
    darkKingPos = kings[ PieceColor.DARK ].getPos()

    for color,king in kings.items():
      if gameRules.isInCheckMate( board, king.getPos() ):
        self.setGameOver( True )
        self.isCheckMate = True
        self.inCheckMate = king
        break
      if gameRules.isInCheck( board, king.getPos() ):
        self.isCheck = True
        self.inCheck = king

    if gameRules.isDraw( board, lightKingPos, darkKingPos ):
      self.isDraw = True
      self.setGameOver( True )

  def advanceTurn(self):
    if self.turnColor == PieceColor.LIGHT:
      self.turnColor = PieceColor.DARK
    else:
      self.turnColor = PieceColor.LIGHT
