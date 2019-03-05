class RelativeColor:
  def __init__(self):
    pass

  def getColor(self, color, offset):
    r, g, b = color
    rOffset, gOffset, bOffset = offset
    return self.getColorUnit( r, rOffset ), self.getColorUnit( g, gOffset ),\
             self.getColorUnit( b, bOffset )

  def getColorUnit(self, colorUnit, offset):
    colorUnit += offset

    if colorUnit > 255:
      colorUnit = 255
    elif colorUnit < 0:
      colorUnit = 0

    return colorUnit
