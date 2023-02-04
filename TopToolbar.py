from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QToolBar,QAction

class TopToolbar(QToolBar):
    def __init__(self,mainWidget):
        super(QToolBar,self).__init__()
        self.mainWidget=mainWidget
        self.packetSnifferAction = QAction("&Packet Sniffer", self)
        self.packetSnifferAction.triggered.connect(self.goToPacketSniffer)
        self.sendRecievePacketsAction=QAction("&Send And Recieve Packets",self)
        self.sendRecievePacketsAction.triggered.connect(self.goToSendAndRecievePackets)
        self.threeWayHandShakeAction=QAction("&Three Way Handshake",self)
        self.threeWayHandShakeAction.triggered.connect(self.goToThreeWayHandShake)
        self.addAction(self.packetSnifferAction)
        self.addAction(self.sendRecievePacketsAction)
        self.addAction(self.threeWayHandShakeAction)


    def goToPacketSniffer(self):
        self.mainWidget.setCurrentIndex(0)

    def goToSendAndRecievePackets(self):
        self.mainWidget.setCurrentIndex(1)

    def goToThreeWayHandShake(self):
        self.mainWidget.setCurrentIndex(2)
    