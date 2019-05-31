import cv2
import numpy
import os
import pickle
from PyQt4 import  QtCore
class Trainer(QtCore.QThread):
    def __init__(self , BASE_DIR):
        QtCore.QThread.__init__(self)
        self.BASE_DIR = BASE_DIR
    def run(self):
        face_recognizer = cv2.face.createLBPHFaceRecognizer()
        images = []
        templables = []
        templablesNames = []
        org_path = self.BASE_DIR
        for folder in os.listdir(org_path):
            templablesNames.append(folder)
            branch_dir = os.path.join(org_path, folder)
            count = 0
            for imgFile in os.listdir(branch_dir):
                try:
                    imname = os.path.join(branch_dir, imgFile)
                    temp = cv2.imread(imname)
                    temp = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
                    images.append(temp)
                    templables.append(len(templablesNames) - 1)
                    count += 1
                except:
                    pass
        labels = numpy.asarray(templables, dtype=numpy.int32)

        print "train started"
        face_recognizer.train(images, labels)
        print "train ended"
        face_recognizer.save('facesModel.xml')
        pickle.dump(templablesNames, open("faceLabels", "w"))

