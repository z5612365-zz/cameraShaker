#run this on maya python script
from tool.cameraShaker.cameraShaker import GUI_PySide_LoadFrom_QtUI as gui

reload(gui)
cameraShaker = gui.PyQtMayaWindow()
cameraShaker.run()

