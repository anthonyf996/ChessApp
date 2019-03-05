class GUIButton:
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h

  def isClicked(self, cursor):
    if cursor is not None:
      if self.x + self.w > cursor[0] > self.x and self.y + self.h > cursor[1] > self.y:
        return True
    return False
