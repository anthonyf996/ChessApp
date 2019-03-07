from GUILabelGen import GUILabelGen

class GUIBoardLabel:
  def __init__(self, textSize, fontStr, textArr, textColor):
    self.textSize = textSize
    self.fontStr = fontStr
    self.textArr = textArr
    self.textColor = textColor
    self.labels = []

    labelGen = GUILabelGen( textSize, fontStr )

    for label in self.textArr:
      self.labels.append( labelGen.getLabel( label, textColor ) )

  def drawPanel(self, display, panelColor, x, y, w, h):
    display.fill( panelColor, rect = [ x, y, w, h ] )

  def drawLabels(self, display, xMult, xSum, yMult, ySum, centerX, centerY):
    x, y = 0, 0

    for i in range(0,len(self.labels)):
      xPos, yPos = x * xMult + xSum, y * yMult + ySum
      textRect = self.labels[ i ].get_rect( center = ( xPos + centerX,\
                                                       yPos + centerY ) )
      display.blit( self.labels[ i ], textRect )
      x, y = x + 1, y + 1
