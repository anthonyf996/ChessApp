from GetSimpleMovement import GetSimpleMovement
from GetEatMovement import GetEatMovement
from BoardOrientation import BoardOrientation
from PieceColor import PieceColor
from Pon import Pon
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King

class Board:
  def __init__(self, numRows, numCols, orientation = BoardOrientation.LIGHT_TILE_RIGHT):
    self.numRows = numRows
    self.numCols = numCols
    self.orientation = orientation
    self.board = self.initBoard()

  def setup(self):
    self.addPiece( ( 0, 7 ), Rook( PieceColor.LIGHT ) )
    self.addPiece( ( 1, 7 ), Knight( PieceColor.LIGHT ) )
    self.addPiece( ( 2, 7 ), Bishop( PieceColor.LIGHT ) )
    self.addPiece( ( 3, 7 ), Queen( PieceColor.LIGHT ) )
    self.addPiece( ( 4, 7 ), King( PieceColor.LIGHT ) )
    self.addPiece( ( 5, 7 ), Bishop( PieceColor.LIGHT ) )
    self.addPiece( ( 6, 7 ), Knight( PieceColor.LIGHT ) )
    self.addPiece( ( 7, 7 ), Rook( PieceColor.LIGHT ) )
    self.addPiece( ( 0, 6 ), Pon( PieceColor.LIGHT ) )
    self.addPiece( ( 1, 6 ), Pon( PieceColor.LIGHT ) )
    self.addPiece( ( 2, 6 ), Pon( PieceColor.LIGHT ) )
    self.addPiece( ( 3, 6 ), Pon( PieceColor.LIGHT ) )
    self.addPiece( ( 4, 6 ), Pon( PieceColor.LIGHT ) )
    self.addPiece( ( 5, 6 ), Pon( PieceColor.LIGHT ) )
    self.addPiece( ( 6, 6 ), Pon( PieceColor.LIGHT ) )
    self.addPiece( ( 7, 6 ), Pon( PieceColor.LIGHT ) )
    self.addPiece( ( 0, 0 ), Rook( PieceColor.DARK ) )
    self.addPiece( ( 1, 0 ), Knight( PieceColor.DARK ) )
    self.addPiece( ( 2, 0 ), Bishop( PieceColor.DARK ) )
    self.addPiece( ( 3, 0 ), Queen( PieceColor.DARK ) )
    self.addPiece( ( 4, 0 ), King( PieceColor.DARK ) )
    self.addPiece( ( 5, 0 ), Bishop( PieceColor.DARK ) )
    self.addPiece( ( 6, 0 ), Knight( PieceColor.DARK ) )
    self.addPiece( ( 7, 0 ), Rook( PieceColor.DARK ) )
    self.addPiece( ( 0, 1 ), Pon( PieceColor.DARK ) )
    self.addPiece( ( 1, 1 ), Pon( PieceColor.DARK ) )
    self.addPiece( ( 2, 1 ), Pon( PieceColor.DARK ) )
    self.addPiece( ( 3, 1 ), Pon( PieceColor.DARK ) )
    self.addPiece( ( 4, 1 ), Pon( PieceColor.DARK ) )
    self.addPiece( ( 5, 1 ), Pon( PieceColor.DARK ) )
    self.addPiece( ( 6, 1 ), Pon( PieceColor.DARK ) )
    self.addPiece( ( 7, 1 ), Pon( PieceColor.DARK ) )

  def __str__(self):
    return self.toString()

  def toString(self, moves = None):
    moveArr = []

    if moves is not None:
      for m in moves:
        pair = m.getPosPair()
        start, end = pair
        moveArr.append( end )

    s = ""

    for y in range(0,self.numRows):
      for x in range(0,self.numCols):
        p = self.getPiece( ( x, y ) )

        if ( x, y ) in moveArr:
          if p is None:
            s += "||||||||||"
          else:
            s += "|||||%s||||" % ( str( p ) )
        elif p is None:
          s += "|         "
        else:
          s += "|    %s    " % ( str( p ) )
      s += "|\n"

    return s

  def getNumRows(self):
    return self.numRows

  def getNumCols(self):
    return self.numCols

  def getOrientation(self):
    return self.orientation

  def initBoard(self):
    board = []
    for y in range(0, self.numRows):
      row = []
      for x in range(0, self.numCols):
        row.append( None )
      board.append( row )

    return board

  def addPiece(self, pos, piece):
    x, y = pos
    self.board[ y ][ x ] = piece

  def removePiece(self, pos):
    x, y = pos
    self.board[ y ][ x ] = None

  def getPiece(self, pos):
    x, y = pos
    return self.board[ y ][ x ]

  def isValidMove(self, pos):
    x, y = pos
    if 0 <= y < self.numRows and 0 <= x < self.numCols:
      return True

  def isCollision(self, pos):
    return self.isOccupied( pos )

  def isOccupied(self, pos):
    return self.getPiece( pos ) != None

  def isOpponentPiece(self, currPiece, otherPiece):
    return currPiece.getColor() != otherPiece.getColor()

  def getAllMoves(self, pos):
    moves = set()

    moves = moves.union( self.getMoves( pos ) )
    moves = moves.union( self.getEatMoves( pos ) )
    moves = moves.union( self.getSpecialMoves( pos ) )

    return moves

  def getMoves(self, pos):
    return GetSimpleMovement().getMoves( self, pos )

  def getEatMoves(self, pos):
    return GetEatMovement().getMoves( self, pos )

  def getSpecialMoves(self, pos):
    return self.getPiece( pos ).getSpecialMoves( self, pos )

  def move(self, move):
    move.execute()

  def undo(self, move):
    move.undo()
