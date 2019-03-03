class MetaCommand:
  def __init__(self, commands):
    self.commands = commands

  def execute(self):
    raise NotImplementedError

  def undo(self):
    raise NotImplementedError
