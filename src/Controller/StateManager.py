class StateManager:
  def __init__(self):
    self.states = {}
    self.currState = None

  def getState(self, key):
    return self.states[ key ]

  def setState(self, key):
    self.currState = self.states[ key ]

  def reset(self):
    raise NotImplementedError
