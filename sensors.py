#!/usr/bin/python
import os, sys
import ctypes
from constants import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

#Drive to black function
    
def analog_median(port, num):
	values=[]	
	for value in range(num):
		values.append( KIPR.analog(port) )
	values.sort()
	return values[num/2]
    
def drive_to_black(speed):
	KIPR.cmpc(Lmotor)
	KIPR.mav(Rmotor, speed);
	KIPR.mav(Lmotor, speed);
	while KIPR.analog(Top_Hat_left_port) < Thresh:
		pass
	KIPR.ao()

def back_to_black(speed):
	KIPR.cmpc(Lmotor)
	KIPR.mav(Rmotor, -speed);
	KIPR.mav(Lmotor, -speed);
	while KIPR.analog(Top_Hat_left_port) < Thresh:
		pass
	KIPR.ao()
#Drive to white function
def drive_to_white(speed):
	KIPR.mav(Rmotor, speed);
	KIPR.mav(Lmotor, speed);
	while KIPR.analog(Top_Hat_left_port) > Thresh:
		pass
	KIPR.ao()
#Drive until bump function
def drive_until_bump(speed):
	KIPR.cmpc(Lmotor)
	KIPR.mav(Rmotor,speed);
	KIPR.mav(Lmotor,speed);
	while KIPR.digital(Touch_port) < 1:
		pass
        
def right_to_line(speed):
	KIPR.mav(Rmotor, -speed)
	KIPR.mav(Lmotor, speed)
	while KIPR.analog(Top_Hat_right_port) < Thresh:
		pass
	KIPR.ao()
#Linefollowing man
def linefollowing(speed,ticks):
	KIPR.cmpc(Lmotor)
	KIPR.cmpc(Rmotor)
	while KIPR.gmpc(Lmotor) < ticks:
		if KIPR.analog(Top_Hat_left_port) > Thresh:
			KIPR.cmpc(Lmotor)
			KIPR.mav(Lmotor,-speed/4)
			KIPR.mav(Rmotor, speed/4)
		elif KIPR.analog(Top_Hat_right_port) > Thresh:
			KIPR.cmpc(Lmotor)
			KIPR.mav(Lmotor, speed/4)
			KIPR.mav(Rmotor, -speed/4)
		else:
			KIPR.mav(Lmotor, speed)
			KIPR.mav(Rmotor, speed)		
	KIPR.ao()
#Linefollowing to bump
def linefollowing_bump(speed):
	KIPR.cmpc(Lmotor)
	KIPR.cmpc(Rmotor)
	while KIPR.digital(Touch_port) < 1:
		if KIPR.analog(Top_Hat_left_port) > Thresh:
			KIPR.cmpc(Lmotor)
			KIPR.mav(Lmotor,-speed)
			KIPR.mav(Rmotor, speed)
			KIPR.msleep(100)
		elif KIPR.analog(Top_Hat_right_port) > Thresh:
			KIPR.cmpc(Lmotor)
			KIPR.mav(Lmotor, speed)
			KIPR.mav(Rmotor, -speed)
			KIPR.msleep(100)
		else:
			KIPR.mav(Lmotor, speed)
			KIPR.mav(Rmotor, speed)		
	KIPR.ao()		
                
#linefollow till white

def linefollow_cliff(speed):
	KIPR.cmpc(Lmotor)
	KIPR.cmpc(Rmotor)
	while KIPR.analog(Top_Hat_right_port) < 4000 or KIPR.analog(Top_Hat_left_port) < 4000:
		if KIPR.analog(Top_Hat_left_port) > Thresh:
			KIPR.cmpc(Lmotor)
			KIPR.mav(Lmotor,-speed)
			KIPR.mav(Rmotor, speed)
			KIPR.msleep(100)
		elif KIPR.analog(Top_Hat_right_port) > Thresh:
			KIPR.cmpc(Lmotor)
			KIPR.mav(Lmotor, speed)
			KIPR.mav(Rmotor, -speed)
			KIPR.msleep(100)
		else:
			KIPR.mav(Lmotor, speed)
			KIPR.mav(Rmotor, speed)		
	KIPR.ao()				