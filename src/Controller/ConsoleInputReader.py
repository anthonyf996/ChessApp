from InputReader import InputReader
from GameExitException import GameExitException

class ConsoleInputReader(InputReader):
  def read(self):
    return self.promptUserInput()

  def promptUserInput(self):
    posX, posY = "", ""

    while not posX.isnumeric():
      posX = input( "Enter posX or 'q' to quit ( %s ): " % ( str( self.callbacks[ "getCurrPos" ]() ) ) )
      self.checkToQuitGame( posX )
    while not posY.isnumeric():
      posY = input( "Enter posY or 'q' to quit ( ( %s, _ ) ): " % ( posX ) )
      self.checkToQuitGame( posY )

    return int( posX ), int( posY )

  def checkToQuitGame(self, coord):
    if coord.lower() == "q":
      raise GameExitException
