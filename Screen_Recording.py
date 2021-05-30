from PIL import ImageGrab
import numpy as np
import cv2


# import tkinter
# root = tkinter.Tk()
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
from win32api import GetSystemMetrics
width= GetSystemMetrics(0)
height= GetSystemMetrics(1)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))


while True:
    img=ImageGrab.grab(bbox=(0,0,width,height))
    img_np=np.array(img)
    img_final=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('Secret Capture', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(1) == ord('q'):
        break