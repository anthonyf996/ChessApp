from View.View import View
from Model.Model import Model
from Controller.Controller import Controller

view = View()
model = Model()
controller = Controller( view, model )

controller.run()
