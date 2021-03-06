# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Forms/mrrobot.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_statusView(object):
    def setupUi(self, statusView):
        statusView.setObjectName(_fromUtf8("statusView"))
        statusView.resize(600, 628)
        statusView.setMinimumSize(QtCore.QSize(600, 0))
        statusView.setMaximumSize(QtCore.QSize(600, 16777215))
        statusView.setStyleSheet(_fromUtf8("border:2px solid green;"))
        self.centralwidget = QtGui.QWidget(statusView)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(60, 0))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.cameraLivefeed = QtGui.QLabel(self.page)
        self.cameraLivefeed.setText(_fromUtf8(""))
        self.cameraLivefeed.setScaledContents(True)
        self.cameraLivefeed.setObjectName(_fromUtf8("cameraLivefeed"))
        self.verticalLayout_5.addWidget(self.cameraLivefeed)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.registerBtn = QtGui.QPushButton(self.page)
        self.registerBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.registerBtn.setObjectName(_fromUtf8("registerBtn"))
        self.horizontalLayout_7.addWidget(self.registerBtn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.setStretch(0, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(20, 243, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.groupBox = QtGui.QGroupBox(self.page_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.idLable = QtGui.QLabel(self.groupBox)
        self.idLable.setMinimumSize(QtCore.QSize(70, 30))
        self.idLable.setObjectName(_fromUtf8("idLable"))
        self.horizontalLayout_2.addWidget(self.idLable)
        self.idLine = QtGui.QLineEdit(self.groupBox)
        self.idLine.setMinimumSize(QtCore.QSize(200, 30))
        self.idLine.setObjectName(_fromUtf8("idLine"))
        self.horizontalLayout_2.addWidget(self.idLine)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.nameLable = QtGui.QLabel(self.groupBox)
        self.nameLable.setMinimumSize(QtCore.QSize(70, 0))
        self.nameLable.setObjectName(_fromUtf8("nameLable"))
        self.horizontalLayout_3.addWidget(self.nameLable)
        self.nameLine = QtGui.QLineEdit(self.groupBox)
        self.nameLine.setMinimumSize(QtCore.QSize(200, 30))
        self.nameLine.setObjectName(_fromUtf8("nameLine"))
        self.horizontalLayout_3.addWidget(self.nameLine)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.saveBtn = QtGui.QPushButton(self.groupBox)
        self.saveBtn.setMinimumSize(QtCore.QSize(90, 30))
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.horizontalLayout_5.addWidget(self.saveBtn)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addWidget(self.groupBox)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtGui.QSpacerItem(20, 79, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.cameraCapturefeed = QtGui.QLabel(self.page_3)
        self.cameraCapturefeed.setText(_fromUtf8(""))
        self.cameraCapturefeed.setObjectName(_fromUtf8("cameraCapturefeed"))
        self.verticalLayout_4.addWidget(self.cameraCapturefeed)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.captureBtn = QtGui.QPushButton(self.page_3)
        self.captureBtn.setMinimumSize(QtCore.QSize(80, 0))
        self.captureBtn.setObjectName(_fromUtf8("captureBtn"))
        self.horizontalLayout_4.addWidget(self.captureBtn)
        self.okBtn = QtGui.QPushButton(self.page_3)
        self.okBtn.setMinimumSize(QtCore.QSize(80, 0))
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.horizontalLayout_4.addWidget(self.okBtn)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.setStretch(0, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backBtn = QtGui.QPushButton(self.centralwidget)
        self.backBtn.setMinimumSize(QtCore.QSize(70, 0))
        self.backBtn.setObjectName(_fromUtf8("backBtn"))
        self.horizontalLayout.addWidget(self.backBtn)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        statusView.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(statusView)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        statusView.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(statusView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        statusView.setMenuBar(self.menubar)
        self.actionTxt = QtGui.QAction(statusView)
        self.actionTxt.setObjectName(_fromUtf8("actionTxt"))
        self.actionCsv = QtGui.QAction(statusView)
        self.actionCsv.setObjectName(_fromUtf8("actionCsv"))
        self.actionClose = QtGui.QAction(statusView)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))

        self.retranslateUi(statusView)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(statusView)

    def retranslateUi(self, statusView):
        statusView.setWindowTitle(_translate("statusView", "MainWindow", None))
        self.registerBtn.setText(_translate("statusView", "Register", None))
        self.groupBox.setTitle(_translate("statusView", "User Information", None))
        self.idLable.setText(_translate("statusView", "ID", None))
        self.nameLable.setText(_translate("statusView", "NAME", None))
        self.saveBtn.setText(_translate("statusView", "SAVE", None))
        self.captureBtn.setText(_translate("statusView", "CAPTURE", None))
        self.okBtn.setText(_translate("statusView", "OK", None))
        self.backBtn.setText(_translate("statusView", "Back", None))
        self.actionTxt.setText(_translate("statusView", "txt", None))
        self.actionCsv.setText(_translate("statusView", "csv", None))
        self.actionClose.setText(_translate("statusView", "close", None))

