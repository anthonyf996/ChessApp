from PieceType import PieceType
from RelativeColor import RelativeColor
from GUIButton import GUIButton

class GUIUpgradeMenu:
  def __init__(self, w, h, x, y, pieceColor, menuColor):
    self.w = w
    self.h = h
    self.x = x
    self.y = y
    self.pieceColor = pieceColor
    self.menuColor = menuColor

    self.buttons = {}
    self.upgradeMenuButtonNames = [ PieceType.KNIGHT, PieceType.BISHOP,
                                    PieceType.ROOK, PieceType.QUEEN ]

  def addButton(self, unique_name, x, y, w, h):
    self.buttons[ unique_name ] = GUIButton( x, y, w, h )

  def removeButton(self, unique_name):
    del self.buttons[ unique_name ]

  def removeUpgradeMenuButtons(self):
    for name in self.upgradeMenuButtonNames:
      self.removeButton( name )

  def pollUpgradeMenuButtons(self, cursor):
    for name in self.upgradeMenuButtonNames:
      if name in self.buttons and self.buttons[ name ].isClicked( cursor ):
        return name
    return None

  def draw(self, display, spriteSheets, tileSize):
    x, y, w, h = self.x, self.y, self.w, self.h
    pieceColor, color = self.pieceColor, self.menuColor

    borderColor = RelativeColor().getColor( color, ( -10, -10, -10 ) )

    display.fill( borderColor, rect = [ x, y, w, h ] )
    display.fill( color, rect = [ x + 6, y + 6, w - 12, h - 12 ] )

    centerX, centerY = ( x + w // 2 ) - ( tileSize // 2 ), ( y + h // 2 ) - ( tileSize // 2 )
    padding = 15
    numPlaces = 4
    offsetX = ( w - ( numPlaces + 1 ) * padding ) // numPlaces

    spriteSheets[ "PIECES" ].drawSprite( display, x + ( 1 * padding ) + ( 0 * offsetX ), 
      centerY, PieceType.KNIGHT, pieceColor )
    spriteSheets[ "PIECES" ].drawSprite( display, x + ( 2 * padding ) + ( 1 * offsetX ), 
      centerY, PieceType.BISHOP, pieceColor )
    spriteSheets[ "PIECES" ].drawSprite( display, x + ( 3 * padding ) + ( 2 * offsetX ), 
      centerY, PieceType.ROOK, pieceColor )
    spriteSheets[ "PIECES" ].drawSprite( display, x + ( 4 * padding ) + ( 3 * offsetX ), 
      centerY, PieceType.QUEEN, pieceColor )

    self.addButton( self.upgradeMenuButtonNames[0], x + ( 1 * padding ) + ( 0 * offsetX ),
      centerY, tileSize, tileSize )
    self.addButton( self.upgradeMenuButtonNames[1], x + ( 2 * padding ) + ( 1 * offsetX ),
      centerY, tileSize, tileSize )
    self.addButton( self.upgradeMenuButtonNames[2], x + ( 3 * padding ) + ( 2 * offsetX ),
      centerY, tileSize, tileSize )
    self.addButton( self.upgradeMenuButtonNames[3], x + ( 4 * padding ) + ( 3 * offsetX ),
      centerY, tileSize, tileSize )
