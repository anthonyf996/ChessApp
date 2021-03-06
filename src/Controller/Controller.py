from GameExitException import GameExitException

class Controller:
  def __init__(self, Factory):
    self.Factory = Factory
    self.View = self.Factory.createView()
    self.Model = self.Factory.createModel()
    self.Clock = self.Factory.createClock()
    self.MoveController = self.Factory.createMoveController( 
                            self.Factory.createMoveHistory( self.Model ) )
    self.AI = self.Factory.createAI( self.Model )
    self.HintManager = self.Factory.createHintManager( self.Model.getGame(),\
                         self.AI )
    self.KeyHandler = self.Factory.createKeyHandler( self.Model, self.MoveController,\
                                                       self.HintManager )
    self.InputReader = self.Factory.createInputReader( self.View, self.Model.getGame(),\
                                                       self.MoveController, self.KeyHandler )
    self.InputController = self.Factory.createInputController( self, self.InputReader )
    self.StateManager = self.Factory.createStateManager( self.View, self.Model,\
                          self, self.MoveController, self.InputController,\
                          self.AI, self.HintManager )

  def run(self):
    try:
      while True:
        self.StateManager.updateView()

        cursor = self.StateManager.pollUserInput()

        self.StateManager.updateModel( cursor )

        self.tick()
    except GameExitException as e:
      print( e )
    finally:
      self.finish()

  def finish(self):
    self.View.finish()

  def reset(self):
    self.Model.getBoard().reset()
    self.Model.getGame().reset()
    self.MoveController.reset()
    self.StateManager.reset()

  def tick(self):
    if self.Model.getGame().getPlayersEnabled():
      self.Clock.tick()
    else:
      #self.Clock.tick( "AI_FPS" )
      self.Clock.tick( "TESTING_FPS" )
