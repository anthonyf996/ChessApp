from GUITile import GUITile
from ColorPalette import ColorPalette
from PieceColor import PieceColor
from PieceType import PieceType
from SpriteSheet import SpriteSheet
from GUIBoardLabel import GUIBoardLabel

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

    self.fileLabelsText = [ "a", "b", "c", "d", "e", "f", "g", "h" ]
    self.rankLabelsText = [ "1", "2", "3", "4", "5", "6", "7", "8" ]

    self.fileLabels = GUIBoardLabel( boardLabelSize, boardLabelFont,\
      self.fileLabelsText, self.ColorPalette.BOARD_LABEL_TEXT_COLOR )
    self.rankLabels = GUIBoardLabel( boardLabelSize, boardLabelFont,\
      self.rankLabelsText[::-1], self.ColorPalette.BOARD_LABEL_TEXT_COLOR )

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
    if self.boardLabelSize > 0:
      self.drawBoardLabels( display )

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

  def drawBoardLabels(self, display):
    x, y, w, h = 0 * self.tileSize, 8 * self.tileSize, 9 * self.tileSize,\
                 self.boardLabelSize
    self.fileLabels.drawPanel( display, self.ColorPalette.BOARD_LABEL_COLOR,\
                               x, y, w, h )
    x, y, w, h = 0 * self.tileSize, 0 * self.tileSize, self.boardLabelSize,\
                 8 * self.tileSize
    self.rankLabels.drawPanel( display, self.ColorPalette.BOARD_LABEL_COLOR,\
                               x, y, w, h )

    self.fileLabels.drawLabels( display, self.tileSize, self.boardLabelSize,\
      0, 8 * self.tileSize, self.tileSize // 2, self.boardLabelSize // 2 )
    self.rankLabels.drawLabels( display, 0, 0, self.tileSize, 0,\
      self.boardLabelSize // 2, self.tileSize // 2 )

  def setHighlightPotentialMove(self, pos):
    self.setTileColor( pos, self.ColorPalette.TILE_MOVE_AVAILABLE_COLOR )

  def setHighlightPotentialEat(self, pos):
    self.setTileColor( pos, self.ColorPalette.TILE_EAT_AVAILABLE_COLOR )

  def setHighlightPotentialPromotion(self, pos):
    self.setTileColor( pos, self.ColorPalette.TILE_PROMOTION_AVAILABLE_COLOR )

  def setHighlightPotentialCastle(self, pos):
    self.setTileColor( pos, self.ColorPalette.TILE_CASTLE_AVAILABLE_COLOR )

  def setHighlightInCheck(self, pos):
    self.setTileColor( pos, self.ColorPalette.TILE_CHECK_COLOR )

  def setHighlightInCheckMate(self, pos):
    self.setTileColor( pos, self.ColorPalette.TILE_CHECK_MATE_COLOR )

  def setHighlightDraw(self, lightKingPos, darkKingPos):
    self.setTileColor( lightKingPos, self.ColorPalette.TILE_DRAW_COLOR )
    self.setTileColor( darkKingPos, self.ColorPalette.TILE_DRAW_COLOR )

  def setHighlightTileClicked(self, pos):
    self.setTileColor( pos, self.ColorPalette.TILE_CLICKED_COLOR )

  def setHighlightLastMove(self, pos):
    self.setTileColor( pos, self.ColorPalette.TILE_LAST_MOVE_COLOR )

  def setHighlightHint(self, startPos, endPos):
    self.setTileColor( startPos, self.ColorPalette.TILE_HINT_COLOR )
    self.setTileColor( endPos, self.ColorPalette.TILE_HINT_COLOR )

  def setTileColor(self, pos, color):
    if pos is not None:
      x, y = pos
      self.tiles[ y ][ x ].setColor( color )
