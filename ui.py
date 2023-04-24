# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 353)
        MainWindow.setStyleSheet("font: 11pt \"Microsoft YaHei UI\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.restTab = QtWidgets.QWidget()
        self.restTab.setObjectName("restTab")
        self.gridLayout = QtWidgets.QGridLayout(self.restTab)
        self.gridLayout.setObjectName("gridLayout")
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
        self.label_2 = QtWidgets.QLabel(self.restTab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.restSpinBox = QtWidgets.QSpinBox(self.restTab)
        self.restSpinBox.setMinimum(1)
        self.restSpinBox.setMaximum(9999)
        self.restSpinBox.setProperty("value", 60)
        self.restSpinBox.setObjectName("restSpinBox")
        self.horizontalLayout.addWidget(self.restSpinBox)
        spacerItem = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.restTab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.methodComboBox = QtWidgets.QComboBox(self.restTab)
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.methodComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.restTab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.restTab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.workProgressBar = QtWidgets.QProgressBar(self.restTab)
        self.workProgressBar.setProperty("value", 0)
        self.workProgressBar.setObjectName("workProgressBar")
        self.gridLayout.addWidget(self.workProgressBar, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.restTab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.restProgressBar = QtWidgets.QProgressBar(self.restTab)
        self.restProgressBar.setProperty("value", 0)
        self.restProgressBar.setObjectName("restProgressBar")
        self.gridLayout.addWidget(self.restProgressBar, 6, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.restStopBtn = QtWidgets.QPushButton(self.restTab)
        self.restStopBtn.setObjectName("restStopBtn")
        self.horizontalLayout_6.addWidget(self.restStopBtn)
        self.restStartBtn = QtWidgets.QPushButton(self.restTab)
        self.restStartBtn.setObjectName("restStartBtn")
        self.horizontalLayout_6.addWidget(self.restStartBtn)
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)
        self.tabWidget.addTab(self.restTab, "")
        self.scheduleTab = QtWidgets.QWidget()
        self.scheduleTab.setObjectName("scheduleTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scheduleTab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scheduleTextEdit = QtWidgets.QPlainTextEdit(self.scheduleTab)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.scheduleTextEdit.setFont(font)
        self.scheduleTextEdit.setStyleSheet("font-size: 11pt;\n"
"font-family: \"Consolas\", \"Microsoft YaHei\";")
        self.scheduleTextEdit.setObjectName("scheduleTextEdit")
        self.gridLayout_3.addWidget(self.scheduleTextEdit, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(498, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.scheduleSaveBtn = QtWidgets.QPushButton(self.scheduleTab)
        self.scheduleSaveBtn.setObjectName("scheduleSaveBtn")
        self.horizontalLayout_4.addWidget(self.scheduleSaveBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.scheduleTab, "")
        self.otherTab = QtWidgets.QWidget()
        self.otherTab.setObjectName("otherTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.otherTab)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.otherTab)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bootStartCheckBox = QtWidgets.QCheckBox(self.tab)
        self.bootStartCheckBox.setObjectName("bootStartCheckBox")
        self.horizontalLayout_5.addWidget(self.bootStartCheckBox)
        self.hideStartCheckBox = QtWidgets.QCheckBox(self.tab)
        self.hideStartCheckBox.setObjectName("hideStartCheckBox")
        self.horizontalLayout_5.addWidget(self.hideStartCheckBox)
        self.beginStartCheckBox = QtWidgets.QCheckBox(self.tab)
        self.beginStartCheckBox.setObjectName("beginStartCheckBox")
        self.horizontalLayout_5.addWidget(self.beginStartCheckBox)
        spacerItem4 = QtWidgets.QSpacerItem(118, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.updateBtn = QtWidgets.QPushButton(self.tab)
        self.updateBtn.setObjectName("updateBtn")
        self.horizontalLayout_7.addWidget(self.updateBtn)
        spacerItem5 = QtWidgets.QSpacerItem(348, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.gridLayout_8.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 183, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem6, 2, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout.setObjectName("formLayout")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setMinimumSize(QtCore.QSize(45, 0))
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.titleTextLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.titleTextLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.titleTextLineEdit.setObjectName("titleTextLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleTextLineEdit)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.workTextLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.workTextLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.workTextLineEdit.setObjectName("workTextLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.workTextLineEdit)
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.restTextLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.restTextLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.restTextLineEdit.setObjectName("restTextLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.restTextLineEdit)
        spacerItem7 = QtWidgets.QSpacerItem(20, 147, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem7)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayout_3 = QtWidgets.QFormLayout(self.tab_4)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.messagePusherServerAddressLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.messagePusherServerAddressLineEdit.setText("")
        self.messagePusherServerAddressLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.messagePusherServerAddressLineEdit.setObjectName("messagePusherServerAddressLineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.messagePusherServerAddressLineEdit)
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.messagePusherUsernameLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.messagePusherUsernameLineEdit.setText("")
        self.messagePusherUsernameLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.messagePusherUsernameLineEdit.setObjectName("messagePusherUsernameLineEdit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.messagePusherUsernameLineEdit)
        self.messagePusherCheckBox = QtWidgets.QCheckBox(self.tab_4)
        self.messagePusherCheckBox.setObjectName("messagePusherCheckBox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.messagePusherCheckBox)
        self.messagePusherClientTokenLineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.messagePusherClientTokenLineEdit.setText("")
        self.messagePusherClientTokenLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.messagePusherClientTokenLineEdit.setObjectName("messagePusherClientTokenLineEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.messagePusherClientTokenLineEdit)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.microblogServerLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.microblogServerLineEdit.setText("")
        self.microblogServerLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.microblogServerLineEdit.setObjectName("microblogServerLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.microblogServerLineEdit)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.microblogTokenLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.microblogTokenLineEdit.setText("")
        self.microblogTokenLineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.microblogTokenLineEdit.setObjectName("microblogTokenLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.microblogTokenLineEdit)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.messagePusherURLLineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.messagePusherURLLineEdit.setText("")
        self.messagePusherURLLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.messagePusherURLLineEdit.setObjectName("messagePusherURLLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.messagePusherURLLineEdit)
        spacerItem8 = QtWidgets.QSpacerItem(20, 69, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem8)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.gridLayout_5.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.otherTab, "")
        self.msgHistoryTab = QtWidgets.QWidget()
        self.msgHistoryTab.setObjectName("msgHistoryTab")
        self.gridLayout_history = QtWidgets.QGridLayout(self.msgHistoryTab)
        self.gridLayout_history.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_history.setSpacing(0)
        self.gridLayout_history.setObjectName("gridLayout_history")
        self.messageHistoryEdit = QtWidgets.QTextEdit(self.msgHistoryTab)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.messageHistoryEdit.setFont(font)
        self.messageHistoryEdit.setReadOnly(True)
        self.messageHistoryEdit.setObjectName("messageHistoryEdit")
        self.gridLayout_history.addWidget(self.messageHistoryEdit, 0, 0, 1, 1)
        self.horizontalLayout_history = QtWidgets.QHBoxLayout()
        self.horizontalLayout_history.setObjectName("horizontalLayout_history")
        spacerItem9 = QtWidgets.QSpacerItem(498, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_history.addItem(spacerItem9)
        self.msgClearBtn = QtWidgets.QPushButton(self.msgHistoryTab)
        self.msgClearBtn.setObjectName("msgClearBtn")
        self.horizontalLayout_history.addWidget(self.msgClearBtn)
        self.gridLayout_history.addLayout(self.horizontalLayout_history, 1, 0, 1, 1)
        self.tabWidget.addTab(self.msgHistoryTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "个人助理"))
        self.label.setText(_translate("MainWindow", "休息间隔："))
        self.workSpinBox.setSuffix(_translate("MainWindow", " 分钟"))
        self.label_2.setText(_translate("MainWindow", "休息时长："))
        self.restSpinBox.setSuffix(_translate("MainWindow", " 秒"))
        self.label_3.setText(_translate("MainWindow", "提醒方式："))
        self.methodComboBox.setItemText(0, _translate("MainWindow", "消息提醒"))
        self.methodComboBox.setItemText(1, _translate("MainWindow", "弹窗提醒"))
        self.methodComboBox.setItemText(2, _translate("MainWindow", "显示桌面"))
        self.methodComboBox.setItemText(3, _translate("MainWindow", "强制锁屏"))
        self.label_4.setText(_translate("MainWindow", "工作进度条："))
        self.label_5.setText(_translate("MainWindow", "休息进度条："))
        self.restStopBtn.setText(_translate("MainWindow", "终止"))
        self.restStartBtn.setText(_translate("MainWindow", "开始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.restTab), _translate("MainWindow", "休息提醒"))
        self.scheduleTextEdit.setPlainText(_translate("MainWindow", "# 语法：weekday hour minute command\n"
""))
        self.scheduleSaveBtn.setText(_translate("MainWindow", "保存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scheduleTab), _translate("MainWindow", "定时任务"))
        self.bootStartCheckBox.setText(_translate("MainWindow", "开机启动"))
        self.hideStartCheckBox.setText(_translate("MainWindow", "启动时最小化到托盘"))
        self.beginStartCheckBox.setText(_translate("MainWindow", "启动时自动开始休息提醒"))
        self.updateBtn.setText(_translate("MainWindow", "检查更新"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "通用"))
        self.label_16.setText(_translate("MainWindow", "标题文案："))
        self.titleTextLineEdit.setText(_translate("MainWindow", "个人助理"))
        self.label_14.setText(_translate("MainWindow", "提醒开始工作文案："))
        self.workTextLineEdit.setText(_translate("MainWindow", "开始工作！"))
        self.label_15.setText(_translate("MainWindow", "提醒开始休息文案："))
        self.restTextLineEdit.setText(_translate("MainWindow", "开始休息！"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "个性化"))
        self.label_13.setText(_translate("MainWindow", "服务端部署地址："))
        self.messagePusherServerAddressLineEdit.setPlaceholderText(_translate("MainWindow", "例如：https://msgpusher.com"))
        self.label_17.setText(_translate("MainWindow", "客户端连接密钥："))
        self.label_18.setText(_translate("MainWindow", "用户名："))
        self.messagePusherUsernameLineEdit.setPlaceholderText(_translate("MainWindow", "用户名"))
        self.messagePusherCheckBox.setText(_translate("MainWindow", "本客户端作为消息推送服务客户端使用"))
        self.messagePusherClientTokenLineEdit.setPlaceholderText(_translate("MainWindow", "在后台设置的客户端连接密钥"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "消息推送服务"))
        self.label_10.setText(_translate("MainWindow", "microblog 服务地址："))
        self.label_11.setText(_translate("MainWindow", "microblog 访问凭证："))
        self.label_12.setText(_translate("MainWindow", "消息推送 API 端口："))
        self.messagePusherURLLineEdit.setPlaceholderText(_translate("MainWindow", "$title 和 $description 将会被替换为实际值"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "外部服务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.otherTab), _translate("MainWindow", "其他设置"))
        self.msgClearBtn.setText(_translate("MainWindow", "清空显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.msgHistoryTab), _translate("MainWindow", "消息历史"))
import resource_rc
