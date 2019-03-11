from EatMove import EatMove
from PieceType import PieceType
from PieceColor import PieceColor
import random

class AI:
  def __init__(self, Board, Game, color):
    self.Board = Board
    self.Game = Game
    self.color = color
    self.encourageForwardMovementRate = 0.01

  def getMove(self, color = None):
    if color is None:
      color = self.color
    weightedMoves = []
    for row in self.Board.getBoard():
      for piece in row:
        if piece is not None and piece.getColor() == color:
          for move in self.Board.getAllMoves( piece.getPos() ):
            weightedMoves.append( self.tryMove( self.Board, self.Game, move ) )

    return self.getMaxMove( weightedMoves )

  def tryMove(self, board, game, move):
    weight = 0
    startPos = move.getStartPos()
    currPiece = board.getPiece( move.getStartPos() )
    currColor = currPiece.getColor()
    if currColor == PieceColor.LIGHT:
      otherColor = PieceColor.DARK
    else:
      otherColor = PieceColor.LIGHT

    # Encourage forward movements randomly
    if random.random() <= self.encourageForwardMovementRate:
      x1, y1 = move.getStartPos()
      x2, y2 = move.getEndPos()
      if currColor == PieceColor.LIGHT:
        if ( y2 < y1 ):
          weight += 20
      else:
        if ( y2 > y1 ):
          weight += 20

    # Encourage eating enemy pieces
    if isinstance( move, EatMove ):
      target = board.getPiece( move.getEndPos() )
      if target.getType() == PieceType.QUEEN:
        weight += 100
      elif target.getType() == PieceType.ROOK:
        weight += 80
      elif target.getType() == PieceType.BISHOP:
        weight += 60
      elif target.getType() == PieceType.KNIGHT:
        weight += 40
      elif target.getType() == PieceType.PON:
        weight += 20

    move.execute()

    if board.isInInconsistentState( currColor ):
      weight -= 500
    # Encourage placing opponent in check
    if game.getIsCheck():
      if game.getInCheck().getColor() == otherColor:
        weight += 120
    # Discourage losing own pieces
    for row in self.Board.getBoard():
      for piece in row:
        if piece is not None and piece.getColor() == currColor:
          if board.isInDanger( piece.getPos() ):
            if board.isProtected( piece.getPos() ):
              print ( "PROTECTED %s %s" % ( str( piece.getPos() ), piece.getType() ) )
              if piece.getType() == PieceType.QUEEN:
                weight -= 50
              elif piece.getType() == PieceType.ROOK:
                weight -= 40
              elif piece.getType() == PieceType.BISHOP:
                weight -= 30
              elif piece.getType() == PieceType.KNIGHT:
                weight -= 20
              elif piece.getType() == PieceType.PON:
                weight -= 10
            else:
              print ( "NOT PROTECTED %s %s" % ( str( piece.getPos() ), piece.getType() ) )
              if piece.getType() == PieceType.QUEEN:
                weight -= 100
              elif piece.getType() == PieceType.ROOK:
                weight -= 80
              elif piece.getType() == PieceType.BISHOP:
                weight -= 60
              elif piece.getType() == PieceType.KNIGHT:
                weight -= 40
              elif piece.getType() == PieceType.PON:
                weight -= 20
    """
    if board.isInDanger( currPiece.getPos() ):
      if currPiece.getType() == PieceType.QUEEN:
        weight -= 100
      elif currPiece.getType() == PieceType.ROOK:
        weight -= 80
      elif currPiece.getType() == PieceType.BISHOP:
        weight -= 60
      elif currPiece.getType() == PieceType.KNIGHT:
        weight -= 40
      elif currPiece.getType() == PieceType.PON:
        weight -= 20
    """

    """
    for row in self.Board.getBoard():
      for piece in row:
        if piece is not None and piece.getColor() == otherColor:
          if board.isInDanger( piece.getPos() ):
            if currPiece.getType() == PieceType.QUEEN:
              weight += 100
            elif currPiece.getType() == PieceType.ROOK:
              weight += 80
            elif currPiece.getType() == PieceType.BISHOP:
              weight += 60
            elif currPiece.getType() == PieceType.KNIGHT:
              weight += 40
            elif currPiece.getType() == PieceType.PON:
              weight += 20
    """

    move.undo()

    return ( weight, move )

  def getMaxMove(self, weightedMoves):
    maxWeight = -500
    maxMoves = []
    for weightedMove in weightedMoves:
      weight, move = weightedMove
      if weight > maxWeight:
        maxWeight = weight
        maxMoves = [ move ]
      elif weight == maxWeight:
        maxMoves.append( move )
    print( maxMoves )
    
    if len( maxMoves ) == 0:
      move = None
    else:
      move = maxMoves[ random.randint( 0, len( maxMoves ) - 1 ) ]
    print( move )
    return move
