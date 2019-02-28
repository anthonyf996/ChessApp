from MoveController import MoveController
from ConsoleInputController import ConsoleInputController
from ConsoleInputReader import ConsoleInputReader
from GameExitException import GameExitException
from ConsoleClock import ConsoleClock

class Controller:
  def __init__(self, View, Model):
    self.View = View
    self.Model = Model
    self.board = Model.getBoard()
    self.Clock = ConsoleClock( fpsSpec = { "FPS" : 60 } )
    self.MoveController = MoveController()
    self.InputController = ConsoleInputController( ConsoleInputReader( { "getCurrPos" : self.MoveController.getCurrPos } ) )

  def run(self):
    try:
      while True:
        self.updateView()

        pos = self.InputController.pollUserInput()

        self.MoveController.handleInput( self.board, pos )

        self.Clock.tick()
    except GameExitException as e:
      print( e )
    finally:
      self.finish()

  def finish(self):
    pass

  def updateView(self):
    moves = self.MoveController.getMoves()

    if moves is None:
      self.View.display( self.board )
    else:
      self.View.display( self.board, moves )
