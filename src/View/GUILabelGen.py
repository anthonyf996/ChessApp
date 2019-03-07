import pygame

class GUILabelGen:
  def __init__(self, textSize, fontStr):
    self.textSize = textSize
    self.fontStr = fontStr
    self.font = pygame.font.SysFont( fontStr, textSize )

  def getLabel(self, textStr, textColor):
    return self.font.render( textStr, False, textColor )
