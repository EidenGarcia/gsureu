#***This is been implemented in jupiter on a notebook file***
#This is a 20.7sec dance.

#To get started programming JetBot, well need to import the Robot class. 
from jetbot import Robot
#Import the time class.
import time
robot=Robot()
#The robot is goign to stand by 5sec.
time.sleep(5.0)
#The robot i going to move foward.
robot.forward(0.5)
time.sleep(0.5)
#Then is going to move backward.
robot.backward(0.5)
time.sleep(0.3)
#The robot is going to rotate in the left direction.
robot.left(speed=0.3)
time.sleep(3.0)
#The robot will move slightly to the right and forward.
robot.set_motors(0.6,0.3)
time.sleep(0.5)
#The robot will move slightly to the left and backward.
robot.set_motors(-0.6,-0.3)
time.sleep(0.5)
#The robot is going to rotate for 3sec.
robot.right(speed=0.3)
time.sleep(3.0)
#The robot will move slightly to the right and forward.
robot.set_motors(0.6,0.3)
time.sleep(0.5)
#The robot is going to rotate for 1sec.
robot.right(speed=0.3)
time.sleep(1.0)
#The robot is going to move backward.
robot.backward(0.5)
time.sleep(0.3)
#The robot is going to rotate for 1sec.
robot.left(speed=0.3)
time.sleep(1.0)
#The robot is going to move foward.
robot.forward(0.5)
time.sleep(0.3)
#The robot is going to rotate for 2sec.
robot.right(speed=0.3)
time.sleep(2.0)
#The robot is going to rotate for 2sec.
robot.left(speed=0.3)
time.sleep(2.0)
#The robot is going to mve backward.
robot.backward(0.5)
time.sleep(0.3)
#The robot is going to rotate for 0.5sec.
robot.right(speed=0.3)
time.sleep(0.5)
#The robot is going to stop.
robot.stop()