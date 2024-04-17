# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerDqPUar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in tshis file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(961, 644)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, 0, 71, 581))
        self.widget.setStyleSheet(u"background-color: rgb(191, 191, 191);")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 0, 1021, 61))
        self.widget_2.setStyleSheet(u"background-color: rgb(191, 191, 191);\n"
"")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 10, 321, 41))
        self.label_2.setStyleSheet(u"font: 18pt \"MS PGothic\";")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 70, 41, 41))
        self.pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/E:/feather/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 70, 201, 41))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(80, 70, 41, 41))
        self.pushButton_2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/E:/feather/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(80, 120, 211, 461))
        self.widget_3.setStyleSheet(u"background-color: rgb(118, 135, 139);")
        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 10, 191, 22))
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(510, 390, 312, 183))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(293, 120, 20, 461))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(130, 70, 41, 41))
        icon2 = QIcon()
        icon2.addFile(u":/icons/E:/feather/tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(180, 70, 41, 41))
        icon3 = QIcon()
        icon3.addFile(u":/icons/E:/feather/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 961, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search Bar", None))
        self.pushButton_2.setText("")
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_3.setText("")
    # retranslateUi

