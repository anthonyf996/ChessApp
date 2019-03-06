class ControllerState:
  def __init__(self):
    pass

  def updateView(self):
    raise NotImplementedError

  def pollUserInput(self):
    raise NotImplementedError

  def updateModel(self, cursor):
    raise NotImplementedError
