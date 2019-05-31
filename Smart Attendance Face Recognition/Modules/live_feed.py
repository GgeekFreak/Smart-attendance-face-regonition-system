from PyQt4 import QtGui
import cv2
import os
from continus_feed import  Camera
import time
class LiveCapturing:
    def __init__(self , image_viewer, destination = "" , storeImages = False,max_images=120 ):
        self.viewer_window = image_viewer
        self.camera_ref = Camera(destination, storeImages ,max_images)
        self.camera_ref.newImage.isAvailable.connect(self.updateImageWindow)

    def StartLiveFeed(self):
        self.camera_ref.Connect()
        self.camera_ref.start()
    def record(self , path):
        self.camera_ref.start_recording(path)

    def stop_record(self):
        self.camera_ref.Stop_Record()

    def set_window_viewer(self , image_viewer):
        self.viewer_window = image_viewer

    def StopLiveFeed(self):
        self.camera_ref.close()
        self.camera_ref.terminate()
        time.sleep(0.5)

    def updateImageWindow(self , image):
        self.viewer_window.setPixmap(QtGui.QPixmap(image))
    def EnableCapturing(self):
        if not self.camera_ref.enableCapturing:
            self.camera_ref.imageCounter = 0
            self.camera_ref.enableCapturing = True







