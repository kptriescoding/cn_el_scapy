from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView,QWidget
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView,QWidget,QGridLayout,QHBoxLayout,QLabel

import sys
from scapy.all import IP,TCP,UDP,ICMP,Ether
import socket
from GeneratePacketReportButton import GeneratePacketReportButton

class SendAndReciecePackets(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setWindowTitle("CN EL")
        self.mainLayout=QVBoxLayout()
        self.setLayout(self.mainLayout)
        self._initUI()
        self._setUpPostiions()

    def _initUI(self):
        self.dataLinkLayerLabel = QtWidgets.QLabel()
        self.dataLinkLayerLabel.setText("Data Link Layer")

        self.networkLayerLabel = QtWidgets.QLabel()
        self.networkLayerLabel.setText("Network Layer")

        self.createPacketsLabel = QtWidgets.QLabel()
        self.createPacketsLabel.setText("Create Packets")

        self.dataLinkSelectBox = QtWidgets.QComboBox()
        self.dataLinkSelectBox.addItem("Ether")

        self.netWorkSelectBox = QtWidgets.QComboBox()
        self.netWorkSelectBox.addItem("IP")

        self.transportLayerLabel = QtWidgets.QLabel()
        self.transportLayerLabel.setText("Transport Layer")

        self.transportSelectBox = QtWidgets.QComboBox()
        self.transportSelectBox.addItem("UDP")
        self.transportSelectBox.addItem("ICMP")
        self.transportSelectBox.addItem("TCP")

        self.createPacketsButton = QtWidgets.QPushButton()
        self.createPacketsButton.setText("Create")
        self.createPacketsButton.clicked.connect(self.createPackets)

        self.generatePacketsButton = QtWidgets.QPushButton()
        self.generatePacketsButton.setText("Generate PDF")
        self.generatePacketsButton.clicked.connect(self.generatePacketsPDF)

        self.networkSrcInput = QtWidgets.QLineEdit()
        self.networkSrcInput.setText("127.0.0.1")
        self.networkDestInput = QtWidgets.QLineEdit()
        self.networkDestInput.setText("127.0.0.1")

        self.dataLinkSelectLabel = QtWidgets.QLabel()
        self.dataLinkSelectLabel.setText("Protocol:")
        self.networkSelectLabel = QtWidgets.QLabel()
        self.networkSelectLabel.setText("Protocol:")
        self.transportSelectLabel = QtWidgets.QLabel()
        self.transportSelectLabel.setText("Protocol:")

        self.networkSrcLabel = QtWidgets.QLabel()
        self.networkSrcLabel.setText("src:")
        self.networkDestLabel = QtWidgets.QLabel()
        self.networkDestLabel.setText("dest:")

    def _setUpPostiions(self):
        self.mainLayout.addWidget(self.createPacketsLabel)
        self.mainLayout.addWidget(self.dataLinkLayerLabel)

        self.dataLinkLayerLayout=QHBoxLayout()
        self.dataLinkLayerLayout.addWidget(self.dataLinkSelectLabel)
        self.dataLinkLayerLayout.addWidget(self.dataLinkSelectBox)

        self.mainLayout.addLayout(self.dataLinkLayerLayout)

        self.mainLayout.addWidget(self.networkLayerLabel)

        self.networkLayerLayout=QHBoxLayout()
        self.networkLayerLayout.addWidget(self.networkSelectLabel)
        self.networkLayerLayout.addWidget(self.netWorkSelectBox)
        self.networkLayerLayout.addWidget(self.networkSrcLabel)
        self.networkLayerLayout.addWidget(self.networkSrcInput)
        self.networkLayerLayout.addWidget(self.networkDestLabel)
        self.networkLayerLayout.addWidget(self.networkDestInput)

        self.mainLayout.addLayout(self.networkLayerLayout)

        self.mainLayout.addWidget(self.transportLayerLabel)

        self.transportLayerLayout=QHBoxLayout()
        self.transportLayerLayout.addWidget(self.transportSelectLabel)
        self.transportLayerLayout.addWidget(self.transportSelectBox)

        self.mainLayout.addLayout(self.transportLayerLayout)

        self.createButtonLayout=QHBoxLayout()
        self.createButtonLayout.addWidget(self.createPacketsButton)
        self.createButtonLayout.addWidget(self.generatePacketsButton)

        self.mainLayout.addLayout(self.createButtonLayout)
    
    def createPackets(self):
        print("")
    
    def generatePacketsPDF(self):
        networkPacket=self.getPacket()
        networkPacket.show()
    
    def getPacket(self):
        print(self.dataLinkSelectBox.currentText())
        linkLayerPacket=Ether()
        networkLayerPacket=IP(src=self.networkSrcInput.text(),dst=self.networkDestInput.text())
        transportProtocol=self.transportSelectBox.currentText()
        if(transportProtocol=="TCP"):
            transportLayerPacket=TCP()
        elif(transportProtocol=="UDP"):
            transportLayerPacket=UDP()
        elif(transportProtocol=="ICMP"):
            transportLayerPacket=ICMP()
        networkPacket=linkLayerPacket/networkLayerPacket/transportLayerPacket
        return networkPacket




        
