from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView
from TopToolbar import TopToolbar
import sys
from scapy.all import sniff
import socket
from GeneratePacketReportButton import GeneratePacketReportButton

class PacketSniffer(QMainWindow):
    def __init__(self):
        self.count=10
        self.r_count=0
        super(QMainWindow,self).__init__()
        self.resize(800,800)
        self.setWindowTitle("CN EL")
        self._initUI()
    
    def _initUI(self):
        self.topToolbar=TopToolbar(self)
        self.topToolbar.setPacketSnifferWindow(self)
        self.bt=QtWidgets.QPushButton(self)
        self.bt.setText("Sniff Packets")
        self.bt.clicked.connect(self.clicked)
        self.bt.move(25,75)
        self.inputCount=QtWidgets.QLineEdit(self)
        self.inputCount.move(25,100)
        self.inputCount.placeholderText="Enter Count"

    def initpacketTables(self):
        columns=["src","dest","time","type","load","protocol","length","generate"]
        self.packetTable=QTableWidget()
        self.packetTable.setColumnCount(8)
        self.packetTable.setRowCount(self.count)
        self.packetTable.setHorizontalHeaderLabels(columns)


    def clicked(self):
        if(self.inputCount.text()==""):
             self.count=10
        else:
             self.count=int(self.inputCount.text())
        self.r_count=0
        self.initpacketTables()
        capture=sniff(count=self.count)
        capture.summary(self.checkCapture)
        self.packetTable.horizontalHeader().setStretchLastSection(True)  
        self.packetTable.horizontalHeader().setSectionResizeMode( QHeaderView.Stretch)  
        self.packetTable.showMaximized() 

    def proto_name_by_num(self,proto_num):
        for name,num in vars(socket).items():
            if name.startswith("IPPROTO") and proto_num == num:
                return name[8:]
        return "Protocol not found"

    def checkCapture(self,s):
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
        self.bt.move(25,75)
        self.r_count+=1
        
