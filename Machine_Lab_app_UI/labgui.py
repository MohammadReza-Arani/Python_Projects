# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'labgui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 750)

        self.motor3text = QtWidgets.QLabel(Dialog)
        self.motor3text.setGeometry(QtCore.QRect(480, 470, 211, 281))
        self.motor3text.setText("")
        self.motor3text.setPixmap(QtGui.QPixmap("filledtext2.jpg"))
        self.motor3text.setObjectName("motor3text")

        self.motor4text = QtWidgets.QLabel(Dialog)
        self.motor4text.setGeometry(QtCore.QRect(700, 470, 221, 281))
        self.motor4text.setText("")
        self.motor4text.setPixmap(QtGui.QPixmap("filledtext2.jpg"))
        self.motor4text.setObjectName("motor4text")

        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(0, 0, 900, 481))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("background.jpg"))
        self.background.setObjectName("background")

        self.MOTOR1action = QtWidgets.QPushButton(Dialog)
        self.MOTOR1action.setGeometry(QtCore.QRect(0, 380, 131, 101))
        self.MOTOR1action.setObjectName("MOTOR1action")
        actIcon = QtGui.QIcon()
        actIcon.addPixmap(QtGui.QPixmap("kontor.jpg"))
        self.MOTOR1action.setIcon(actIcon)
        self.MOTOR1action.setIconSize(QtCore.QSize(131, 101))

        self.MOTOR2action = QtWidgets.QPushButton(Dialog)
        self.MOTOR2action.setGeometry(QtCore.QRect(220, 380, 131, 101))
        self.MOTOR2action.setObjectName("MOTOR2action")
        actIcon.addPixmap(QtGui.QPixmap("kontor.jpg"))
        self.MOTOR2action.setIcon(actIcon)
        self.MOTOR2action.setIconSize(QtCore.QSize(131, 101))
        

        self.MOTOR3action = QtWidgets.QPushButton(Dialog)
        self.MOTOR3action.setGeometry(QtCore.QRect(480, 380, 131, 101))
        self.MOTOR3action.setObjectName("MOTOR3action")
        actIcon.addPixmap(QtGui.QPixmap("kontor.jpg"))
        self.MOTOR3action.setIcon(actIcon)
        self.MOTOR3action.setIconSize(QtCore.QSize(131, 101))

        self.MOTOR4action = QtWidgets.QPushButton(Dialog)
        self.MOTOR4action.setGeometry(QtCore.QRect(700, 380, 131, 101))
        self.MOTOR4action.setObjectName("MOTOR4action")
        actIcon.addPixmap(QtGui.QPixmap("kontor.jpg"))
        self.MOTOR4action.setIcon(actIcon)
        self.MOTOR4action.setIconSize(QtCore.QSize(131, 101))

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(710, 0, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        self.motor2text = QtWidgets.QLabel(Dialog)
        self.motor2text.setGeometry(QtCore.QRect(220, 470, 211, 281))
        self.motor2text.setText("")
        self.motor2text.setPixmap(QtGui.QPixmap("filledtext2.jpg"))
        self.motor2text.setObjectName("motor2text")

        self.motor1text = QtWidgets.QLabel(Dialog)
        self.motor1text.setGeometry(QtCore.QRect(0, 470, 211, 281))
        self.motor1text.setText("")
        self.motor1text.setPixmap(QtGui.QPixmap("filledtext2.jpg"))
        self.motor1text.setObjectName("motor1text")

        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 492, 71, 221))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.speed1_2 = QtWidgets.QLabel(self.layoutWidget)
        self.speed1_2.setText("")
        self.speed1_2.setObjectName("speed1_2")

        self.verticalLayout_2.addWidget(self.speed1_2)

        self.v1_4 = QtWidgets.QLabel(self.layoutWidget)
        self.v1_4.setText("")
        self.v1_4.setObjectName("v1_4")

        self.verticalLayout_2.addWidget(self.v1_4)

        self.v1_5 = QtWidgets.QLabel(self.layoutWidget)
        self.v1_5.setText("")
        self.v1_5.setObjectName("v1_5")

        self.verticalLayout_2.addWidget(self.v1_5)

        self.v1_6 = QtWidgets.QLabel(self.layoutWidget)
        self.v1_6.setText("")
        self.v1_6.setObjectName("v1_6")

        self.verticalLayout_2.addWidget(self.v1_6)

        self.vC1_2 = QtWidgets.QLabel(self.layoutWidget)
        self.vC1_2.setText("")
        self.vC1_2.setObjectName("vC1_2")

        self.verticalLayout_2.addWidget(self.vC1_2)

        self.C1_4 = QtWidgets.QLabel(self.layoutWidget)
        self.C1_4.setText("")
        self.C1_4.setObjectName("C1_4")

        self.verticalLayout_2.addWidget(self.C1_4)

        self.C1_5 = QtWidgets.QLabel(self.layoutWidget)
        self.C1_5.setText("")
        self.C1_5.setObjectName("C1_5")

        self.verticalLayout_2.addWidget(self.C1_5)

        self.A1_4 = QtWidgets.QLabel(self.layoutWidget)
        self.A1_4.setText("")
        self.A1_4.setObjectName("A1_4")

        self.verticalLayout_2.addWidget(self.A1_4)

        self.A1_5 = QtWidgets.QLabel(self.layoutWidget)
        self.A1_5.setText("")
        self.A1_5.setObjectName("A1_5")

        self.verticalLayout_2.addWidget(self.A1_5)

        self.A1_6 = QtWidgets.QLabel(self.layoutWidget)
        self.A1_6.setText("")
        self.A1_6.setObjectName("A1_6")

        self.verticalLayout_2.addWidget(self.A1_6)

        self.PA1_4 = QtWidgets.QLabel(self.layoutWidget)
        self.PA1_4.setText("")
        self.PA1_4.setObjectName("PA1_4")

        self.verticalLayout_2.addWidget(self.PA1_4)

        self.PA1_5 = QtWidgets.QLabel(self.layoutWidget)
        self.PA1_5.setText("")
        self.PA1_5.setObjectName("PA1_5")

        self.verticalLayout_2.addWidget(self.PA1_5)

        self.PA1_6 = QtWidgets.QLabel(self.layoutWidget)
        self.PA1_6.setText("")
        self.PA1_6.setObjectName("PA1_6")

        self.verticalLayout_2.addWidget(self.PA1_6)

        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(570, 490, 71, 221))
        self.layoutWidget_2.setObjectName("layoutWidget_2")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.speed1_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.speed1_3.setText("")
        self.speed1_3.setObjectName("speed1_3")

        self.verticalLayout_3.addWidget(self.speed1_3)

        self.v1_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.v1_7.setText("")
        self.v1_7.setObjectName("v1_7")

        self.verticalLayout_3.addWidget(self.v1_7)

        self.v1_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.v1_8.setText("")
        self.v1_8.setObjectName("v1_8")

        self.verticalLayout_3.addWidget(self.v1_8)

        self.v1_9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.v1_9.setText("")
        self.v1_9.setObjectName("v1_9")

        self.verticalLayout_3.addWidget(self.v1_9)

        self.vC1_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.vC1_3.setText("")
        self.vC1_3.setObjectName("vC1_3")

        self.verticalLayout_3.addWidget(self.vC1_3)

        self.C1_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.C1_6.setText("")
        self.C1_6.setObjectName("C1_6")

        self.verticalLayout_3.addWidget(self.C1_6)

        self.C1_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.C1_7.setText("")
        self.C1_7.setObjectName("C1_7")

        self.verticalLayout_3.addWidget(self.C1_7)

        self.A1_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.A1_7.setText("")
        self.A1_7.setObjectName("A1_7")

        self.verticalLayout_3.addWidget(self.A1_7)

        self.A1_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.A1_8.setText("")
        self.A1_8.setObjectName("A1_8")

        self.verticalLayout_3.addWidget(self.A1_8)

        self.A1_9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.A1_9.setText("")
        self.A1_9.setObjectName("A1_9")

        self.verticalLayout_3.addWidget(self.A1_9)

        self.PA1_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.PA1_7.setText("")
        self.PA1_7.setObjectName("PA1_7")

        self.verticalLayout_3.addWidget(self.PA1_7)

        self.PA1_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.PA1_8.setText("")
        self.PA1_8.setObjectName("PA1_8")

        self.verticalLayout_3.addWidget(self.PA1_8)

        self.PA1_9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.PA1_9.setText("")
        self.PA1_9.setObjectName("PA1_9")

        self.verticalLayout_3.addWidget(self.PA1_9)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(790, 492, 71, 221))
        self.layoutWidget_3.setObjectName("layoutWidget_3")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.speed1_4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.speed1_4.setText("")
        self.speed1_4.setObjectName("speed1_4")

        self.verticalLayout_4.addWidget(self.speed1_4)

        self.v1_10 = QtWidgets.QLabel(self.layoutWidget_3)
        self.v1_10.setText("")
        self.v1_10.setObjectName("v1_10")

        self.verticalLayout_4.addWidget(self.v1_10)

        self.v1_11 = QtWidgets.QLabel(self.layoutWidget_3)
        self.v1_11.setText("")
        self.v1_11.setObjectName("v1_11")

        self.verticalLayout_4.addWidget(self.v1_11)

        self.v1_12 = QtWidgets.QLabel(self.layoutWidget_3)
        self.v1_12.setText("")
        self.v1_12.setObjectName("v1_12")

        self.verticalLayout_4.addWidget(self.v1_12)

        self.vC1_4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.vC1_4.setText("")
        self.vC1_4.setObjectName("vC1_4")

        self.verticalLayout_4.addWidget(self.vC1_4)

        self.C1_8 = QtWidgets.QLabel(self.layoutWidget_3)
        self.C1_8.setText("")
        self.C1_8.setObjectName("C1_8")

        self.verticalLayout_4.addWidget(self.C1_8)

        self.C1_9 = QtWidgets.QLabel(self.layoutWidget_3)
        self.C1_9.setText("")
        self.C1_9.setObjectName("C1_9")

        self.verticalLayout_4.addWidget(self.C1_9)

        self.A1_10 = QtWidgets.QLabel(self.layoutWidget_3)
        self.A1_10.setText("")
        self.A1_10.setObjectName("A1_10")

        self.verticalLayout_4.addWidget(self.A1_10)

        self.A1_11 = QtWidgets.QLabel(self.layoutWidget_3)
        self.A1_11.setText("")
        self.A1_11.setObjectName("A1_11")

        self.verticalLayout_4.addWidget(self.A1_11)

        self.A1_12 = QtWidgets.QLabel(self.layoutWidget_3)
        self.A1_12.setText("")
        self.A1_12.setObjectName("A1_12")

        self.verticalLayout_4.addWidget(self.A1_12)

        self.PA1_10 = QtWidgets.QLabel(self.layoutWidget_3)
        self.PA1_10.setText("")
        self.PA1_10.setObjectName("PA1_10")

        self.verticalLayout_4.addWidget(self.PA1_10)

        self.PA1_11 = QtWidgets.QLabel(self.layoutWidget_3)
        self.PA1_11.setText("")
        self.PA1_11.setObjectName("PA1_11")

        self.verticalLayout_4.addWidget(self.PA1_11)

        self.PA1_12 = QtWidgets.QLabel(self.layoutWidget_3)
        self.PA1_12.setText("")
        self.PA1_12.setObjectName("PA1_12")

        self.verticalLayout_4.addWidget(self.PA1_12)

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(90, 490, 71, 231))
        self.widget.setObjectName("widget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.speed1 = QtWidgets.QLabel(self.widget)
        self.speed1.setText("1")
        self.speed1.setObjectName("speed1")
        self.verticalLayout.addWidget(self.speed1)
        
        self.v1_1 = QtWidgets.QLabel(self.widget)
        self.v1_1.setText("")
        self.v1_1.setObjectName("v1_1")
        self.verticalLayout.addWidget(self.v1_1)
        
        self.v1_2 = QtWidgets.QLabel(self.widget)
        self.v1_2.setText("")
        self.v1_2.setObjectName("v1_2")
        self.verticalLayout.addWidget(self.v1_2)
        
        self.v1_3 = QtWidgets.QLabel(self.widget)
        self.v1_3.setText("")
        self.v1_3.setObjectName("v1_3")
        self.verticalLayout.addWidget(self.v1_3)
        
        self.vC1_1 = QtWidgets.QLabel(self.widget)
        self.vC1_1.setText("")
        self.vC1_1.setObjectName("vC1_1")
        self.verticalLayout.addWidget(self.vC1_1)
        
        self.C1_2 = QtWidgets.QLabel(self.widget)
        self.C1_2.setText("")
        self.C1_2.setObjectName("C1_2")
        self.verticalLayout.addWidget(self.C1_2)
        
        self.C1_3 = QtWidgets.QLabel(self.widget)
        self.C1_3.setText("")
        self.C1_3.setObjectName("C1_3")
        self.verticalLayout.addWidget(self.C1_3)
        
        self.A1_1 = QtWidgets.QLabel(self.widget)
        self.A1_1.setText("")
        self.A1_1.setObjectName("A1_1")
        self.verticalLayout.addWidget(self.A1_1)
        
        self.A1_2 = QtWidgets.QLabel(self.widget)
        self.A1_2.setText("")
        self.A1_2.setObjectName("A1_2")
        self.verticalLayout.addWidget(self.A1_2)
        
        self.A1_3 = QtWidgets.QLabel(self.widget)
        self.A1_3.setText("")
        self.A1_3.setObjectName("A1_3")
        self.verticalLayout.addWidget(self.A1_3)
        
        self.PA1_1 = QtWidgets.QLabel(self.widget)
        self.PA1_1.setText("")
        self.PA1_1.setObjectName("PA1_1")
        self.verticalLayout.addWidget(self.PA1_1)
        
        self.PA1_2 = QtWidgets.QLabel(self.widget)
        self.PA1_2.setText("")
        self.PA1_2.setObjectName("PA1_2")
        self.verticalLayout.addWidget(self.PA1_2)
        
        self.PA1_3 = QtWidgets.QLabel(self.widget)
        self.PA1_3.setText("")
        self.PA1_3.setObjectName("PA1_3")
        self.verticalLayout.addWidget(self.PA1_3)
        
        self.background.raise_()
        self.motor3text.raise_()
        self.motor4text.raise_()
        self.MOTOR1action.raise_()
        self.MOTOR2action.raise_()
        self.MOTOR3action.raise_()
        self.MOTOR4action.raise_()
        self.dateTimeEdit.raise_()
        self.motor2text.raise_()
        self.motor1text.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.MOTOR1action.setText(_translate("Dialog", "R1"))
        self.MOTOR2action.setText(_translate("Dialog", "R2"))
        self.MOTOR3action.setText(_translate("Dialog", "R3"))
        self.MOTOR4action.setText(_translate("Dialog", "R4"))