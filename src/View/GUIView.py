import pygame
from View import View
from PieceType import PieceType
from PieceColor import PieceColor
from GUIBoard import GUIBoard
from ColorPalette import ColorPalette
from SpriteSheet import SpriteSheet
from GUIImage import GUIImage
from MoveType import MoveType

class GUIView(View):
  BOARD_LABEL_FONT = "Arial"
  TILE_SIZE = 75
  BOARD_LABEL_SIZE = TILE_SIZE // 2
  NUM_TILES = 8
  DISP_WIDTH = NUM_TILES * TILE_SIZE + BOARD_LABEL_SIZE
  DISP_HEIGHT = DISP_WIDTH

  def __init__(self):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption( "Chess v3.0" )
    self.gameDisplay = pygame.display.set_mode( ( self.DISP_WIDTH, self.DISP_HEIGHT ) )

    self.spritePos = { PieceType.KING : 0, PieceType.QUEEN : 1, PieceType.BISHOP : 2,
                       PieceType.KNIGHT : 3, PieceType.ROOK : 4, PieceType.PON : 5 }
    self.spriteColorPos = { PieceColor.LIGHT : 0, PieceColor.DARK : 1 }
    self.images = {}
    self.spriteSheets = {}
    self.regImages()

    self.ColorPalette = ColorPalette()
 
    self.Board = GUIBoard( self.ColorPalette, self.TILE_SIZE, self.NUM_TILES,
                             self.BOARD_LABEL_SIZE, self.BOARD_LABEL_FONT )

  def finish(self):
    pygame.quit()

  def regImages(self):
    self.images[ "PIECES" ] = GUIImage( "../img/sprites/450px-Chess_Pieces_Sprite.svg.png" )
    self.spriteSheets[ "PIECES" ] = SpriteSheet( self.images[ "PIECES" ], self.TILE_SIZE,
                                                 self.TILE_SIZE, self.spritePos, self.spriteColorPos )
    self.AppIcon = GUIImage( "../img/icons/queen75x75.png" )

  def setAppIcon(self, img):
    pygame.display.set_icon( img )

  def display(self, board, game, moves = set(), currPos = None):
    self.Board.setHighlightTileClicked( currPos )
    self.displayMoves( moves )
    self.displayGameState( game )
    self.Board.draw( self.gameDisplay, self.spriteSheets[ "PIECES" ], board.getBoard() )
    pygame.display.update()

  def displayMoves(self, moves):
    for move in moves:
      moveType = move.getMoveType()
      if moveType == MoveType.EAT:
        self.Board.setHighlightPotentialEat( move.getEndPos() )
      elif moveType == MoveType.PROMOTION:
        self.Board.setHighlightPotentialPromotion( move.getEndPos() )
      elif moveType == MoveType.CASTLE:
        self.Board.setHighlightPotentialCastle( move.getEndPos() )
      else:
        self.Board.setHighlightPotentialMove( move.getEndPos() )

  def displayGameState(self, game):
    if game.getIsCheckMate():
      self.displayCheckMate( game.getInCheckMate() )
    elif game.getIsDraw():
      kings = board.getKingsPair()
      self.displayDraw( *kings )
    elif game.getIsCheck():
      self.displayCheck( game.getInCheck() )

  def displayCheck(self, piece):
    #print ( "Check at %s [ %s ]" % ( piece.getPos(), piece.getColor() ) )
    self.Board.setHighlightInCheck( piece.getPos() )

  def displayCheckMate(self, piece):
    #print ( "CheckMate at %s [ %s ]" % ( piece.getPos(), piece.getColor() ) )
    self.Board.setHighlightInCheckMate( piece.getPos() )

  def displayDraw(self, lightKing, darkKing):
    #print ( "Draw at %s and %s" % ( lightKing.getPos(), darkKing.getPos() ) )
    self.Board.setHighlightDraw( piece.getPos() )

  # Board label offset is subtracted from the x pos index so that the entire board is
  # effectively shifted right by the value of the board label size, making room for
  # the board labels to be drawn.
  def getPosPairFromCursor(self, cursor):
    if cursor is None:
      return cursor

    x, y = cursor
    x = x - self.BOARD_LABEL_SIZE
    x , y = x // self.TILE_SIZE, y // self.TILE_SIZE

    return ( x, y )
