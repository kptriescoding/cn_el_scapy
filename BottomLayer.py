from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QToolBar,QAction,QPushButton,QVBoxLayout,QHBoxLayout
from scapy.all import raw,hexdump

class BottomLayer(QVBoxLayout):
    def __init__(self):
        super(QVBoxLayout,self).__init__()
        self.packet=None
        self._initUI()
        self._addUIElements()
        
    def _initUI(self):
        self.bottomText=QtWidgets.QTextBrowser()

        self.bottomButtonLayer=QHBoxLayout()
        self.generateReportBtn=QPushButton()
        self.generateReportBtn.setText("Generate PDF")
        self.generateReportBtn.clicked.connect(self.generateReport)
        self.hexDataBtn=QPushButton()
        self.hexDataBtn.setText("Hex Data")
        self.hexDataBtn.clicked.connect(self.changeHexData)
        self.rawDataBtn=QPushButton()
        self.rawDataBtn.setText("Raw Data")
        self.rawDataBtn.clicked.connect(self.changeRawData)

    def _addUIElements(self):
        self.bottomButtonLayer.addWidget(self.generateReportBtn)
        self.bottomButtonLayer.addWidget(self.hexDataBtn)
        self.bottomButtonLayer.addWidget(self.rawDataBtn)
        self.addWidget(self.bottomText)
        self.addLayout(self.bottomButtonLayer)

    def generateReport(self):
        if(self.packet):
            self.packet.pdfdump()
    
    def changeHexData(self):
        if self.packet:
            self.bottomText.setText(hexdump(self.packet,dump=True))

    def changeRawData(self):
        if self.packet:
            self.bottomText.setText(str(raw(self.packet)))

    def setCurrentPacket(self,packet):
        self.packet=packet
        self.changeHexData()
