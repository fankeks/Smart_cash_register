from Neural_network.INeuralNetwork import INeuralNetwork
from ultralytics import YOLO
import cv2
import os
from  Neural_network.Anatator import MyAnnotator


d_translator = {'Baked chicken': "Запеченная курица",
     'Black bread': "Чёрный хлеб",
     'Cheese soup' : "Сырный суп",
     'Compote' : "Компот",
     'Fish cutlet': "Рыбные котлеты",
     'Kharcho':  "Харчо",
     'Mashed potatoes': "Картофельное пюре",
     'Meat cutlet': "Мясные котлеты",
     'Rice': "Рис",
     'White bread': "Белый хлеб",
     }


NEURAL_NETWORK_NAME = f"best_1280_1.pt"


class NeuralNetwork(INeuralNetwork):
    def __init__(self):
        self.model=YOLO(NEURAL_NETWORK_NAME)

    def get_report(self, path) -> list:

        img = cv2.imread(path)

        results = self.model.predict(img)  # results list

        annotator = MyAnnotator(img)

        boxes = results[0].boxes
        for box in boxes:
            b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
            c = box.cls
            annotator.box_label(b, label=d_translator[self.model.names[int(c)]])

        img = annotator.result()

        cv2.imwrite(path, img)

        clist= boxes.cls
        cls = {}

        for cno in clist:
            if self.model.names[int(cno)] in cls.keys():
                cls[d_translator[self.model.names[int(cno)]]] +=1
            else:
                cls[d_translator[self.model.names[int(cno)]]]=1

        return [(k,v) for k,v in cls.items()]