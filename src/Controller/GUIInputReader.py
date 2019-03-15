import pygame
from InputReader import InputReader
from GameExitException import GameExitException
from GameResetException import GameResetException
from PieceColor import PieceColor
from PieceType import PieceType

class GUIInputReader(InputReader):
  def read(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        raise GameExitException
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          raise GameExitException
        elif event.key == pygame.K_r:
          raise GameResetException
        else:
          self.callbacks[ "handleKeyPress" ]( event.key )
      elif event.type == pygame.MOUSEBUTTONDOWN:
        cursor, click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        pos = self.callbacks[ "getPosPairFromCursor" ]( cursor )
        print( "Click: %s --> %s" % ( cursor, pos ) )
        return cursor
      return None
