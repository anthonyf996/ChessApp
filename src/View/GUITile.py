from RelativeColor import RelativeColor

class GUITile:
  BORDER_WIDTH_SIZE = 6
  BORDER_COLOR_OFFSET = 10

  def __init__(self, x, y, w, h, color):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.color = color
    self.origColor = color
    self.borderWSize = self.BORDER_WIDTH_SIZE
    self.borderHSize = self.borderWSize

  def setColor(self, c):
    self.color = c

  def resetColor(self):
    self.color = self.origColor

  def getBorderColor(self, color):
    return RelativeColor().getColor( color, ( self.BORDER_COLOR_OFFSET, 
                                              self.BORDER_COLOR_OFFSET, 
                                              self.BORDER_COLOR_OFFSET ) )

  def draw(self, display):
    x, y, w, h, color = self.x, self.y, self.w, self.h, self.color
    display.fill( color, rect = [ x, y, w, h ] )
    x, y, w, h, color = x + self.borderWSize, y + self.borderHSize,\
                        w - ( 2 * self.borderWSize ), h - ( 2 * self.borderHSize ),\
                        self.getBorderColor( color )
    display.fill( color, rect = [ x, y, w, h ] )
    self.resetColor()
