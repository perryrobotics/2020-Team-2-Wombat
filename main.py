#!/usr/bin/python
import os, sys
import ctypes
from motion import *
from sensors import *
from effectors import *
from constants import *
from start import *


KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

def main():
 	print "Hello World"
	KIPR.enable_servos() 
	#POSITION IN START BOX
	tail_up()
	arm_start(50)
	claw_open(50)
	start(2)
	KIPR.shut_down_in(120)
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
	claw_close(50)
            
#knocked over conmtainers, get to ramp
	forward(1000,550) #get away from swings
	right(750,650)#turn to face black tape
	drive_to_black(750)
	right(750,850) #turn to face back pipe
	forward(1000, 6500) #hit back pipe
	backward(1000,700)  #get off back pipe a buit
	left(750,1150)  #turn towards ramp
	forward(1000,5500) #hit pipe by ramp
	backward(1000, 500)
	left(1000,1100)
	backward(1000,1000)


	#GO UP THE RAMP
	#forward(1500, 3000)

	linefollowing_bump(1500)
	
	#Bump
	backward(1000, 700)# get off the pipe
	left(1500,600) #turn to the mine
	forward(1500, 700)
	left(1500,500)
	forward (1500, 700)
	arm_half(30)
	linefollow_cliff(1000)
	backward(1000, 1500)
	#ready to go down
	arm_yellow(10)
	claw_open(50)
	forward(900,750)
	arm_deep(50)
	claw_close(70)
	claw_open(70)
	claw_close(70)
	#We got em, get em out now!!
	arm_yellow(10)
	backward(1000, 700)
	arm_half(10)
	backward(1000, 1000)
	#OK, got em out! Now lets dump it on the ramp!
	claw_open(10)
#SCORED!!  NOW MAKE SECOND GRAB!
	claw_close(50)
	left(1000, 50)
	linefollow_grab(1000)
	backward(1000, 1500)
	#ready to go down
	arm_yellow(25)
	forward(900,610)
	claw_open(50)
	arm_deep(10)
	claw_close(70)
	claw_open(70)
	claw_close(70)
	#We got em, get em out now!!
	arm_yellow(25)
	backward(1000, 800)
	arm_half(25)
	backward(1000, 1000)
	#OK, got em out!  Now lets try and dump #1
	backward(500, 1500)

	claw_open(50)
#SCORED!!  NOW MAKE Third GRAB!
	claw_close(50)
	left(600, 50)
	linefollow_grab(1000)
	backward(1000, 1500)
	#ready to go down
	arm_yellow(25)
	forward(1000,620)
	claw_open(50)
	arm_deep(10)
	claw_close(70)
	claw_open(70)
	claw_close(70)
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
