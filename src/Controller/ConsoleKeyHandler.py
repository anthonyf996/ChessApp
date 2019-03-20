from KeyHandler import KeyHandler

class ConsoleKeyHandler(KeyHandler):
  def __init__(self, Board, Game, MoveController, HintManager):
    super().__init__( Board, Game, MoveController, HintManager )

  def handleKeyPress(self, k):
    if k == "h":
      print ( "USER_INPUT_GET_HINT" )
      self.HintManager.toggleHint()
    elif k == "f":
      if self.Game.getPlayersEnabled():
        print ( "USER_INPUT_FOLLOW_HINT" )
        self.MoveController.performMove( self.Board, self.Game, self.HintManager.getHint() )
        self.HintManager.clearHint()
    elif k == "u":
      if self.Game.getPlayersEnabled():
        print ( "USER_INPUT_UNDO_MOVE" )
        if self.Game.getIsMultiplayer():
          self.MoveController.undoLastMove( self.Game )
        # Single player. Undo AI's move too.
        else:
          self.MoveController.undoLastMove( self.Game )
          self.MoveController.undoLastMove( self.Game )
