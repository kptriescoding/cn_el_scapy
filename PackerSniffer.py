from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView,QWidget,QGridLayout,QHBoxLayout,QLabel
from TopToolbar import TopToolbar
import sys
from scapy.all import *
import socket
from GeneratePacketReportButton import GeneratePacketReportButton

class PacketSniffer(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.count=10
        self.r_count=0
        self.setWindowTitle("CN EL")
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.initpacketTables()
        self._initUI()
        self._addUIElements()
    
    def _initUI(self):
        self.sniffPacketsBtn=QtWidgets.QPushButton()
        self.sniffPacketsBtn.setText("Sniff Packets")
        self.sniffPacketsBtn.clicked.connect(self.sniffPacketsBtnClicked)
        self.inputTakerLayout=QHBoxLayout()
        self.inputCountLabel=QLabel()
        self.inputCountLabel.setText("Enter Count:")
        self.inputCount=QtWidgets.QLineEdit()
        self.inputCount.move(25,100)

    def _addUIElements(self):
        self.inputTakerLayout.addWidget(self.inputCountLabel)
        self.inputTakerLayout.addWidget(self.inputCount)
        self.mainLayout.addLayout(self.inputTakerLayout)
        self.mainLayout.addWidget(self.sniffPacketsBtn)
        self.mainLayout.addWidget(self.packetTable)


    def initpacketTables(self):
        columns=["src","dest","time","type","load","protocol","length","generate"]
        self.packetTable=QTableWidget()
        self.packetTable.setColumnCount(8)
        self.packetTable.setHorizontalHeaderLabels(columns)


    def sniffPacketsBtnClicked(self):
        if(self.inputCount.text()==""):
             self.count=10
        else:
             self.count=int(self.inputCount.text())
        sniff(count=self.count,prn=self.checkCapture)
        self.packetTable.horizontalHeader().setStretchLastSection(True)  
        self.packetTable.horizontalHeader().setSectionResizeMode( QHeaderView.Stretch)  
    def proto_name_by_num(self,proto_num):
        for name,num in vars(socket).items():
            if name.startswith("IPPROTO") and proto_num == num:
                return name[8:]
        return "Protocol not found"

    def checkCapture(self,s):
        try:
            # print(self.packetTable.rowCount())
            if s[1].src=="127.0.0.1":
                s.show()
            self.packetTable.setRowCount(self.packetTable.rowCount()+1)
            self.packetTable.setItem(self.r_count,0,QTableWidgetItem(s[1].src))
            self.packetTable.setItem(self.r_count,1,QTableWidgetItem(s[1].dst))
            self.packetTable.setItem(self.r_count,2,QTableWidgetItem(str(s.time)))
            try:
                self.packetTable.setItem(self.r_count,4,QTableWidgetItem(str(s.load)))
            except:
                self.packetTable.setItem(self.r_count,4,QTableWidgetItem(str("-")))
            if(s.type==2048):
                self.packetTable.setItem(self.r_count,3,QTableWidgetItem(str("IPV4")))
                self.packetTable.setItem(self.r_count,5,QTableWidgetItem(str(self.proto_name_by_num(s.proto))))
                self.packetTable.setItem(self.r_count,6,QTableWidgetItem(str(s.len)))
            elif(s.type==34525):
                self.packetTable.setItem(self.r_count,3,QTableWidgetItem(str("IPV6")))
                self.packetTable.setItem(self.r_count,5,QTableWidgetItem(str(self.proto_name_by_num(s.nh))))
                self.packetTable.setItem(self.r_count,6,QTableWidgetItem(str(s.plen)))
            btn=GeneratePacketReportButton(s)
            btn.setText("Generate")
            self.packetTable.setCellWidget(self.r_count,7,btn)
            self.r_count+=1
        except Exception as e:
            self.packetTable.setRowCount(self.packetTable.rowCount()-1)
            pass
