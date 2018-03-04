from vpython import *
import random
import time

#label(pos=vector(0,8,0),text='Density Flow of Vehicles',color=color.white,height=20,box=False)
#label(pos=vector(12,-5,0),text="Blue : Road\nRed : Congestion\nYellow : Slight traffic\nGreen : Free way",depth=0.3,color=color.white)

def road_simulation(pos_y,neg_y):
	i = -17
	while i <= 17:
		curve(pos=[(-17,pos_y,0),(0,pos_y,0),(i,pos_y,0)],radius=0.05)
		curve(pos=[(-17,neg_y,0),(0,neg_y,0),(i,neg_y,0)],radius=0.05)
		i += 1

j = 0
while j <= 5:
	road_simulation(7.5,4.5)
	red = box(length=30,radius=0.3,color=color.red,pos=vector(0,6,0),width=0.2,height=1)
	red_vehicle = sphere(pos=vector(-16,6.6,0),radius=0.3,color=color.cyan,visible=True)
	i = -16
	while i <= 16:
		rate(10)
		red_vehicle.pos.x = i
		i += 1
		time.sleep(0.5)

	road_simulation(1.5,-1.5)
	yellow = box(length=30,radius=0.3,color=color.yellow,pos=vector(0,-0.1,0),width=0.2,height=1)
	yellow_vehicle = sphere(pos=vector(-16,0.6,0),radius=0.3,color=color.cyan,visible=True)
	i = -16
	while i <= 16:
		rate(10)
		yellow_vehicle.pos.x = i
		i += 1
		time.sleep(0.35)

	road_simulation(-4.5,-7.5)
	green = box(length=30,radius=0.3,color=color.green,pos=vector(0,-6,0),width=0.2,height=1)
	green_vehicle = sphere(pos=vector(-16,-5.4,0),radius=0.3,color=color.magenta,visible=True)
	i = -16
	while i <= 16:
		rate(10)
		green_vehicle.pos.x = i
		i += 1
		time.sleep(0.05)

	time.sleep(1.5)
	green_vehicle.visible = False
	red_vehicle.visible = False
	yellow_vehicle.visible = False

	j += 1
