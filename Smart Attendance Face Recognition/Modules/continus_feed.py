import cv2
import time
import os
from PyQt4 import QtCore,QtGui
import pickle
class communicate(QtCore.QObject):
    isAvailable = QtCore.pyqtSignal([QtGui.QImage])
    isImageAvailable = QtCore.pyqtSignal([str])
    isDone = QtCore.pyqtSignal()
class Camera(QtCore.QThread):
    def __init__(self,destination = "" , storeImages = False,max_images=120):
        super(Camera , self).__init__()
        file_path = os.path.join(os.getcwd() , "Modules" ,'haarcascade_frontalface_alt.xml' )
        face_path = os.path.join(os.getcwd() , "facesModel.xml")
        self.faceCascade =cv2.CascadeClassifier(file_path)
        self.face_recognizer = cv2.face.createLBPHFaceRecognizer()
        self.users_id = pickle.load(open("faceLabels" , "r"))
        self.face_recognizer.load(face_path)
        self.is_store_image_active = storeImages
        self.max_images = max_images
        self.image_path = destination
        self.imageCounter = 0
        self._camera_dev = None
        self.isOpened = False
        self.enableCapturing = False
        self.newImage = communicate()
        self.recordingSignal = communicate()
        self.imageSignal = communicate()

    def reloadModel(self):
        face_path = os.path.join(os.getcwd(), "facesModel.xml")
        self.users_id = pickle.load(open("faceLabels", "r"))
        self.face_recognizer.load(face_path)


    def start_recording(self , destination = ""):
        self.image_path = destination
        self.imageCounter = 0
        self.enableCapturing = False
        self.is_store_image_active = True
    def Stop_Record(self):
        self.imageCounter = 0
        self.enableCapturing = False
        self.is_store_image_active = False

    def Connect(self , camera_id = 0):
        self._camera_dev = cv2.VideoCapture(camera_id)
        if self._camera_dev.isOpened():
            self.isOpened = True
        else:
            self.isOpened = False
        return self

    def run(self):
        while self.isOpened :
            ret , frame = self._camera_dev.read()
            if ret:
                frame = cv2.flip(frame , 1)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.faceCascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=5, minSize=(100, 100))
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x , y ), (x +w , y + h), (255, 0, 0), 2)
                    f = gray[y:y+h, x:x+w]
                    if self.is_store_image_active :
                        if self.imageCounter < self.max_images and self.enableCapturing:
                            image_name = os.path.join(self.image_path, "image_{}.png".format(self.imageCounter))
                            cv2.imwrite( image_name , f)
                            self.imageCounter += 1
                            if self.imageCounter == self.max_images:
                                self.recordingSignal.isDone.emit()
                                self.enableCapturing = False
                    else:
                        label = self.face_recognizer.predict(f)
                        cv2.putText(frame, self.users_id[label], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 255, 155), 2,cv2.LINE_AA)
                        self.imageSignal.isImageAvailable.emit(self.users_id[label])
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                colored = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                qImg = QtGui.QImage(colored.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                self.newImage.isAvailable.emit(qImg)

        self._camera_dev.release()

    def close(self):
        self.isOpened = False
        time.sleep(0.1)

