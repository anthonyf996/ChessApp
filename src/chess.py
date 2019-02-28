import sys
sys.path.insert(0, 'Model/')
sys.path.insert(0, 'View/')
sys.path.insert(0, 'Controller/')
from View import View
from Model import Model
from Controller import Controller

view = View()
model = Model()
model.board.setup()
controller = Controller( view, model )

controller.run()
