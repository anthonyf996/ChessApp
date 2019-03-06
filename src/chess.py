import sys
sys.path.insert(0, 'Model/')
sys.path.insert(0, 'View/')
sys.path.insert(0, 'Controller/')
from Controller import Controller
from GUIControllerFactory import GUIControllerFactory
#from ConsoleControllerFactory import ConsoleControllerFactory 

controller = Controller( GUIControllerFactory() )
#controller = Controller( ConsoleControllerFactory() )
controller.run()
