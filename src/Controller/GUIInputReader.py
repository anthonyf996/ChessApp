import pygame
from InputReader import InputReader
from GameExitException import GameExitException
from GameResetException import GameResetException
from PieceColor import PieceColor
from PieceType import PieceType

class GUIInputReader(InputReader):
  def read(self):
    #return self.promptUserInput()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        raise GameExitException
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          raise GameExitException
        elif event.key == pygame.K_r:
          raise GameResetException
      elif event.type == pygame.MOUSEBUTTONDOWN:
        cursor, click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        pos = self.callbacks[ "getPosPairFromCursor" ]( cursor )
        print( "Click: %s --> %s" % ( cursor, pos ) )
        return cursor
      return None

  def promptUpgradeType(self, color):
    return self.callbacks[ "promptUpgradeType" ]( color )

  """
  def promptUserInput(self):
    posX, posY = "", ""
    turnStr = self.getTurnStr( self.callbacks[ "getTurnColor" ]() )

    posX = self.promptUserInputCoord( "[ %s ] Enter posX or 'q' to quit ( %s ): " % 
                                      ( turnStr, str( self.callbacks[ "getCurrPos" ]() ) ) )
    posY = self.promptUserInputCoord( "[ %s ] Enter posY or 'q' to quit ( ( %s, _ ) ): " % 
                                      ( turnStr, posX ) )

    return int( posX ), int( posY )

  def promptUserInputCoord(self, promptStr ):
    coord = ""
    while not coord.isnumeric():
      coord = input( promptStr )
      self.checkToRaiseException( coord )
    return coord

  def checkToRaiseException(self, coord):
    self.checkToQuitGame( coord )
    self.checkToResetGame( coord )

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

  def promptUpgradeType(self):
    upgradeType = ""
    while upgradeType.upper() not in [ "N", "B", "R", "Q" ]:
      print( "Pon Upgrade Selection" )
      upgradeType = input( "Enter corresponding letter ( N | B | R | Q ): " ).upper()

    if upgradeType == "N":
      return PieceType.KNIGHT
    elif upgradeType == "B":
      return PieceType.BISHOP
    elif upgradeType == "R":
      return PieceType.ROOK
    else:
      return PieceType.QUEEN
  """
