from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QToolBar,QAction,QPushButton

class GeneratePacketReportButton(QPushButton):
    def __init__(self,pck):
        super(QPushButton,self).__init__()
        self.pck=pck
        self.clicked.connect(self.generateReport)
    
    def generateReport(self):
        self.pck.pdfdump()