from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from PackerSniffer import PacketSniffer


def startApplication():
    app=QApplication(sys.argv)
    packetSnifferWindow=PacketSniffer()
    packetSnifferWindow.show()
    sys.exit(app.exec_())

startApplication()
    

