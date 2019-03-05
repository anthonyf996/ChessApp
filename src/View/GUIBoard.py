from GUITile import GUITile
from ColorPalette import ColorPalette
from PieceColor import PieceColor
from PieceType import PieceType
from SpriteSheet import SpriteSheet

class GUIBoard:
  def __init__(self, colorPalette, tileSize, numTiles, boardLabelSize, boardLabelFont):
    self.ColorPalette = colorPalette
    self.tileSize = tileSize
    self.numTiles = numTiles
    self.boardLabelSize = boardLabelSize
    self.boardLabelFont = boardLabelFont
    self.numRows = self.numTiles
    self.numCols = self.numTiles
    self.tiles = []

    self.initTiles()

  def initTiles(self):
    for y in range(0,self.numRows):
      row = []
      for x in range(0,self.numCols):
        color = self.getNextCheckeredPatternColor( y, x, self.ColorPalette.LIGHT_TILE_COLOR,
                                                   self.ColorPalette.DARK_TILE_COLOR )
        row.append( GUITile( x * self.tileSize + self.boardLabelSize, y * self.tileSize,
                             self.tileSize, self.tileSize, color ) )
      self.tiles.append( row )

  def getNextCheckeredPatternColor(self, row, col, color1, color2):
    if ( row % 2 ) == 0:
      if ( col % 2 ) == 0:
        color = color1
      else:
        color = color2
    else:
      if ( col % 2 ) == 0:
        color = color2
      else:
        color = color1

    return color

  def draw(self, display, spriteSheet, board):
    self.drawTiles( display )
    self.drawPieces( display, spriteSheet, board )

  def drawTiles(self, display):
    for row in self.tiles:
      for tile in row:
        tile.draw( display )

  def drawPieces(self, display, spriteSheet, board):
    for row in board:
      for piece in row:
        if piece is not None:
          x, y = piece.getPos()
          pieceType, color = piece.getType(), piece.getColor()
          spriteSheet.drawSprite( display, x * self.tileSize + self.boardLabelSize,
                                    y * self.tileSize, pieceType, color )
