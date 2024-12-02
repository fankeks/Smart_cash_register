from ultralytics.utils.plotting import Annotator
import cv2
import numpy as np


class MyAnnotator(Annotator):
    def box_label(self, box, label="", color=(128, 128, 128), txt_color=(255, 255, 255), rotated=False):
        if rotated:
            p1 = [int(b) for b in box[0]]
            cv2.polylines(self.im, [np.asarray(box, dtype=int)], True, color, self.lw)  # cv2 requires nparray box
        else:
            p1, p2 = (int(box[0]), int(box[1])), (int(box[2]), int(box[3]))
            cv2.rectangle(self.im, p1, p2, color, thickness=self.lw, lineType=cv2.LINE_AA)
        if label:
            w, h = cv2.getTextSize(label, cv2.FONT_HERSHEY_COMPLEX, fontScale=self.sf, thickness=self.tf)[0]  # text width, height
            h += 3  # add pixels to pad text
            outside = p1[1] >= h  # label fits outside box
            if p1[0] > self.im.shape[1] - w:  # shape is (h, w), check if label extend beyond right side of image
                p1 = self.im.shape[1] - w, p1[1]
            p2 = p1[0] + w, p1[1] - h if outside else p1[1] + h
            cv2.rectangle(self.im, p1, p2, color, -1, cv2.LINE_AA)  # filled
            cv2.putText(
                self.im,
                label,
                (p1[0], p1[1] - 2 if outside else p1[1] + h - 1),
                cv2.FONT_HERSHEY_COMPLEX,
                self.sf,
                txt_color,
                thickness=self.tf,
                lineType=cv2.LINE_AA,
            )