import cv2
import numpy as np

class ObjectDetector:

    def __init__(self, weights_path, config_path, names_path):

        self.net = cv2.dnn.readNet(weights_path, config_path)

        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        layer_names = self.net.getLayerNames()
        self.output_layers = [layer_names[i - 1] for i in self.net.getUnconnectedOutLayers().flatten()]

        with open(names_path, "r") as f:
            self.classes = [line.strip() for line in f.readlines()]


    def detect_objects(self, frame):

        height, width, _ = frame.shape

        # smaller frame = faster
        frame = cv2.resize(frame, (480, 360))

        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (320,320), swapRB=True, crop=False)

        self.net.setInput(blob)

        outputs = self.net.forward(self.output_layers)

        boxes = []
        confidences = []
        class_ids = []

        for output in outputs:
            for detection in output:

                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.35:

                    center_x = int(detection[0] * 480)
                    center_y = int(detection[1] * 360)
                    w = int(detection[2] * 480)
                    h = int(detection[3] * 360)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x,y,w,h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.35, 0.3)

        detected_labels = {}

        if len(indexes) > 0:
            for i in indexes.flatten():

                x,y,w,h = boxes[i]

                label = self.classes[class_ids[i]]

                confidence = confidences[i]

                color = (0,255,0)

                # rectangles
                cv2.rectangle(frame,(x,y),(x+w,y+h),color,1)

                # label
                cv2.putText(frame,
                            f"{label}",
                            (x,y-5),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            color,
                            1)

                if label in detected_labels:
                    detected_labels[label] += 1
                else:
                    detected_labels[label] = 1

        return frame, detected_labels