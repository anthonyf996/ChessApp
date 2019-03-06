class InputReader:
  def __init__(self, callbacks):
    self.callbacks = callbacks

  def read(self):
    raise NotImplementedError
