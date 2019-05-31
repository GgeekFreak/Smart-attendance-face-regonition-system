#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  sys
import os
from PyQt4 import  QtCore , QtGui
from Views.main_ui import Ui_statusView
from aqua.qsshelper import QSSHelper
from Modules.live_feed import LiveCapturing
from Modules.Trainer import Trainer
from Modules.dataBaseManger import DbManger
import datetime

class SmartSchool(QtGui.QMainWindow , Ui_statusView):
    def __init__(self):
        super(SmartSchool , self).__init__()
        self.setupUi(self)
        #
        self.MIN_ID_DIGITS = 8
        self.MIN_Name_DIGITS = 8
        self.currentPage = 0
        self.live_capturing_handler = LiveCapturing(self.cameraLivefeed)
        self.live_capturing_handler.StartLiveFeed()
        self.live_capturing_handler.camera_ref.imageSignal.isImageAvailable.connect(self.newFace)
        self.registerBtn.clicked.connect(self.goToRegisterWindow)
        self.captureBtn.clicked.connect(self.startDataSetCapture)
        self.saveBtn.clicked.connect(self.storeStudentInfo)
        self.okBtn.clicked.connect(self.start_training)
        self.backBtn.setVisible(False)
        self.backBtn.clicked.connect(self.goToprePage)
        self.dbManger = DbManger()
        # loads and sets the Qt stylesheet
        self.currentUer = ''
        qss = QSSHelper.open_qss(os.path.join('aqua', 'aqua.qss'))
        self.setStyleSheet(qss)
        self.stackedWidget.setCurrentIndex(0)
        self.show()
    def goToprePage(self):
        if self.currentPage ==  2:
            self.currentPage == 1
            self.idLine.setText("")
            self.nameLine.setText("")
        elif self.currentPage ==  1:
            self.currentPage == 0
            self.goLiveFeedWindow()
        self.stackedWidget.setCurrentIndex(self.currentPage)

    def goToRegisterWindow(self):
        self.currentPage = 1
        self.stackedWidget.setCurrentIndex(self.currentPage)
        self.backBtn.setVisible(True)

    def storeStudentInfo(self):
        userId = str(self.idLine.text())
        userName = str(self.nameLine.text())
        if len(userId) < self.MIN_ID_DIGITS or len(userName)<self.MIN_Name_DIGITS:
            QtGui.QMessageBox.critical(self , "smart school" , "the id must be > {} and user name must be >{}.".format(self.MIN_ID_DIGITS , self.MIN_Name_DIGITS))

        elif not userId.isdigit():
            QtGui.QMessageBox.critical(self , "smart school" , "the id must contain digits only")
        elif not userName.isalpha():
            QtGui.QMessageBox.critical(self , "smart school" , "the user name must contain letters only")
        else:
            self.registerNewStudent(userId , userName)
            self.currentUer = userName , userId

    def registerNewStudent(self, id , name):
        self.currentPage = 2
        self.backBtn.setVisible(True)

        #creat folder
        dir_path = os.path.join(os.getcwd() , "data_set" , id)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        #
        self.live_capturing_handler.record(dir_path)
        self.live_capturing_handler.set_window_viewer(self.cameraCapturefeed)
        self.live_capturing_handler.camera_ref.recordingSignal.isDone.connect(self.gatheringDataFinshed)

        self.stackedWidget.setCurrentIndex(self.currentPage)
        self.okBtn.setDisabled(True)
    def startDataSetCapture(self):
        self.okBtn.setDisabled(True)
        self.captureBtn.setStyleSheet("background-color:red;")

        self.live_capturing_handler.EnableCapturing()
    def gatheringDataFinshed(self):
        self.captureBtn.setStyleSheet("background-color:rgb(80,80,80);")
        QtGui.QMessageBox.about(self, "smart school"," done ")
        self.okBtn.setEnabled(True)
    def start_training(self):
        self.live_capturing_handler.camera_ref.reloadModel()
        self.live_capturing_handler.stop_record()
        self.live_capturing_handler.set_window_viewer(self.cameraLivefeed)
        self.setDisabled(True)
        self.trainObj = Trainer(os.path.join(os.path.join(os.getcwd() , "data_set")))
        self.trainObj.finished.connect(self.trainingFinshed)
        self.trainObj.start()

    def trainingFinshed(self):
        self.add_new_record()
        self.setDisabled(False)
        self.goLiveFeedWindow()


    def add_new_record(self):
        self.dbManger.inser_new_student(self.currentUer[0] , self.currentUer[1])

    def goLiveFeedWindow(self):
        self.currentPage = 0
        self.stackedWidget.setCurrentIndex(self.currentPage)
        self.backBtn.setVisible(False)

    def newFace(self , id):
        now = datetime.datetime.now()
        cur_date = now.strftime('%Y-%m-%d')
        usrr_ids = self.dbManger.is_exist(id)
        attandance = self.dbManger.isAttended(id , cur_date)

        if len(usrr_ids) and len(attandance ) == 0 :
            self.dbManger.submit_attendance(id , cur_date)
            print "added"













if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    smart_school = SmartSchool()
    app.exec_()
