from vpython import *
import random
import time

label(pos=vector(0,8,0),text='Density Flow of Vehicles',color=color.white,height=20,box=False)
label(pos=vector(12,-5,0),text="Blue : Road\nRed : Congestion\nYellow : Slight traffic\nGreen : Free way",depth=0.3,color=color.white)

def road_simulation():
	i = -17
	while i <= 17:
		rate(10)
		curve(pos=[(-17,1.5,0),(0,1.5,0),(i,1.5,0)],radius=0.05)
		curve(pos=[(-17,-1.5,0),(0,-1.5,0),(i,-1.5,0)],radius=0.05)
		i += 1
		time.sleep(0.01)

road_simulation()

time.sleep(0.4)
obj = box(length=30,width=0.2,color=color.cyan,pos=vector(0,0,0))
arrow(pos=vector(-18,0,0),axis=vector(2,0,0),color=color.white)
vehicle = sphere(pos=vector(-16,0.9,0),radius=0.2,color=color.magenta,visible=True)

time.sleep(6)

def different_movements(rate_value,time_factor):
	i = -16
	while i <= 16:
		rate(rate_value)
		vehicle.pos.x = i
		i += 1
		time.sleep(time_factor)

def green_movement(): # 10, 0.02
	different_movements(10,0.02)

def yellow_movement(): # 6, 0.3
	different_movements(6,0.3)

def red_movement(): # 3, 0.5
	different_movements(3,0.5)
	
density_graph = gcurve(color=color.blue)

value = 0
while (value <= 20):
	rate(30)
	rand_value = random.choice(range(3,20))

	if 3 < rand_value <= 8:
		obj.color = color.green
		green_movement()

	if 8 < rand_value <= 13:
		obj.color = color.yellow
		yellow_movement()

	if 13 < rand_value <= 20:
		obj.color = color.red
		red_movement()

	density_graph.plot((value,rand_value))

	value += 1
	
	time.sleep(1)
