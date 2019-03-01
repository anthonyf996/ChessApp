from PieceColor import PieceColor

class Game:
  def __init__(self, startingColor = PieceColor.LIGHT):
    self.turnColor = startingColor
    self.gameOver = False
    self.enableTurns = False

  def getTurnColor(self):
    return self.turnColor

  def setGameOver(self, b):
    if not self.gameOver:
      print ( "GAME OVER" )
    self.gameOver = b

  def update(self, board, gameRules):
    kings= board.getKings()

    lightKingPos = kings[ PieceColor.LIGHT ].getPos()
    darkKingPos = kings[ PieceColor.DARK ].getPos()

    for color,king in kings.items():
      if gameRules.isInCheckMate( board, king.getPos() ):
        self.setGameOver( True )
        break

    if gameRules.isDraw( board, lightKingPos, darkKingPos ):
      self.setGameOver( True )

  def advanceTurn(self):
    if self.enableTurns:
      if self.turnColor == PieceColor.LIGHT:
        self.turnColor = PieceColor.DARK
      else:
        self.turnColor = PieceColor.LIGHT

  def isGameOver(self):
    return self.gameOver
