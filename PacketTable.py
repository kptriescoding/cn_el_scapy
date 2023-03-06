from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView,QWidget,QGridLayout,QHBoxLayout,QLabel
from TopToolbar import TopToolbar
import sys
from scapy.all import sniff,get_if_list,IP,ARP
import socket
from BottomLayer import BottomLayer
from threading import Thread

class PacketTable(QTableWidget):
    def __init__(self,bottomLayer):
        super(QTableWidget,self).__init__()
        self.bottomLayer=bottomLayer
        self.packetList=[]
        self.initpacketTables()
    
    def initpacketTables(self):
        columns=["No","src","dest","time","type","load","protocol","length"]
        self.setColumnCount(8)
        self.setHorizontalHeaderLabels(columns)
        self.horizontalHeader().setStretchLastSection(True)  
        self.horizontalHeader().setSectionResizeMode( QHeaderView.Stretch)  
        self.verticalHeader().setVisible(False)
        self.clicked.connect(self.onClickTable)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    
    def onClickTable(self):
        self.bottomLayer.setCurrentPacket(self.packetList[self.currentIndex().row()])

    def addRowEntry(self,s):
        try:
            # print(s.show())
            self.setRowCount(self.rowCount()+1)
            self.setItem(self.rowCount()-1,0,QTableWidgetItem(str(self.rowCount())))
            try:
                self.setItem(self.rowCount()-1,1,QTableWidgetItem(s[IP].src))
                self.setItem(self.rowCount()-1,2,QTableWidgetItem(s[IP].dst))
            except:
                try:
                    self.setItem(self.rowCount()-1,1,QTableWidgetItem(s[ARP].psrc))
                    self.setItem(self.rowCount()-1,2,QTableWidgetItem(s[ARP].pdst))
                except:
                    self.setItem(self.rowCount()-1,1,QTableWidgetItem(s[1].src))
                    self.setItem(self.rowCount()-1,2,QTableWidgetItem(s[1].dst))
            
            self.setItem(self.rowCount()-1,3,QTableWidgetItem(str(s.time)))
            try:
                self.setItem(self.rowCount()-1,5,QTableWidgetItem(str(s.load)))
            except:
                self.setItem(self.rowCount()-1,5,QTableWidgetItem(str("-")))
            try:
                ipType=s.type
            except:
                ipType=-1
            if(ipType==2048 or ipType==-1):
                self.setItem(self.rowCount()-1,4,QTableWidgetItem(str("IPV4")))
                self.setItem(self.rowCount()-1,6,QTableWidgetItem(str(self.proto_name_by_num(s.proto))))
                self.setItem(self.rowCount()-1,7,QTableWidgetItem(str(s.len)))
            elif(ipType==34525):
                self.setItem(self.rowCount()-1,4,QTableWidgetItem(str("IPV6")))
                self.setItem(self.rowCount()-1,6,QTableWidgetItem(str(self.proto_name_by_num(s.nh))))
                self.setItem(self.rowCount()-1,7,QTableWidgetItem(str(s.plen)))
            elif(ipType==2054):
                self.setItem(self.rowCount()-1,4,QTableWidgetItem(str("ARP")))
                self.setItem(self.rowCount()-1,6,QTableWidgetItem("-"))
                self.setItem(self.rowCount()-1,7,QTableWidgetItem(str(s.plen)))
            self.packetList.append(s)
        except Exception as e:
            print(e)
            self.setRowCount(self.rowCount()-1)

    def proto_name_by_num(self,proto_num):
        for name,num in vars(socket).items():
            if name.startswith("IPPROTO") and proto_num == num:
                return name[8:]
        return "Protocol not found"
    
    def removeAllEntries(self):
        self.setRowCount(0)
        self.packetList=[]