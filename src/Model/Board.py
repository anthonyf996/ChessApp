from GetSimpleMovement import GetSimpleMovement
from GetEatMovement import GetEatMovement
from GetCollisionMovement import GetCollisionMovement
from PieceColor import PieceColor
from Pon import Pon
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King

class Board:
  def __init__(self, numRows, numCols ):
    self.numRows = numRows
    self.numCols = numCols
    self.board = self.initBoard()
    self.kings = {}

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
    self.kings[ PieceColor.LIGHT ] = self.getPiece( ( 4, 7 ) )
    self.kings[ PieceColor.DARK ] = self.getPiece( ( 4, 0 ) )
    """
    self.addPiece( ( 1, 3 ), Queen( PieceColor.LIGHT ) )
    self.addPiece( ( 4, 7 ), King( PieceColor.LIGHT ) )
    self.addPiece( ( 0, 0 ), King( PieceColor.DARK ) )
    self.kings[ PieceColor.LIGHT ] = self.getPiece( ( 4, 7 ) )
    self.kings[ PieceColor.DARK ] = self.getPiece( ( 0, 0 ) )
    """

  def getNumRows(self):
    return self.numRows

  def getNumCols(self):
    return self.numCols

  def getBoard(self):
    return self.board

  def getKings(self):
    return self.kings

  def getKingsPair(self):
    return self.kings[ PieceColor.LIGHT ], self.kings[ PieceColor.DARK ]

  def getTurnKing(self, turnColor):
    return self.getKing( turnColor )

  def getKing(self, color):
    return self.getKings()[ color ]

  def getMovesEndPos(self, moves):
    moveArr = []

    if moves is not None:
      for m in moves:
        start, end = m.getPosPair()

        moveArr.append( end )

    return moveArr

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
    if piece is not None:
      piece.setPos( pos )

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

  def getCollisionMoves(self, pos):
    return GetCollisionMovement().getMoves( self, pos )

  def getSpecialMoves(self, pos):
    return self.getPiece( pos ).getSpecialMoves( self, pos )

  def move(self, move):
    move.execute()

  def undo(self, move):
    move.undo()

  def isInDanger(self, currPos):
    inDanger = False
    currPiece = self.getPiece( currPos )

    for y in range(0,self.getNumRows()):
      for x in range(0,self.getNumCols()):
        pos = ( x, y )
        piece = self.getPiece( pos )

        if piece is None:
          continue
        if piece.getColor() == currPiece.getColor():
          continue

        eatMoves = self.getEatMoves( pos )

        for move in eatMoves:
          if currPos in move.getPosPair():
            inDanger = True
            break

    return inDanger

  def isLastPiece(self, kingPos):
    king = self.getPiece( kingPos )

    for y in range(0,self.getNumRows()):
      for x in range(0,self.getNumCols()):
        pos = ( x, y )
        piece = self.getPiece( pos )

        if piece is None:
          continue
        if piece == king:
          continue
        if piece.getColor() == king.getColor():
          return False

    return True

  def isKingTrapped(self, kingPos):
    king = self.getPiece( kingPos )
    for y in range(0,self.getNumRows()):
      for x in range(0,self.getNumCols()):
        pos = ( x, y )
        piece = self.getPiece( pos )
        if piece is None:
          continue
        if piece.getColor() != king.getColor():
          continue

        if not self.cannotStopCheck( pos, king ):
          return False

    return True

  def cannotStopCheck(self, piecePos, king):
    moves = self.getAllMoves( piecePos )

    for move in moves:
      self.move( move )
      inDanger = self.isInDanger( king.getPos() )
      self.undo( move )

      if not inDanger:
        return False

    return True

  # This method should only be called after a move is made to verify the
  # integrity of the board.
  def isInInconsistentState(self, currPieceColor):
    # Do not allow any move that places own king in check
    if self.isInDanger( self.getKing( currPieceColor ).getPos() ):
      return True
    # Do not allow any king to be eaten
    for color,king in self.getKings().items():
      if self.getPiece( king.getPos() ) != king:
        return True

    return False
