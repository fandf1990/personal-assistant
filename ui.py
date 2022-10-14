# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 280)
        MainWindow.setStyleSheet("font: 9pt \"Microsoft YaHei UI\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.restTab = QtWidgets.QWidget()
        self.restTab.setObjectName("restTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.restTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.restTab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.workSpinBox = QtWidgets.QSpinBox(self.restTab)
        self.workSpinBox.setMinimum(1)
        self.workSpinBox.setMaximum(9999)
        self.workSpinBox.setProperty("value", 20)
        self.workSpinBox.setObjectName("workSpinBox")
        self.horizontalLayout.addWidget(self.workSpinBox)
        spacerItem = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.restTab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.restSpinBox = QtWidgets.QSpinBox(self.restTab)
        self.restSpinBox.setMinimum(1)
        self.restSpinBox.setMaximum(9999)
        self.restSpinBox.setProperty("value", 1)
        self.restSpinBox.setObjectName("restSpinBox")
        self.horizontalLayout_2.addWidget(self.restSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.restTab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.methodComboBox = QtWidgets.QComboBox(self.restTab)
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.methodComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.restTab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.workProgressBar = QtWidgets.QProgressBar(self.restTab)
        self.workProgressBar.setProperty("value", 0)
        self.workProgressBar.setObjectName("workProgressBar")
        self.gridLayout_2.addWidget(self.workProgressBar, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.restTab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.restProgressBar = QtWidgets.QProgressBar(self.restTab)
        self.restProgressBar.setProperty("value", 0)
        self.restProgressBar.setObjectName("restProgressBar")
        self.gridLayout_2.addWidget(self.restProgressBar, 6, 0, 1, 1)
        self.tabWidget.addTab(self.restTab, "")
        self.scheduleTab = QtWidgets.QWidget()
        self.scheduleTab.setObjectName("scheduleTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scheduleTab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scheduleTextEdit = QtWidgets.QPlainTextEdit(self.scheduleTab)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.scheduleTextEdit.setFont(font)
        self.scheduleTextEdit.setStyleSheet("font: 9pt \"Consolas\";")
        self.scheduleTextEdit.setPlainText("")
        self.scheduleTextEdit.setObjectName("scheduleTextEdit")
        self.gridLayout_3.addWidget(self.scheduleTextEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.scheduleTab, "")
        self.todoTab = QtWidgets.QWidget()
        self.todoTab.setObjectName("todoTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.todoTab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.todoTextEdit = QtWidgets.QPlainTextEdit(self.todoTab)
        self.todoTextEdit.setStyleSheet("font: 9pt \"Consolas\";")
        self.todoTextEdit.setObjectName("todoTextEdit")
        self.gridLayout_4.addWidget(self.todoTextEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.todoTab, "")
        self.otherTab = QtWidgets.QWidget()
        self.otherTab.setObjectName("otherTab")
        self.tabWidget.addTab(self.otherTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personal Assistant"))
        self.label.setText(_translate("MainWindow", "休息间隔："))
        self.workSpinBox.setSuffix(_translate("MainWindow", " 分钟"))
        self.label_2.setText(_translate("MainWindow", "休息时长："))
        self.restSpinBox.setSuffix(_translate("MainWindow", " 分钟"))
        self.label_3.setText(_translate("MainWindow", "提醒方式："))
        self.methodComboBox.setItemText(0, _translate("MainWindow", "消息提醒"))
        self.methodComboBox.setItemText(1, _translate("MainWindow", "弹窗提醒"))
        self.methodComboBox.setItemText(2, _translate("MainWindow", "全屏覆盖"))
        self.label_4.setText(_translate("MainWindow", "工作进度条："))
        self.label_5.setText(_translate("MainWindow", "休息进度条："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.restTab), _translate("MainWindow", "休息提醒"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scheduleTab), _translate("MainWindow", "定时任务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.todoTab), _translate("MainWindow", "周期待办"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.otherTab), _translate("MainWindow", "其他设置"))
