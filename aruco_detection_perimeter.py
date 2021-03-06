from jetbot import Robot
import time
import numpy as np
import cv2
import cv2.aruco as aruco
robot = Robot()
cap = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=720, format=(string)NV12, framerate=(fraction)20/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , cv2.CAP_GSTREAMER)  # Get the camera source

while True:
    ret, frame = cap.read()
    # operations on the frame come here
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_100)  # Use 5x5 dictionary to find markers
    parameters = aruco.DetectorParameters_create()  # Marker detection parameters
    # lists of ids and the corners beloning to each id
	#ids = np.array([1])
    corners, ids, rejected_img_points = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
	#print(ids)
    

    if corners:
        for id in ids:
            if id == 2:
                print("North: 2")
                robot.left(0.3)
                time.sleep(0.325)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 3:
                print("South: 3")
                robot.left(0.3)
                time.sleep(0.5)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 4:
                print("East: 4")
                robot.left(0.3)
                time.sleep(0.325)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 5:
                print("West: 5")
                robot.left(0.3)
                time.sleep(0.325)
                robot.stop()
                break
		
    else:
        robot.forward(0.2)
        time.sleep(0.001)
        
            
                
				
    frame = aruco.drawDetectedMarkers(frame, corners, ids)

	# Display the resulting frame
    cv2.imshow('frame', frame)
    # Wait 3 milisecoonds for an interaction. Check the key and do the corresponding job.
    key = cv2.waitKey(3) & 0xFF
    if key == ord('q'):  # Quit
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
