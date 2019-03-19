from KeyHandler import KeyHandler

class ConsoleKeyHandler(KeyHandler):
  def __init__(self, Game, HintManager):
    super().__init__( Game, HintManager )

  def handleKeyPress(self, k):
    if k == "h":
      print ( "USER_INPUT_GET_HINT" )
      self.HintManager.toggleHint()
    elif k == "h":
      print ( "USER_INPUT_UNDO_MOVE" )
