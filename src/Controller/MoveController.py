from MoveWithSideEffects import MoveWithSideEffects 
from PieceUpgradeCommand import PieceUpgradeCommand
from StateType import StateType
from EatMove import EatMove
from PieceType import PieceType
from SimpleMove import SimpleMove
from EnPassantCommand import EnPassantCommand

class MoveController:
  def __init__(self):
    self.reset()

  def reset(self):
    self.currPos = None
    self.currPiece = None
    self.prevPos = None

  def getCurrPos(self):
    return self.currPos

  def getPrevPos(self):
    return self.prevPos

  def getMoves(self, board):
    if self.currPiece is not None:
      return board.getAllMoves( self.currPos )
    return set()

  def handleInput(self, stateManager, board, game, pos):
    if self.isValidMove( board, pos ):
      self.updatePos( pos )
      if self.readyToMove( game ):
        move = self.getMove( board )
        if not self.checkToPromptUpgradeType( stateManager, board, game, move ):
          self.performMove( board, game, move )
      self.toggleCurrPiece( board )

  def isValidMove(self, board, pos):
    if pos is not None:
      if board.isValidMove( pos ):
        return True

    return False

  def updatePos(self, pos):
    if self.currPos is not None and self.currPiece is None:    
      self.currPos = None
    else:
      self.currPos = pos

  def readyToMove(self, game):
    if self.currPiece is not None:
      return self.canMove( game )

    return False
  
  def canMove(self, game):
    if not game.isGameOver():
      if not game.getTurnsEnabled() or self.currPiece.getColor() == game.getTurnColor():
        return True
      elif game.getTurnsEnabled():
        print( "%s's turn!" % ( game.getTurnColor() ) )

    return False

  def checkToPromptUpgradeType(self, stateManager, board, game, move):
    if isinstance( move, MoveWithSideEffects ):
      if not self.canPerformUpgradeMove( board, game, move.getMove()):
        return False
      command = move.getCommand( 0 )
      if isinstance( command, PieceUpgradeCommand ):
        if not game.getIsAIEnabled() or not game.getIsAITurn():
          pieceUpgradeState = stateManager.getState( StateType.PIECE_UPGRADE )
          pieceUpgradeState.update( move, command, self.currPiece.getColor() )
          stateManager.setState( StateType.PIECE_UPGRADE )
          return True
    return False

  def canPerformUpgradeMove(self, board, game, move):
    king = board.getKing( game.getTurnColor() )
    return not board.stillInCheckAfterMove( king, move )

  def performMove(self, board, game, move):
    if move is not None:
      successful = board.move( move )
      if successful:
        print( "%s: %s" % ( game.getTurnColor(), str( move ) ) )
        self.checkToResetTurnCount( board, game, move )
        game.advanceTurn()
        self.prevPos = move.getEndPos()

  def checkToResetTurnCount(self, board, game, move ):
    if isinstance( move, MoveWithSideEffects ):
      innerMove = move.getMove()
      command = move.getCommand( 0 )
      if isinstance( command, PieceUpgradeCommand ):
        game.resetTurnCount()
    else:
      innerMove = move

    if isinstance( innerMove, EatMove ):
      game.resetTurnCount()
    else:
      if isinstance( innerMove, SimpleMove ) or isinstance( innerMove, EnPassantCommand ):
        piece = board.getPiece( innerMove.getEndPos() )
        if piece.getType() == PieceType.PON:
          game.resetTurnCount()

  def toggleCurrPiece(self, board):
    if self.currPiece is None:
      if self.currPos is not None:
        self.currPiece = board.getPiece( self.currPos )
    else:
      self.currPiece = None
      self.currPos = None

  def getMove(self, board):
    for move in board.getAllMoves( self.currPiece.getPos() ):
      if ( self.currPiece.getPos(), self.currPos ) == move.getPosPair():
        return move

    return None
