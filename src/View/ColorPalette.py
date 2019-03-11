from RelativeColor import RelativeColor

class ColorPalette:
  TILE_PROMOTION_AVAILABLE_COLOR = ( 150, 50, 200 )
  TILE_CASTLE_AVAILABLE_COLOR = ( 100, 175, 125 )
  TILE_CHECK_COLOR = ( 255, 200, 200 )
  TILE_CHECK_MATE_COLOR = ( 255, 100, 100 )
  TILE_DRAW_COLOR = ( 100, 255, 100 )
  TILE_HINT_COLOR = ( 200, 200, 140 )
  BOARD_LABEL_COLOR = ( 0, 70, 160 )
  BOARD_LABEL_TEXT_COLOR = ( 255, 255, 255 )
  BOARD_REPLAY_TEXT_COLOR = ( 200, 50, 50 )

  def __init__(self):
    self.LIGHT_MENU_COLOR = RelativeColor().getColor( self.DARK_TILE_COLOR, ( 22, 22, 50 ) )
    self.DARK_MENU_COLOR = RelativeColor().getColor( self.DARK_TILE_COLOR, ( -50, -50, -22 ) )
