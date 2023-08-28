
import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMainWindow,QDialog, QApplication, QAction, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from labgui4 import *
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber
import datetime

tday=datetime.date.today()




class apped(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.MOTOR1action.clicked.connect(self.message1)
        self.ui.MOTOR2action.clicked.connect(self.message2)
        self.ui.MOTOR3action.clicked.connect(self.message3)
        self.ui.MOTOR4action.clicked.connect(self.message4)
        self.show()
  
    def message1(self):
        self.ui.speed1.setText("1")
        self.ui.v1_1.setText("2")
        self.ui.v1_2.setText("3")
        self.ui.v1_3.setText("4")
        self.ui.vC1_1.setText("5")
        self.ui.C1_2.setText("6")
        self.ui.C1_3.setText("7")
        self.ui.A1_1.setText("8")
        self.ui.A1_2.setText("9")
        self.ui.A1_3.setText("10")
        self.ui.PA1_1.setText("11")
        self.ui.PA1_2.setText("12")
        self.ui.PA1_3.setText("13")
        #self.update1()
        #self.erase2
        #self.erase3
        #self.erase4
        
    def message2(self):
        self.ui.speed1_2.setText("1")
        self.ui.v1_4.setText("2")
        self.ui.v1_5.setText("3")
        self.ui.v1_6.setText("4")
        self.ui.vC1_2.setText("5")
        self.ui.C1_4.setText("6")
        self.ui.C1_5.setText("7")
        self.ui.A1_4.setText("8")
        self.ui.A1_5.setText("9")
        self.ui.A1_6.setText("10")
        self.ui.PA1_4.setText("11")
        self.ui.PA1_5.setText("12")
        self.ui.PA1_6.setText("13")
        #self.update2()
        #self.erase1
        #self.erase3
        #self.erase4
        
     

     

        
        
    def message3(self):
        self.ui.speed1_3.setText("1")
        self.ui.v1_7.setText("2")
        self.ui.v1_8.setText("3")
        self.ui.v1_9.setText("4")
        self.ui.vC1_3.setText("5")
        self.ui.C1_6.setText("6")
        self.ui.C1_7.setText("7")
        self.ui.A1_7.setText("8")
        self.ui.A1_8.setText("9")
        self.ui.A1_9.setText("10")
        self.ui.PA1_7.setText("11")
        self.ui.PA1_8.setText("12")
        self.ui.PA1_9.setText("13")
        #self.update3()
        #self.erase2
        #self.erase1
        #self.erase4
        
        
    def message4(self):
        self.ui.speed1_4.setText("1")
        self.ui.v1_10.setText("2")
        self.ui.v1_11.setText("3")
        self.ui.v1_12.setText("4")
        self.ui.vC1_4.setText("5")
        self.ui.C1_8.setText("6")
        self.ui.C1_9.setText("7")
        self.ui.A1_10.setText("8")
        self.ui.A1_11.setText("9")
        self.ui.A1_12.setText("10")
        self.ui.PA1_10.setText("11")
        self.ui.PA1_11.setText("12")
        self.ui.PA1_12.setText("13")
        #self.update4()
        #self.erase2
        #self.erase3
        #self.erase1

    def erase1(self):
        self.ui.speed1.setText("")
        self.ui.v1_1.setText("")
        self.ui.v1_2.setText("")
        self.ui.v1_3.setText("")
        self.ui.vC1_1.setText("")
        self.ui.C1_2.setText("")
        self.ui.C1_3.setText("")
        self.ui.A1_1.setText("")
        self.ui.A1_2.setText("")
        self.ui.A1_3.setText("")
        self.ui.PA1_1.setText("")
        self.ui.PA1_2.setText("")
        self.ui.PA1_3.setText("")

    def erase2(self):
        self.ui.speed1_2.setText("")
        self.ui.v1_4.setText("")
        self.ui.v1_5.setText("")
        self.ui.v1_6.setText("")
        self.ui.vC1_2.setText("")
        self.ui.C1_4.setText("")
        self.ui.C1_5.setText("")
        self.ui.A1_4.setText("")
        self.ui.A1_5.setText("")
        self.ui.A1_6.setText("")
        self.ui.PA1_4.setText("")
        self.ui.PA1_5.setText("")
        self.ui.PA1_6.setText("")

    def erase3(self):
        self.ui.speed1_3.setText("")
        self.ui.v1_7.setText("")
        self.ui.v1_8.setText("")
        self.ui.v1_9.setText("")
        self.ui.vC1_3.setText("")
        self.ui.C1_6.setText("")
        self.ui.C1_7.setText("")
        self.ui.A1_7.setText("")
        self.ui.A1_8.setText("")
        self.ui.A1_9.setText("")
        self.ui.PA1_7.setText("")
        self.ui.PA1_8.setText("")
        self.ui.PA1_9.setText("")
        
    def erase4(self):
        self.ui.speed1_4.setText("")
        self.ui.v1_10.setText("")
        self.ui.v1_11.setText("")
        self.ui.v1_12.setText("")
        self.ui.vC1_4.setText("")
        self.ui.C1_8.setText("")
        self.ui.C1_9.setText("")
        self.ui.A1_10.setText("")
        self.ui.A1_11.setText("")
        self.ui.A1_12.setText("")
        self.ui.PA1_10.setText("")
        self.ui.PA1_11.setText("")
        self.ui.PA1_12.setText("")
        
    def update4(self):
        self.speed1_4.adjustSize()
        self.v1_10.adjustSize()
        self.v1_11.adjustSize()
        self.v1_12.adjustSize()
        self.vC1_4.adjustSize()
        self.C1_8.adjustSize()
        self.C1_9.adjustSize()
        self.A1_10.adjustSize()
        self.A1_11.adjustSize()
        self.A1_12.adjustSize()
        self.PA1_10.adjustSize()
        self.PA1_11.adjustSize()
        self.PA1_12.adjustSize()
    def update3(self):
        self.speed1_3.adjustSize()
        self.v1_7.adjustSize()
        self.v1_8.adjustSize()
        self.v1_9.adjustSize()
        self.vC1_3.adjustSize()
        self.C1_6.adjustSize()
        self.C1_7.adjustSize()
        self.A1_7.adjustSize()
        self.A1_8.adjustSize()
        self.A1_9.adjustSize()
        self.PA1_7.adjustSize()
        self.PA1_8.adjustSize()
        self.PA1_9.adjustSize()
    def update2(self):
        self.speed1_2.adjustSize()
        self.v1_4.adjustSize()
        self.v1_5.adjustSize()
        self.v1_6.adjustSize()
        self.vC1_2.adjustSize()
        self.C1_4.adjustSize()
        self.C1_5.adjustSize()
        self.A1_4.adjustSize()
        self.A1_5.adjustSize()
        self.A1_6.adjustSize()
        self.PA1_4.adjustSize()
        self.PA1_5.adjustSize()
        self.PA1_6.adjustSize()
    def update1(self):
        self.speed1.adjustSize()
        self.v1_1.adjustSize()
        self.v1_2.adjustSize()
        self.v1_3.adjustSize()
        self.vC1_1.adjustSize()
        self.C1_2.adjustSize()
        self.C1_3.adjustSize()
        self.A1_1.adjustSize()
        self.A1_2.adjustSize()
        self.A1_3.adjustSize()
        self.PA1_1.adjustSize()
        self.PA1_2.adjustSize()
        self.PA1_3.adjustSize()
        
        
        
       
        

if __name__=="__main__":
	app = QApplication(sys.argv)
	r = apped()
	r.show()
	sys.exit(app.exec_())
