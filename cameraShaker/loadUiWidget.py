from PySide2 import QtCore, QtUiTools, QtWidgets


import shiboken2
import maya.OpenMayaUI as omui


def getMayaMainWindow():
    accessMainWindow = omui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(
        long(accessMainWindow),
        QtWidgets.QMainWindow

    )
class loadUiWidget():

    def __init__(self):
        #self.ui
        print("412")

    def loadUiWidget(self, uifilename, parent=getMayaMainWindow()):

        loader = QtUiTools.QUiLoader()
        uifile = QtCore.QFile(uifilename)
        uifile.open(QtCore.QFile.ReadOnly)
        ui = loader.load(uifile, parent)
        uifile.close()
        return ui

