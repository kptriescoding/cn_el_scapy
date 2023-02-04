from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView,QWidget
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView,QWidget,QGridLayout,QHBoxLayout,QLabel

import sys
from scapy.all import IP,TCP,UDP,Ether,conf,get_if_addr,sr,sr1,get_if_list,ICMP,RandNum,sniff,send
import socket
from BottomLayer import BottomLayer
from threading import Thread
from PacketTable import PacketTable
from time import sleep

class ThreeWayHandShake(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setWindowTitle("CN EL")
        self.mainLayout=QVBoxLayout()
        self.networkPacket=None
        self.setLayout(self.mainLayout)
        self._initUI()
        self._setUpPostiions()

    def _initUI(self):

        self.urlLabel = QtWidgets.QLabel()
        self.urlLabel.setText("Enter Dest Host:")
        self.urlInput=QtWidgets.QLineEdit()
        self.urlInput.setText("www.google.com")

        self.startThreeWayHandshakeButton = QtWidgets.QPushButton()
        self.startThreeWayHandshakeButton.setText("Create")
        self.startThreeWayHandshakeButton.clicked.connect(self.startHandshake)

        self.setSYNBtn = QtWidgets.QPushButton()
        self.setSYNBtn.setText("SYN")
        self.setSYNBtn.clicked.connect(self.setSYN)

        self.setSYN_ACKBtn = QtWidgets.QPushButton()
        self.setSYN_ACKBtn.setText("SYN-ACK")
        self.setSYN_ACKBtn.clicked.connect(self.setSYN_ACK)

        self.setACKBtn = QtWidgets.QPushButton()
        self.setACKBtn.setText("ACK")
        self.setACKBtn.clicked.connect(self.setACK)

        self.setGETBtn = QtWidgets.QPushButton()
        self.setGETBtn.setText("GET")
        self.setGETBtn.clicked.connect(self.setGET)

        self.setResponseBtn = QtWidgets.QPushButton()
        self.setResponseBtn.setText("Response")
        self.setResponseBtn.clicked.connect(self.setResponse)

        self.setGETDataBtn = QtWidgets.QPushButton()
        self.setGETDataBtn.setText("GETResponse")
        self.setGETDataBtn.clicked.connect(self.setGETData)

        self.setFINBtn = QtWidgets.QPushButton()
        self.setFINBtn.setText("FIN")
        self.setFINBtn.clicked.connect(self.setFIN)

        self.processLogging=QtWidgets.QTextBrowser()

        self.bottomLayer=BottomLayer()



    def _setUpPostiions(self):

        self.urlInputLayout=QHBoxLayout()
        self.urlInputLayout.addWidget(self.urlLabel)
        self.urlInputLayout.addWidget(self.urlInput)
        self.urlInputLayout.addWidget(self.startThreeWayHandshakeButton)

        self.mainLayout.addLayout(self.urlInputLayout)

        self.packetSetButtons=QHBoxLayout()
        self.packetSetButtons.addWidget(self.setSYNBtn)
        self.packetSetButtons.addWidget(self.setSYN_ACKBtn)
        self.packetSetButtons.addWidget(self.setACKBtn)
        self.packetSetButtons.addWidget(self.setGETBtn)
        self.packetSetButtons.addWidget(self.setResponseBtn)
        self.packetSetButtons.addWidget(self.setGETDataBtn)
        self.packetSetButtons.addWidget(self.setFINBtn)

        self.mainLayout.addLayout(self.packetSetButtons)

        self.mainLayout.addWidget(self.processLogging)

        self.mainLayout.addLayout(self.bottomLayer)

    def setSYN(self):
        if self.SYN:
            self.bottomLayer.setCurrentPacket(self.SYN)
            self.processLogging.setText(self.SYN.show(dump=True))
    
    def setSYN_ACK(self):
        if self.SYNACK:
            self.bottomLayer.setCurrentPacket(self.SYNACK)
            self.processLogging.setText(self.SYNACK.show(dump=True))
    
    def setACK(self):
        if self.ACK:
            self.bottomLayer.setCurrentPacket(self.ACK)
            self.processLogging.setText(self.ACK.show(dump=True))

    def setGET(self):
        if self.GET:
            self.bottomLayer.setCurrentPacket(self.GET)
            self.processLogging.setText(self.GET.show(dump=True))

    def setResponse(self):
        if self.Response:
            self.bottomLayer.setCurrentPacket(self.Response)
            self.processLogging.setText(self.Response.show(dump=True))
    
    def setFIN(self):
        if self.FIN:
            self.bottomLayer.setCurrentPacket(self.FIN)
            self.processLogging.setText(self.FIN.show(dump=True))
    
    def setGETData(self):
        if self.GETData:
            self.bottomLayer.setCurrentPacket(self.GETData)
            self.processLogging.setText(self.GETData.show(dump=True))

    def startHandshake(self):
        hostUrl=self.urlInput.text()
        get = "GET / HTTP/1.1\r\nHost:"+hostUrl+"\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.110 Chrome/58.0.3029.110 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.8\r\n\r\n"
        ip=IP(dst=hostUrl)
        port=RandNum(1024,65535)
        self.SYN=ip/TCP(sport=port, dport=80, flags="S", seq=42)
        self.processLogging.setText("[*] Sending SYN packet...")
        self.SYNACK=sr1(self.SYN)
        sleep(1)
        self.processLogging.setText(self.processLogging.toPlainText()+"\n[*] Sent SYN Packets...\n[*] Recieved SYNACK Packets...")
        self.ACK=ip/TCP(sport=self.SYNACK.dport, dport=80, flags="A", seq=self.SYNACK.ack, ack=self.SYNACK.seq + 1)
        self.processLogging.setText(self.processLogging.toPlainText()+"\n[*] Sending ACK packet....")
        send(self.ACK)
        sleep(1)
        self.processLogging.setText(self.processLogging.toPlainText()+"\n[*] Sending GET packet....")
        self.GET=self.ACK/get
        self.Response=sr1(self.GET)
        sleep(1)
        filter="host "+hostUrl
        self.GETData=sniff(count=1,filter=filter)
        self.GETData=self.GETData[0]
        sleep(1)
        self.processLogging.setText(self.processLogging.toPlainText()+"\n[*] Closing Connection....\n[*] Sending FIN packet...")
        self.FIN=ip/TCP(sport=self.SYNACK.dport, dport=80, flags="F", seq=self.SYNACK.ack, ack=self.SYNACK.seq + 1)
        send(self.FIN)
        sleep(1)
        self.processLogging.setText(self.processLogging.toPlainText()+"\n[*] Done!")
        self.bottomLayer.setCurrentPacket(self.GETData)

    





        
