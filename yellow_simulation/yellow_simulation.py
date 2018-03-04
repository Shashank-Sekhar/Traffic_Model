from vpython import *
import time
import random

label(pos=vector(0,8,0),text='Density Flow of Vehicles',color=color.white,height=20,box=False)
label(pos=vector(12,-5,0),text="Yellow : Slight traffic",depth=0.3,color=color.white)

def road_simulation():
	i = -17
	while i <= 17:
		rate(10)
		curve(pos=[(-17,1.5,0),(0,1.5,0),(i,1.5,0)],radius=0.05)
		curve(pos=[(-17,-1.5,0),(0,-1.5,0),(i,-1.5,0)],radius=0.05)
		i += 1
		time.sleep(0.01)

road_simulation()

red = box(pos=vector(0,0,0),color=color.yellow,width=0.2,length=30,height=1.2)
vehicle = sphere(pos=vector(-16,0,0),radius=0.3,color=color.cyan,visible=True)

def vehicle_movement():
	i = -16
	while i <= 16:
		rate(20)
		vehicle.pos.x = i
		i += 1
		time.sleep(0.3)

for i in range(60): # repeat for _ times
	vehicle_movement()
