from Neural_network.INeuralNetwork import INeuralNetwork
from ultralytics import YOLO
import cv2
import os
from ultralytics.utils.plotting import Annotator


NEURAL_NETWORK_NAME = f"best_1280_1.pt"


class NeuralNetwork(INeuralNetwork):
    def __init__(self):
        self.model=YOLO(NEURAL_NETWORK_NAME)

    def get_report(self, path) -> list:

        img = cv2.imread(path)

        results = self.model.predict(img)  # results list

        annotator = Annotator(img)

        boxes = results[0].boxes
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
            c = box.cls
            annotator.box_label(b, self.model.names[int(c)])

        img = annotator.result()

        cv2.imwrite(path, img)

        clist= boxes.cls
        cls = {}

        for cno in clist:
            if self.model.names[int(cno)] in cls.keys():
                cls[self.model.names[int(cno)]] +=1
            else:
                cls[self.model.names[int(cno)]]=1

        return [(k,v) for k,v in cls.items()]