from KeyHandler import KeyHandler
import pygame

class GUIKeyHandler(KeyHandler):
  def __init__(self, Board, Game, MoveController, HintManager):
    super().__init__( Board, Game, MoveController, HintManager )

  def handleKeyPress(self, k):
    if k == pygame.K_p:
      print ( "USER_INPUT_TOGGLE_PAUSE ( %s )" % ( "ON" if ( not self.Game.getIsPaused() ) else "OFF" ) )
      self.Game.togglePause()
    elif k == pygame.K_m:
      print ( "USER_INPUT_TOGGLE_MULTIPLAYER ( %s )" % ( "ON" if ( not self.Game.getIsMultiplayer() ) else "OFF" ) )
      self.Game.toggleMultiplayer()
    elif k == pygame.K_a:
      print ( "USER_INPUT_TOGGLE_PLAYERS_ENABLED ( %s )" % ( "ON" if ( not self.Game.getPlayersEnabled() ) else "OFF" ) )
      self.Game.togglePlayersEnabled()
    elif k == pygame.K_s:
      print ( self.Game )
    elif k == pygame.K_h:
      if self.Game.getPlayersEnabled():
        print ( "USER_INPUT_GET_HINT" )
        self.HintManager.toggleHint()
    elif k == pygame.K_f:
      if self.Game.getPlayersEnabled():
        print ( "USER_INPUT_FOLLOW_HINT" )
        self.MoveController.performMove( self.Board, self.Game, self.HintManager.getHint() )
        self.HintManager.clearHint()
    elif k == pygame.K_u:
      if self.Game.getPlayersEnabled():
        print ( "USER_INPUT_UNDO_MOVE" )
        if self.Game.getIsMultiplayer():
          self.MoveController.undoLastMove( self.Game )
        # Single player. Undo AI's move too.
        else:
          self.MoveController.undoLastMove( self.Game )
          self.MoveController.undoLastMove( self.Game )
