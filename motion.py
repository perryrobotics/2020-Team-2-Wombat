#!/usr/bin/python
import os, sys
import ctypes
from constants import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")



    
def forward(speed, ticks):
	KIPR.cmpc(Lmotor)
	KIPR.mav(Lmotor, speed);
	KIPR.mav(Rmotor, speed);
	while KIPR.gmpc(Lmotor) < ticks:
		pass
	KIPR.ao()
            
def backward(speed, ticks):
	KIPR.cmpc(Lmotor)
	KIPR.mav(Lmotor, -speed);
	KIPR.mav(Rmotor, -speed);
	while KIPR.gmpc(Lmotor) > -ticks:
		pass
	KIPR.ao()

def left(speed, ticks):
	KIPR.cmpc(Rmotor)
  	KIPR.cmpc(Lmotor)
	KIPR.mav(Lmotor,-speed)
	KIPR.mav(Rmotor, speed)
	while KIPR.gmpc(Rmotor) < ticks:
		pass
	KIPR.ao()

def left_power(speed, ticks):
	KIPR.cmpc(Rmotor)
  	KIPR.cmpc(Lmotor)
	KIPR.mav(Lmotor,-speed)
	KIPR.mav(Rmotor,speed*2)
	while KIPR.gmpc(Rmotor) < ticks:
		pass
	KIPR.ao()
            
def right(speed, ticks):
	KIPR.cmpc(Lmotor)
	KIPR.mav(Lmotor, speed)
	KIPR.mav(Rmotor, -speed)
	while KIPR.gmpc(Lmotor) < ticks:
		pass
	KIPR.ao()