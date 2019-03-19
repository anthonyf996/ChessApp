from KeyHandler import KeyHandler
import pygame

class GUIKeyHandler(KeyHandler):
  def __init__(self, Game, HintManager):
    super().__init__( Game, HintManager )

  def handleKeyPress(self, k):
    if k == pygame.K_p:
      print ( "USER_INPUT_TOGGLE_PAUSE" )
      self.Game.togglePause()
    elif k == pygame.K_h:
      if self.Game.getPlayersEnabled():
        print ( "USER_INPUT_GET_HINT" )
        self.HintManager.toggleHint()
    elif k == pygame.K_u:
      if self.Game.getPlayersEnabled():
        print ( "USER_INPUT_UNDO_MOVE" )
