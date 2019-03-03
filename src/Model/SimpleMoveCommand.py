from Command import Command

class SimpleMoveCommand(Command):
  def __init__(self, simpleMove):
    self.simpleMove

  def execute(self):
    self.simpleMove.perform()

  def undo(self):
   pass 
