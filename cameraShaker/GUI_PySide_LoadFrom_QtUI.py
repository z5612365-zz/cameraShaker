import maya.cmds as cmds
from PySide2 import QtCore, QtWidgets

from . import loadUiWidget

import shiboken2
import maya.OpenMayaUI as omui
from PySide2 import  QtUiTools

class PyQtMayaWindow(QtWidgets.QMainWindow):

    def __init__(self):

        #self.app = QtWidgets.QApplication.instance()
        self.MainWindow = loadUiWidget.loadUiWidget().loadUiWidget('/home/chi/maya/scripts/tool/cameraShaker/resource/main.ui')
        #self.MainWindow = self.loadUiWidget('/home/chi/maya/scripts/tool/cameraShaker/resource/main.ui')

        self.init_UI()
        self.SignalSlotLinker()

        #print ("isChecked"+str(self.checkBox.isChecked() ) )
        #print ("isChecked"+str(self.checkBox2.isChecked() ) )


    # ----------------------------------------------- run & show -----------------------------------------------
    def run(self):

        self.MainWindow.show()
        #self.app.exec_()

    def show(self):
        self.MainWindow.show()

    # ----------------------------------------------- init UI stuf -----------------------------------------------
    def init_UI(self):
        self.btn = self.getUIElement(QtWidgets.QPushButton,"pushButton")
        self.lineEdit = self.getUIElement(QtWidgets.QLineEdit,"lineEdit")

        self.checkBox = self.getUIElement(QtWidgets.QCheckBox,"checkBox")
        self.checkBox2 = self.getUIElement(QtWidgets.QCheckBox,"checkBox_2")

        self.lineEdit2 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_2")
        self.lineEdit3 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_3")
        self.lineEdit4 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_4")
        self.lineEdit8 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_8")

        self.lineEdit5 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_5")
        self.lineEdit6 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_6")
        self.lineEdit7 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_7")
        self.lineEdit9 = self.getUIElement(QtWidgets.QLineEdit,"lineEdit_9")

        self.btn2 = self.getUIElement(QtWidgets.QPushButton,"pushButton_2")
        self.btn3 = self.getUIElement(QtWidgets.QPushButton,"pushButton_3")




    def SignalSlotLinker(self):

        self.btn.clicked.connect( self.slot1)
        self.checkBox.stateChanged.connect( self.slot2)
        self.checkBox2.stateChanged.connect( self.slot3)
        self.btn2.clicked.connect( self.addShake)
        self.btn3.clicked.connect( self.deleteExpression)




    # ----------------------------------------------- slot function -----------------------------------------------
    def slot1(self):

        self.load_camera_setting()
        self.lineEdit.setText(self.cam)
        print(self.cam)
        print("QQ")

    def slot2(self):
        if self.checkBox.isChecked():
            cmds.setAttr(self.camShape + ".shakeEnabled",1)
        else:
            cmds.setAttr(self.camShape + ".shakeEnabled", 0)

        #self.shakeEnabled=cmds.getAttr(self.camShape + ".shakeEnabled")
        #self.shakeOverscanEnabled=cmds.getAttr(self.camShape+".shakeOverscanEnabled")

    def slot3(self):
        if self.checkBox2.isChecked():
            cmds.setAttr(self.camShape + ".shakeOverscanEnabled",1)
        else:
            cmds.setAttr(self.camShape + ".shakeOverscanEnabled", 0)

    def load_camera_setting(self):

        self.cam = self.getCamName()
        if self.cam == "":
            print("fk")

        self.camShape = self.getRelShape(self.cam)

        self.shakeEnabled = cmds.getAttr(self.camShape + ".shakeEnabled")
        self.shakeOverscanEnabled = cmds.getAttr(self.camShape + ".shakeOverscanEnabled")

        self.updateCheckbox()

    def updateCheckbox(self):
        if self.shakeEnabled == 0:
            self.checkBox.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.checkBox.setCheckState(QtCore.Qt.Checked)

        if self.shakeOverscanEnabled == 0:
            self.checkBox2.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.checkBox2.setCheckState(QtCore.Qt.Checked)

    def updateLineEdit(self):
        ""

    # ----------------------------------------------- get func -----------------------------------------------
    def getCamName(self):

        camSel = ''.join(cmds.ls(sl=True) )

        return camSel


    def getRelShape(self,ele):
        camShape = ''.join(cmds.listRelatives(ele)[0] )
        return camShape

    def getUIElement(self,type,element):
        return self.MainWindow.findChild(type, element)

    # ----------------------------------------------- tool func -----------------------------------------------
    def addShake(self):


        if self.lineEdit2.text()!="" and self.lineEdit3.text()!="" and self.lineEdit4.text()!="" and self.lineEdit8.text()!="":
            # ========= shakeHorizontal =========
            if cmds.objExists("shakeHorizontal"):
                cmds.expression(
                    s=(self.camShape + ".horizontalShake = noise((time+" + self.lineEdit4.text() + ")*" + self.lineEdit2.text() +"+"+self.lineEdit8.text()+ ")*" + self.lineEdit3.text() + "*.01"),
                    o="", ae=1, uc=all)
            else:
                cmds.expression(
                    s=(self.camShape+".horizontalShake = noise((time+"+ self.lineEdit4.text()+")*"+self.lineEdit2.text()+"+"+self.lineEdit8.text()+")*"+self.lineEdit3.text()+"*.01" ),
                    o="",n="shakeHorizontal",ae=1,uc=all)

        if self.lineEdit5.text() != "" and self.lineEdit6.text() != "" and self.lineEdit7.text()!="" and self.lineEdit9.text()!="":
            # ========= shakeVertical =========
            if cmds.objExists("shakeVertical"):
                cmds.expression(
                    s=(self.camShape + ".verticalShake = noise((time+" + self.lineEdit7.text() + ")*" + self.lineEdit5.text() +"+"+self.lineEdit9.text()+ ")*" + self.lineEdit6.text() + "*.01"),
                    o="", ae=1, uc=all)
            else:
                cmds.expression(
                    s=(self.camShape+ ".verticalShake = noise((time+"+self.lineEdit7.text()+")*"+ self.lineEdit5.text()+"+"+self.lineEdit9.text()+")*"+self.lineEdit6.text()+"*.01" ) ,
                    o="",n="shakeVertical",ae=1,uc=all)

    def deleteExpression(self):
        if cmds.objExists("shakeHorizontal"):
            cmds.delete("shakeHorizontal")
        if cmds.objExists("shakeVertical"):
            cmds.delete("shakeVertical")




if __name__ == '__main__':

    pyQtWindow=PyQtMayaWindow()

    pyQtWindow.run()


