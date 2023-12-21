# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1117, 824)
        Dialog.setStyleSheet("background-color: #cccccc;\n"
"")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1121, 131))
        self.frame.setStyleSheet("background-color: #0A1172;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 40, 841, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.Reload = QtWidgets.QPushButton(self.frame)
        self.Reload.setGeometry(QtCore.QRect(1000, 90, 111, 31))
        self.Reload.setStyleSheet("padding: 5px;\n"
"background-color: #0A1172;\n"
"color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reloadIcon-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Reload.setIcon(icon)
        self.Reload.setObjectName("Reload")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 130, 271, 691))
        self.frame_2.setStyleSheet("background-color: #0A1172;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.addcitybtn = QtWidgets.QPushButton(self.frame_2)
        self.addcitybtn.setGeometry(QtCore.QRect(40, 260, 201, 51))
        self.addcitybtn.setStyleSheet("padding: 5px;\n"
"background-color: #0A1172;\n"
"color: white;")
        self.addcitybtn.setObjectName("addcitybtn")
        self.removecitybtn = QtWidgets.QPushButton(self.frame_2)
        self.removecitybtn.setGeometry(QtCore.QRect(40, 360, 201, 51))
        self.removecitybtn.setStyleSheet("padding: 5px;\n"
"background-color: #0A1172;\n"
"color: white;")
        self.removecitybtn.setObjectName("removecitybtn")
        self.add_userbtn = QtWidgets.QPushButton(self.frame_2)
        self.add_userbtn.setGeometry(QtCore.QRect(40, 160, 201, 51))
        self.add_userbtn.setStyleSheet("padding: 5px;\n"
"background-color: #0A1172;\n"
"color: white;")
        self.add_userbtn.setObjectName("add_userbtn")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(275, 131, 841, 691))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Route Optimization and Management System"))
        self.Reload.setText(_translate("Dialog", "Reload"))
        self.addcitybtn.setText(_translate("Dialog", "Add City"))
        self.removecitybtn.setText(_translate("Dialog", "Remove City"))
        self.add_userbtn.setText(_translate("Dialog", "Add User"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "City Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Latitude"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Adjacent Cities"))