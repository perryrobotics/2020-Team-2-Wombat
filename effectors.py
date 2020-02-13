#!/usr/bin/python
import os, sys
import ctypes
from constants import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

    
    
def move_servo_slow(port, start, end, step):
	if start > end:
		step = -step
	for pos in range(start, end, step):
		KIPR.set_servo_position(port, pos)
		KIPR.msleep(40)
 	KIPR.set_servo_position(port, end)
    
def arm_up(step):
  	start = KIPR.get_servo_position(ARM)
   	move_servo_slow( ARM, start, ARM_UP, step)
        
def arm_down(step):
  	start = KIPR.get_servo_position(ARM)
	move_servo_slow( ARM, start, ARM_DOWN, step)
        
def arm_deep(step):
  	start = KIPR.get_servo_position(ARM)
	move_servo_slow( ARM, start, ARM_DEEP, step)

def arm_half(step):
	start = KIPR.get_servo_position(ARM)
	move_servo_slow( ARM, start, ARM_HALF, step)

def arm_yellow(step):
	start = KIPR.get_servo_position(ARM)
	move_servo_slow( ARM, start, ARM_YELLOW, step)
        
       
def arm_start(step):
	start = KIPR.get_servo_position(ARM)
   	move_servo_slow( ARM, start, ARM_START, step)
        
def claw_close(step):
	start = KIPR.get_servo_position(CLAW)
   	move_servo_slow( CLAW, start, CLAW_CLOSED, step)
 
def claw_open(step):
	start = KIPR.get_servo_position(CLAW)
   	move_servo_slow( CLAW, start, CLAW_OPEN, step)
        
def claw_yellow(step):
	start = KIPR.get_servo_position(CLAW)
   	move_servo_slow( CLAW, start, CLAW_YELLOW, step)
        
def tail_up():
	KIPR.set_servo_position(TAIL, TAIL_UP)
  	KIPR.msleep(350)
        
def tail_down():
	KIPR.set_servo_position(TAIL, TAIL_DOWN)
  	KIPR.msleep(350)
        
