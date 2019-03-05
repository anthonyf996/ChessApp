import sys
sys.path.insert(0, 'Model/')
sys.path.insert(0, 'View/')
sys.path.insert(0, 'Controller/')
#from ConsoleView import ConsoleView
from GUIView import GUIView
from Model import Model
from Controller import Controller
#from ConsoleClock import ConsoleClock
from GUIClock import GUIClock

clock = GUIClock( fpsSpec = { "FPS" : 20 } )
#clock = ConsoleClock( fpsSpec = { "FPS" : 60 } )
#view = ConsoleView()
view = GUIView()
model = Model( boardconfigFileName = "Model/StandardConfig.json" )
controller = Controller( view, model, clock )

controller.run()
