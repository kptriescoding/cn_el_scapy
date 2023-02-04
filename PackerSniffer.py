from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView,QWidget,QGridLayout,QHBoxLayout,QLabel
from TopToolbar import TopToolbar
import sys
from scapy.all import sniff,get_if_list
import socket
from BottomLayer import BottomLayer
from threading import Thread
from PacketTable import PacketTable

class PacketSniffer(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.stopThread=True
        self.interfaces=get_if_list()
        self.setWindowTitle("CN EL")
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self._initUI()
        self._addUIElements()
    
    def _initUI(self):
        self.sniffPacketsBtn=QtWidgets.QPushButton()
        self.sniffPacketsBtn.setText("Sniff Packets")
        self.sniffPacketsBtn.clicked.connect(self.sniffPacketsBtnClicked)

        self.emptyTableBtn=QtWidgets.QPushButton()
        self.emptyTableBtn.setText("Empty Table")
        self.emptyTableBtn.clicked.connect(self.emptyTableBtnClicked)

        self.inputTakerLayout=QHBoxLayout()
        self.inputCountLabel=QLabel()
        self.inputCountLabel.setText("Enter Count:")

        self.inputCount=QtWidgets.QLineEdit()

        self.inputIPLabel=QLabel()
        self.inputIPLabel.setText("Enter IP:")
        self.inputIP=QtWidgets.QLineEdit()

        self.inputProtoLabel=QLabel()
        self.inputProtoLabel.setText("Enter Protocol:")
        self.inputProto=QtWidgets.QLineEdit()

        self.inputInterface=QtWidgets.QComboBox()
        for iface in self.interfaces:
            self.inputInterface.addItem(iface)
        self.inputInterface.addItem("All")

        self.inputMode=QtWidgets.QComboBox()
        self.inputMode.addItem("Specific")
        self.inputMode.addItem("Unlimited")

        self.stopSniffBtn=QtWidgets.QPushButton()
        self.stopSniffBtn.setText("Stop Sniffing")
        self.stopSniffBtn.clicked.connect(self.stopSniffBtnClicked)

        self.BtnLayout=QHBoxLayout()

        self.bottomLayer=BottomLayer()
        self.packetTable=PacketTable(self.bottomLayer)


    def stopSniffBtnClicked(self):
            self.stopThread=True
    
    def emptyTableBtnClicked(self):
        self.packetTable.removeAllEntries()
            


    def _addUIElements(self):
        self.inputTakerLayout.addWidget(self.inputInterface)
        self.inputTakerLayout.addWidget(self.inputMode)
        self.inputTakerLayout.addWidget(self.inputCountLabel)
        self.inputTakerLayout.addWidget(self.inputCount)
        self.inputTakerLayout.addWidget(self.inputIPLabel)
        self.inputTakerLayout.addWidget(self.inputIP)
        self.inputTakerLayout.addWidget(self.inputProtoLabel)
        self.inputTakerLayout.addWidget(self.inputProto)
        self.mainLayout.addLayout(self.inputTakerLayout)
        
        self.BtnLayout.addWidget(self.sniffPacketsBtn)
        self.BtnLayout.addWidget(self.stopSniffBtn)
        self.BtnLayout.addWidget(self.emptyTableBtn)
        self.mainLayout.addLayout(self.BtnLayout)

        self.mainLayout.addWidget(self.packetTable)

        self.mainLayout.addLayout(self.bottomLayer)


    def sniffPacketsBtnClicked(self):

        if  not self.stopThread:
            return
        self.stopThread=False
        self.noOfPacketsSniffed=0
        self.iface=self.inputInterface.currentText()
        if self.iface == "All":
            self.iface=self.interfaces
        self.mode=self.inputMode.currentText()
        self.count=self.inputCount.text()
        self.IP=self.inputIP.text()
        self.proto=self.inputProto.text()
        self.filterText=""
        if(self.proto!=""):
            self.filterText+=self.proto+" and "
        if(self.IP!=""):
            self.filterText+="host "+self.IP
        if self.count=="":
            self.count=10
        else:
            self.count=int(self.count)

        if self.mode=="Specific":
            self.Thread=Thread(target=self.packetSpecificSniffer)
        elif self.mode=="Unlimited":
            self.Thread=Thread(target=self.packetSniffer)
        self.Thread.start()


    def packetSniffer(self):
        print(self.filterText)
        try:
            while True:
                sniff(count=1,prn=self.checkCapture,filter=self.filterText,iface=self.iface)
                if(self.stopThread):
                    break
            self.stopThread=True
        except Exception as e:
            pass

    def packetSpecificSniffer(self):
        try:
            while self.noOfPacketsSniffed<self.count:
                sniff(count=1,prn=self.checkCapture,filter=self.filterText,iface=self.iface)
                if self.stopThread:
                    break
            self.stopThread=True
        except Exception as e:
            pass

    def checkCapture(self,s):  
        self.packetTable.addRowEntry(s)          
        self.noOfPacketsSniffed+=1
    