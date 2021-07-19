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
                print("90-degree angle left: 2")
                robot.left(0.3)
                time.sleep(0.325)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 3:
                print("135-degree angle left: 3")
                robot.left(0.3)
                time.sleep(0.5)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 4:
                print("90-degree angle left: 4")
                robot.left(0.3)
                time.sleep(0.325)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 5:
                print("90-degree angle left: 5")
                robot.left(0.3)
                time.sleep(0.325)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 6:
                print("135-degree angle left: 6")
                robot.left(0.3)
                time.sleep(0.5)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 7:
                print("90-degree angle left: 7")
                robot.left(0.3)
                time.sleep(0.2)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 8:
                print("135-degree angle left: 8")
                robot.left(0.3)
                time.sleep(0.5)
                robot.stop()
                break

    if corners:
        for id in ids:
            if id == 9:
                print("135-degree angle left: 9")
                robot.left(0.3)
                time.sleep(0.5)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 10:
                print("180-degree angle left: 10")
                robot.left(0.3)
                time.sleep(0.625)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 11:
                print("180-degree angle left: 11")
                robot.left(0.3)
                time.sleep(0.625)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 12:
                print("180-degree angle left: 12")
                robot.left(0.3)
                time.sleep(0.625)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 13:
                print("180-degree angle left: 13")
                robot.left(0.3)
                time.sleep(0.625)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 14:
                print("180-degree angle left: 14")
                robot.right(0.3)
                time.sleep(0.625)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 15:
                print("180-degree angle left: 15")
                robot.right(0.3)
                time.sleep(0.625)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 16:
                print("180-degree angle left: 16")
                robot.right(0.3)
                time.sleep(0.625)
                robot.stop()
                break
		
    if corners:
        for id in ids:
            if id == 17:
                print("180-degree angle left: 17")
                robot.rigth(0.3)
                time.sleep(0.625)
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
