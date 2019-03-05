class SpriteSheet:
  def __init__(self, img, indivSpriteWidth, indivSpriteHeight, spriteXArr, spriteYArr):
    self.img = img
    self.spriteWidth = indivSpriteWidth
    self.spriteHeight = indivSpriteHeight
    self.spriteXArr = spriteXArr
    self.spriteYArr = spriteYArr

  def drawSprite(self, display, dispX, dispY, spriteXIndex, spriteYIndex):
    spriteXPos, spriteYPos = self.spriteXArr[ spriteXIndex ] * self.spriteWidth,\
                             self.spriteYArr[ spriteYIndex ] * self.spriteHeight
    display.blit( self.img.getImg(), ( dispX, dispY ), ( spriteXPos, spriteYPos,\
                    self.spriteWidth, self.spriteHeight ) )
