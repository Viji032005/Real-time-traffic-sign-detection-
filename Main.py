import cv2 as cv
import numpy as np
net = cv.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
  classes = [line.strip() for line in f.readlines()]
  layer_names = net.getLayerNames()
  output_layers = [layer_names[i - 1]
       for i in net.getUnconnectedOutLayers()]
  colors = np.random.uniform(0, 255, size=(len(classes), 3))
  cap = cv.VideoCapture(0) # 0 for default webcam
while True:ret, 
  frame = cap.read()
if not ret:
  break
  height, width, channels = frame.shape
  blob = cv.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)net.setInput(blob)outs = net.forward(output_layers)class_ids = []confidences = []boxes = []for out in outs:for detection in out:scores = detection[5:]class_id = np.argmax(scores)confidence = scores[class_id]if confidence > 0.5:center_x = int(detection[0] * width)center_y = int(detection[1] * height)w = int(detection[2] * width)h = int(detection[3] * height)x = int(center_x - w / 2)y = int(center_y - h / 2)boxes.append([x, y, w, h])confidences.append(float(confidence))class_ids.append(class_id)indexes = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)if len(indexes) > 0:for i in indexes.flatten()x, y, w, h = boxes[i]label = str(classes[class_ids[i]])color = colors[i]cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)cv.putText(frame, label, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)cv.imshow("Image", frame)if cv.waitKey(1) & 0xFF == ord('q'):breakcap.release()cv.destroyAllWindows(). 
