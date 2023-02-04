from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView,QWidget
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView,QWidget,QGridLayout,QHBoxLayout,QLabel

import sys
from scapy.all import IP,TCP,UDP,Ether,conf,get_if_addr,sr,sr1,get_if_list,send,ICMP
import socket
from BottomLayer import BottomLayer
from threading import Thread
from PacketTable import PacketTable

class SendAndReciecePackets(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setWindowTitle("CN EL")
        self.mainLayout=QVBoxLayout()
        self.networkPacket=None
        self.interfaces=get_if_list()
        self.setLayout(self.mainLayout)
        self._initUI()
        self._setUpPostiions()

    def _initUI(self):

        self.networkLayerLabel = QtWidgets.QLabel()
        self.networkLayerLabel.setText("Network Layer")

        self.createPacketsLabel = QtWidgets.QLabel()
        self.createPacketsLabel.setText("Create Packets")

        self.netWorkSelectBox = QtWidgets.QComboBox()
        self.netWorkSelectBox.addItem("IP")

        self.transportLayerLabel = QtWidgets.QLabel()
        self.transportLayerLabel.setText("Transport Layer")

        self.transportSelectBox = QtWidgets.QComboBox()
        self.transportSelectBox.addItem("UDP")
        self.transportSelectBox.addItem("TCP")
        self.transportSelectBox.addItem("ICMP")

        self.transportLayerDportLabel=QtWidgets.QLabel()
        self.transportLayerDportLabel.setText("dport:")
        self.transportLayerDportInput=QtWidgets.QLineEdit()

        self.createPacketsButton = QtWidgets.QPushButton()
        self.createPacketsButton.setText("Create")
        self.createPacketsButton.clicked.connect(self.createPackets)

        self.sendPacketsButton = QtWidgets.QPushButton()
        self.sendPacketsButton.setText("Send")
        self.sendPacketsButton.clicked.connect(self.sendPackets)

        self.networkSrcInput = QtWidgets.QLineEdit()
        self.networkSrcInput.setText(get_if_addr(conf.iface))
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

        self.bottomLayer=BottomLayer()

        self.userDataLabel=QtWidgets.QLabel()
        self.userDataLabel.setText("Enter Data:")
        self.userDataInput=QtWidgets.QLineEdit()

        self.inputInterface=QtWidgets.QComboBox()
        for iface in self.interfaces:
            self.inputInterface.addItem(iface)
        self.inputInterfaceLabel = QtWidgets.QLabel()
        self.inputInterfaceLabel.setText("Interface:")

        self.inputTimeout=QtWidgets.QLineEdit()
        self.inputTimeoutLabel = QtWidgets.QLabel()
        self.inputTimeout.setText("10")
        self.inputTimeoutLabel.setText("Timeout:")

        self.packetTable=PacketTable(self.bottomLayer)


    def _setUpPostiions(self):
        self.mainLayout.addWidget(self.createPacketsLabel)

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
        self.transportLayerLayout.addWidget(self.transportLayerDportLabel)
        self.transportLayerLayout.addWidget(self.transportLayerDportInput)
        self.transportLayerLayout.addWidget(self.inputTimeoutLabel)
        self.transportLayerLayout.addWidget(self.inputTimeout)

        self.mainLayout.addLayout(self.transportLayerLayout)

        self.userDataLayout=QHBoxLayout()
        self.userDataLayout.addWidget(self.userDataLabel)
        self.userDataLayout.addWidget(self.userDataInput)

        self.mainLayout.addLayout(self.userDataLayout)

        self.createButtonLayout=QHBoxLayout()
        self.createButtonLayout.addWidget(self.createPacketsButton)
        self.createButtonLayout.addWidget(self.sendPacketsButton)


        self.mainLayout.addLayout(self.createButtonLayout)

        self.mainLayout.addWidget(self.packetTable)

        self.mainLayout.addLayout(self.bottomLayer)
    
    def createPackets(self):
        self.networkPacket=self.getPacket()
        self.bottomLayer.setCurrentPacket(self.networkPacket)

    def sendPackets(self):
        self.packetTable.removeAllEntries()
        self.networkPacket=self.getPacket()
        self.bottomLayer.setCurrentPacket(self.networkPacket)
        thread=Thread(target=self.handleSendRcv)
        thread.start()

    def handleSendRcv(self):
        timeout=int(self.inputTimeout.text())
        ans=sr1(self.networkPacket,timeout=timeout)
        try:
            if ans:
                for p in ans:
                    self.packetTable.addRowEntry(p)
        except Exception as e:
            print(e)


    def getPacket(self):
        dport=self.transportLayerDportInput.text()
        # linkLayerPacket=Ether()
        networkLayerPacket=IP(src=self.networkSrcInput.text(),dst=self.networkDestInput.text())
        transportProtocol=self.transportSelectBox.currentText()
        if(transportProtocol=="TCP"):
            if dport=="":
                dport=[443,884]
            else:
                dport=int(dport)
            transportLayerPacket=TCP(dport=dport)
        elif(transportProtocol=="UDP"):
            if dport=="":
                dport=53
            transportLayerPacket=UDP(dport=dport)
        elif(transportProtocol=="ICMP"):
            transportLayerPacket=ICMP()
        networkPacket=networkLayerPacket/transportLayerPacket/self.userDataInput.text()
        return networkPacket




        
