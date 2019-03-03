from GetSimpleMovement import GetSimpleMovement
from GetEatMovement import GetEatMovement
from GetCollisionMovement import GetCollisionMovement
from PieceColor import PieceColor
from King import King
from BoardFromFile import BoardFromFile
from BoardQueryIsInDanger import BoardQueryIsInDanger 
from BoardQueryIsLastPiece import BoardQueryIsLastPiece 
from BoardQueryIsKingTrapped import BoardQueryIsKingTrapped 
from BoardQueryNoMovesLeft import BoardQueryNoMovesLeft 

class Board:
  def __init__(self, numRows, numCols, boardconfigFileName = ""):
    self.numRows = numRows
    self.numCols = numCols
    self.boardconfigFileName = boardconfigFileName
    self.kings = {}
    self.board = self.getInitBoard()
    self.setupBoard()

  def getInitBoard(self):
    board = []
    for y in range(0, self.numRows):
      row = []
      for x in range(0, self.numCols):
        row.append( None )
      board.append( row )

    return board

  def setupBoard(self):
    BoardFromFile( self, self.boardconfigFileName ).setupBoard()

  def reset(self):
    self.kings = {}
    self.board = self.getInitBoard()
    self.setupBoard()

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
    if color in self.kings:
      return self.getKings()[ color ]
    return None

  def getMovesEndPos(self, moves):
    moveArr = []

    for m in moves:
      moveArr.append( m.getEndPos() )

    return moveArr

  def addPiece(self, pos, piece):
    x, y = pos
    self.board[ y ][ x ] = piece
    if piece is not None:
      piece.setPos( pos )
      if isinstance( piece, King ):
        self.kings[ piece.getColor() ] = piece

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
    moves = self.getMoves( pos )
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
    startPiece = self.getPiece( move.getStartPos() )

    move.execute()

    if self.isInInconsistentState( startPiece.getColor() ):
      self.undo( move )
      return False

    return True

  def undo(self, move):
    move.undo()

  def unprotectedMove(self, move):
    move.execute()

  def isInDanger(self, currPos):
    return BoardQueryIsInDanger().queryBoard( self, currPos )

  def isLastPiece(self, kingPos):
    return BoardQueryIsLastPiece().queryBoard( self, kingPos )

  def isKingTrapped(self, kingPos):
    return BoardQueryIsKingTrapped().queryBoard( self, kingPos )

  def noMovesLeft(self, kingPos):
    return BoardQueryNoMovesLeft().queryBoard( self, kingPos )

  """
  def noMovesLeft(self, currPos):
    currPiece = self.getPiece( currPos )

    for y in range(0,self.getNumRows()):
      for x in range(0,self.getNumCols()):
        pos = ( x, y )
        piece = self.getPiece( pos )

        if piece is None or piece.getColor() != currPiece.getColor():
          continue

        for move in self.getAllMoves( pos ):
          if not self.stillInCheckAfterMove( currPiece, move ):
            return False

    return True

  def isInDanger(self, currPos):
    currPiece = self.getPiece( currPos )

    for y in range(0,self.getNumRows()):
      for x in range(0,self.getNumCols()):
        pos = ( x, y )
        piece = self.getPiece( pos )

        if piece is None or piece.getColor() == currPiece.getColor():
          continue

        for move in self.getEatMoves( pos ):
          if currPos in move.getPosPair():
            return True

    return False

  def isLastPiece(self, kingPos):
    king = self.getPiece( kingPos )

    for y in range(0,self.getNumRows()):
      for x in range(0,self.getNumCols()):
        pos = ( x, y )
        piece = self.getPiece( pos )

        if piece is None or piece == King or piece.getColor() == king.getColor():
          return False

    return True

  def isKingTrapped(self, kingPos):
    king = self.getPiece( kingPos )
    for y in range(0,self.getNumRows()):
      for x in range(0,self.getNumCols()):
        pos = ( x, y )
        piece = self.getPiece( pos )

        if piece is None or piece.getColor() != king.getColor():
          continue

        if self.canStopCheck( pos, king ):
          return False

    return True
  """

  def canStopCheck(self, piecePos, king):
    for move in self.getAllMoves( piecePos ):
      if not self.stillInCheckAfterMove( king, move ):
        return True

    return False

  def stillInCheckAfterMove(self, king, move):
    self.unprotectedMove( move )
    stillInCheck = self.isInDanger( king.getPos() )
    self.undo( move )
    return stillInCheck

  # This method should only be called after a move is made to verify the
  # integrity of the board.
  def isInInconsistentState(self, currPieceColor):
    # Do not allow any move that places own king in check
    ownKing = self.getKing( currPieceColor )
    if ownKing is not None and self.isInDanger( ownKing.getPos() ):
      return True
    # Do not allow any king to be eaten
    for color,king in self.getKings().items():
      if self.getPiece( king.getPos() ) != king:
        return True

    return False
