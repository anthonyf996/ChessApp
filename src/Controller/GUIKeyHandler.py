from KeyHandler import KeyHandler
import pygame

class GUIKeyHandler(KeyHandler):
  def __init__(self, Game):
    super().__init__( Game )

  def handleKeyPress(self, k):
    if k == pygame.K_p:
      print ( "USER_INPUT_TOGGLE_PAUSE" )
      self.Game.togglePause()
    elif k == pygame.K_h:
      print ( "USER_INPUT_GET_HINT" )
