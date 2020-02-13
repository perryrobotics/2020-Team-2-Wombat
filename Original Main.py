#!/usr/bin/python
import os, sys
import ctypes
from motion import *
from sensors import *
from effectors import *
from constants import *

KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

def Original_Main():
 	print "Hello World"
	KIPR.enable_servos() 
	#POSITION IN START BOX
	tail_up()
	arm_start(50)
	claw_open(50)
	while KIPR.a_button() == 0:
		pass
        
	print("HERE WE GO!!:")
	KIPR.msleep(2000)
#================================================================   
    
 	#GO GET YELLOW CUBE
	#forward(1000, 1600)
	drive_to_black(1000)
	backward(500, 50)
	arm_yellow(50)
	claw_yellow(50)
	arm_up(50)
    #WE GRABBED YELLOW CUBE
	#NOW MOVE TO DROP IT
	backward(500,3000)
	arm_yellow(50)
	claw_open(50)
	arm_up(50)
	back_to_black(1000)
	#WE SCORED YELLOW CUBE!!!!

	backward(600, 175)
	tail_down()
#We hooked the container!!            

	forward(1500, 2300)
	left(1000,1250)
	forward(1300, 2000) #HIT PIPE IN FRONT
	back_to_black(800)
	right(1000, 1050)
	forward(1000, 3400) #HIT PIPE IN FRONT OF SWINGS!!
	backward(1000, 450)
	left(1000, 1000)
	backward(1000, 1100)
	tail_up()
#Container Placed
	right(1000, 1700)
	arm_half(50)
	right(1000, 800)
	arm_up(50)
            
#knocked over conmtainers, get to ramp
	forward(1000,550) #get away from swings
	right(750,650)#turn to face black tape
	drive_to_black(750)
	right(750,850) #turn to face back pipe
	forward(1000, 6500) #hit back pipe
	backward(1000,700)  #get off back pipe a buit
	left(750,1150)  #turn towards ramp
	forward(1000,5000) #hit pipe by ramp
	backward(1000, 800)
	left(1000,1100)
            

	forward(1500, 3000)

	linefollowing_bump(1500)
	
	#Bump
	backward(1000, 700)
	left(1500,700)
	forward(1500, 700)
	left(1500,450)
	forward (1500, 700)
	arm_half(30)
	linefollow_cliff(1000)
	backward(1000, 1500)
	#ready to go down
	arm_yellow(10)
	forward(1000,750)
	arm_deep(50)
	claw_close(50)
	#We got em, get em out now!!
	arm_yellow(10)
	backward(1000, 700)
	arm_half(10)
	backward(1000, 1000)
	#OK, got em out!  Now lets try and dump #1
	left(500, 500)
	forward(500, 800)
	left(500,150) #final left to cup
	arm_yellow(10)
	claw_open(10)
#SCORED!!  NOW MAKE SECOND GRAB!!!
	arm_half(20)
	backward(500,1000)
	right_to_line(200)
	right(500,350)
	#LINED UP!!!
	linefollow_cliff(1000)
	backward(1000, 1500)
	#ready to go down
	arm_yellow(25)
	forward(1000,700)
	arm_deep(10)
	claw_close(10)	
	#We got em, get em out now!!
	arm_yellow(25)
	backward(1000, 800)
	arm_half(25)
	backward(1000, 1000)
	#OK, got em out!  Now lets try and dump #1
	backward(500, 1500)

	claw_open(50)
		

	
	#backward(1000,1000)
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
