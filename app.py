from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QStackedWidget
import sys
from PackerSniffer import PacketSniffer
from TopToolbar import TopToolbar
from SendAndRecievePackets import SendAndReciecePackets


def startApplication():
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    mainWidget=QStackedWidget()
    mainWindow.setCentralWidget(mainWidget)
    mainWindow.resize(900,700)
    packetSnifferWidget=PacketSniffer()
    sendAndReciecePacketsWidget=SendAndReciecePackets()
    mainWidget.addWidget(packetSnifferWidget)
    mainWidget.addWidget(sendAndReciecePacketsWidget)
    topToolbar=TopToolbar(mainWidget)
    mainWindow.addToolBar(topToolbar)
    mainWidget.setCurrentIndex(1)
    mainWindow.show()


    sys.exit(app.exec_())

startApplication()
    

