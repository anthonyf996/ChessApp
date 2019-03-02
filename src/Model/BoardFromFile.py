import json
from ast import literal_eval as literalEval
from Pon import Pon
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King
from PieceColor import PieceColor
from PieceType import PieceType
from PieceFactory import PieceFactory

class BoardFromFile:
  def __init__(self, board, filename):
    self.Board = board
    self.filename = filename
    self.colorMap = { "LIGHT" : PieceColor.LIGHT, "DARK" : PieceColor.DARK }
    self.pieceTypeMap = { "KING" : PieceType.KING,
                          "QUEEN" : PieceType.QUEEN,
                          "ROOK" : PieceType.ROOK,
                          "BISHOP" : PieceType.BISHOP,
                          "KNIGHT" : PieceType.KNIGHT,
                          "PON" : PieceType.PON
                        }

  def setupBoard(self):
    if len( self.filename ) > 0:
      spec = self.getSpecFromFile( self.filename )
      self.addPiecesToBoard( self.Board, self.getPiecesArrFromSpec( spec ) )

  def getSpecFromFile(self, filename):
    with open( filename, "r" ) as f:
      spec = json.loads( f.read() )

    return spec

  def addPiecesToBoard(self, board, pieces):
    for piece in pieces:
      board.addPiece( piece.getPos(), piece )

  def getPiecesArrFromSpec(self, spec):
    pieces = []

    for color,piecesDict in spec.items():
      for pieceType, positions in piecesDict.items():
        pieces += self.getPieces( color, pieceType, positions )

    return pieces

  def getPieces(self, color, pieceType, positions):
    pieces = []

    for pos in positions:
      pieces.append( self.getPiece( color, pieceType, literalEval( pos ) ) )

    return pieces

  def getPiece(self, color, pieceType, pos):
    piece = PieceFactory().getPiece( self.colorMap[ color ], self.pieceTypeMap[ pieceType ] )
    piece.setPos( pos )
    return piece
