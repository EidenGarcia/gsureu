import cv2
import time
from jetbot.jetbot import Robot

robot = Robot()
#speed percentage 
spd_1 = 0.3
spd_2 = 0.4
#actual speed of the jetbot at 100%
rspd = 1.405 
#
dspd_1 = (spd_1*rspd)/100
dspd_2 = (spd_2*rspd)/100

#---------------------
disW=640
dispH=480
flip=0
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , cv2.CAP_GSTREAMER)
while True:
    ret, frame=cam.read()
    if robot.forward(spd_1):
        cv2.putText(frame,"Speed m/s:"+str(dspd_1),(600,420),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        
    elif robot.backward(spd_2):
        cv2.putText(frame,"Speed m/s:"+str(dspd_2),(600,420),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2) 
    
    elif robot.left(spd_1):
        cv2.putText(frame,"Speed m/s:"+str(dspd_1),(600,420),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2) 
    
    elif robot.right(spd_1):
        cv2.putText(frame,"Speed m/s:"+str(dspd_1),(600,420),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    
    cv2.imshow('piCam',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

#---------------------
robot.forward(spd_1)
time.sleep(5)
robot.stop

robot.backward(spd_2)
time.sleep(5)
robot.stop

robot.left(spd_1) 
time.sleep(0.5)
robot.stop()

robot.right(spd_1) 
time.sleep(0.5)
robot.stop()
