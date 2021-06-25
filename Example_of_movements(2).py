#***This is been implemented in jupiter on a notebook file***


#To get started programming JetBot, well need to import the Robot class. 
from jetbot import Robot

import time

robot=Robot()
#The robot is goign to stand by 5sec.
time.sleep(5.0)
#The robot i going to move foward.
robot.forward(0.5)
time.sleep(0.3)
#Then is going to move backward.
robot.backward(0.5)
time.sleep(0.3)
#The robot is going to move in circles in the left direction for 1.0 sec at 30% of the MAX speed.
robot.left(speed=0.3)
time.sleep(1.0)
#The robot will move slightly to the right and forward.
robot.set_motors(0.6,0.3)
time.sleep(0.5)
#The robot will move slightly to the left backward.
robot.set_motors(-0.6,-0.3)
time.sleep(0.5)
#The robot is going to move in circles in the right direction for 1.0sec at 30% of the MAX speed.
robot.right(speed=0.3)
time.sleep(1.0)
#The robot will move slightly to the right and forward.
robot.set_motors(0.6,0.3)
time.sleep(0.5)
#The robot is going to move in circles in the right direction for 1.0sec at 30% of the MAX speed.
robot.right(speed=0.3)
time.sleep(1.0)
#Then is going to move backward.
robot.backward(0.5)
time.sleep(0.3)
#The robot is going to move in circles in the left direction for 1.0 sec at 30% of the MAX speed.
robot.left(speed=0.3)
time.sleep(1.0)
#The robot i going to move foward.
robot.forward(0.5)
time.sleep(0.3)
#The robot is going to move in circles in the right direction for 1.0sec at 30% of the MAX speed.
robot.right(speed=0.3)
time.sleep(1.0)
#The robot is going to move in circles in the left direction for 1.0 sec at 30% of the MAX speed.
robot.left(speed=0.3)
time.sleep(1.0)
#The robot will move slightly to the left backward.
robot.set_motors(-0.6,-0.3)
time.sleep(0.5)
#The robot i going to move foward.
robot.forward(0.5)
time.sleep(0.5)
#Then is going to move backward.
robot.backward(0.5)
time.sleep(0.3)
#The robot is going to move in circles in the left direction for 0.5 sec at 30% of the MAX speed.
robot.left(0.3)
time.sleep(0.5)
#The robot i going to move foward.
robot.forward(0.5)
time.sleep(0.5)
#The robot is going to move in circles in the right direction for 0.5sec at 30% of the MAX speed.
robot.right(0.3)
time.sleep(0.5)
#The robot i going to move foward.
robot.forward(0.5)
time.sleep(0.5)
#The robot is going to move in circles in the right direction for 2.0 sec at 50% of the MAX speed.
robot.right(speed=0.5)
time.sleep(2.0)
#The robot is going to stop.
robot.stop()