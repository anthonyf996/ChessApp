from InputReader import InputReader

class ConsoleInputReader(InputReader):
  def read(self):
    return self.promptUserInput()

  def promptUserInput(self):
    posX, posY = "", ""

    while not posX.isnumeric():
      posX = input( "Enter posX ( %s ): " % ( str( self.callbacks[ "getCurrPos" ]() ) ) )
    while not posY.isnumeric():
      posY = input( "Enter posY ( ( %s, _ ) ): " % ( posX ) )

    return int( posX ), int( posY )
