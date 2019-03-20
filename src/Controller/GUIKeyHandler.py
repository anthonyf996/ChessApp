from KeyHandler import KeyHandler
import pygame

class GUIKeyHandler(KeyHandler):
  def __init__(self, Game, MoveController, HintManager):
    super().__init__( Game, MoveController, HintManager )

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
        if self.Game.getIsMultiplayer():
          self.MoveController.undoLastMove( self.Game )
        # Single player. Undo AI's move too.
        else:
          self.MoveController.undoLastMove( self.Game )
          self.MoveController.undoLastMove( self.Game )
