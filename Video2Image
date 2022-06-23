import cv2
import os

def video2image():
	cap = cv2.VideoCapture("video/test.mp4")  # 
	count = 1
	while True:
		success, frame = cap.read()
		if success == False:
			break
		cv2.imwrite("images/%d.jpg"%count, frame)
		count +=1
