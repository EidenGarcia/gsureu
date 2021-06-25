#***This is been implemented in jupiter on a notebook file***


#To get started programming JetBot, well need to import the Robot class. 
#This class allows us to easily control the robots motors! This is contained in the jetbot package.

from jetbot import Robot

#If we want to run the robot for a set period of time. 
#We can use the Python time package.

import time

#We can initialize the class instance as follows.

robot = Robot()

#We can control the velocity of the motor individuali by inputing the (.left) or (.right). And control the speed of the motors.
#In the example the motor are at 40% of the max speed.

robot.left(speed=0.4)
robot.right(speed=0.4)

#We can control the velocity of the two motors by inputing the (.set_motors). And control the speed of the individuali motors.
#In the example the motor rigth is at 40% and the left motor is  at 30% of the max speed.

robot.set_motors(0.4,0.3)

#This package defines the sleep function, which causes the code execution to block 
#for the specified number of seconds before running the next command.

time.sleep(10.0)

#We can mak the robot move forward and backward wiht the next command example.

robot.forward(0.3)
robot.backward(0.3)

#To stop the robot we can use the stop method.
robot.stop()



