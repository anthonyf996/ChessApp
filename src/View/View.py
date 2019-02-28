class View:
  def __init__(self):
    pass

  def display(self, board, moves = None):
    print( board.toString( moves ) )

  def getPos(self, prevPos):
    posX, posY = "", ""

    while not posX.isnumeric():
      posX = input( "Enter posX ( %s ):" % str( prevPos ) )
    while not posY.isnumeric():
      posY = input( "Enter posY ( %s ):" % str( prevPos ) )

    return int( posX[0] ), int( posY[0] )
