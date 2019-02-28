from MoveController import MoveController
from ConsoleInputController import ConsoleInputController
from ConsoleInputReader import ConsoleInputReader

class Controller:
  def __init__(self, View, Model):
    self.View = View
    self.Model = Model
    self.board = Model.getBoard()
    self.MoveController = MoveController()
    self.InputController = ConsoleInputController( ConsoleInputReader( { "getCurrPos" : self.MoveController.getCurrPos } ) )

  def run(self):
    while True:
      self.updateView()

      pos = self.InputController.pollUserInput()

      self.MoveController.handleInput( self.board, pos )

  def updateView(self):
    moves = self.MoveController.getMoves()

    if moves is None:
      self.View.display( self.board )
    else:
      self.View.display( self.board, moves )
