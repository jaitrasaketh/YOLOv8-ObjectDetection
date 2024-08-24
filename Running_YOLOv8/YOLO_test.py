from ultralytics import YOLO
import cv2

#model=YOLO('yolov8n.pt') ##pretrained yolov8 nano.. more fast but less accurate
model=YOLO('yolov8x.pt')   ## most accurate pretrained model of yolov8

results=model('../assets/severalobjs.jpg', show=True)
cv2.waitKey(0)
