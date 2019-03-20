from KeyHandler import KeyHandler

class ConsoleKeyHandler(KeyHandler):
  def __init__(self, Game, MoveController, HintManager):
    super().__init__( Game, MoveController, HintManager )

  def handleKeyPress(self, k):
    if k == "h":
      print ( "USER_INPUT_GET_HINT" )
      self.HintManager.toggleHint()
    elif k == "u":
      if self.Game.getPlayersEnabled():
        print ( "USER_INPUT_UNDO_MOVE" )
        if self.Game.getIsMultiplayer():
          self.MoveController.undoLastMove( self.Game )
        # Single player. Undo AI's move too.
        else:
          self.MoveController.undoLastMove( self.Game )
          self.MoveController.undoLastMove( self.Game )
