from InputReader import InputReader
from GameExitException import GameExitException
from GameResetException import GameResetException
from PieceColor import PieceColor

class ConsoleInputReader(InputReader):
  def read(self):
    return self.promptUserInput()

  def promptUserInput(self):
    posX, posY = "", ""
    turnStr = self.getTurnStr( self.callbacks[ "getTurnColor" ]() )

    while not posX.isnumeric():
      posX = input( "[ %s ] Enter posX or 'q' to quit ( %s ): " % ( turnStr, str( self.callbacks[ "getCurrPos" ]() ) ) )
      self.checkToQuitGame( posX )
      self.checkToResetGame( posX )
    while not posY.isnumeric():
      posY = input( "[ %s ] Enter posY or 'q' to quit ( ( %s, _ ) ): " % ( turnStr, posX ) )
      self.checkToQuitGame( posY )
      self.checkToResetGame( posY )

    return int( posX ), int( posY )

  def checkToQuitGame(self, coord):
    if coord.lower() == "q":
      raise GameExitException

  def checkToResetGame(self, coord):
    if coord.lower() == "r":
      raise GameResetException

  def getTurnStr(self, turnColor):
    if turnColor == PieceColor.LIGHT:
      return "LIGHT"
    else:
      return "DARK"