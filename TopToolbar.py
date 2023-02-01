from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QToolBar,QAction

class TopToolbar():
    def __init__(self,parent):
        self.toolBar=QToolBar("Top toolbar",parent)
        self.openAction = QAction("&Packet Sniffer", parent)
        self.openAction.triggered.connect(self.goToPacketSniffer)
        self.toolBar.addAction(self.openAction)


    def goToPacketSniffer(self):
        if self.currentWindow!=self.packetSnifferWindow:
            self.currentWindow.hide()
            self.packetSnifferWindow.show()
            self.currentWindow=self.packetSnifferWindow

    def setPacketSnifferWindow(self,win):
        self.packetSnifferWindow=win
        self.currentWindow=win

    def setSendRecievePacketsWindow(self,win):
        self.sendRecievePacketsWindow=win
        self.currentWindow=win
    