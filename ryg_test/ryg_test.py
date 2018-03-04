from vpython import *
import random
import time

label(pos=vector(0,8,0),text='Density Flow of Vehicles',color=color.white,depth=20,box=False,height=20)
label(pos=vector(12,-5,0),text="Blue : Road\nRed : Congestion\nYellow : Slight traffic\nGreen : Free way",depth=0.3,color=color.white)

i = -17
while i <= 17:
	rate(10)
	curve(pos=[(-17,1,0),(0,1,0),(i,1,0)],radius=0.05)
	curve(pos=[(-17,-1,0),(0,-1,0),(i,-1,0)],radius=0.05)
	i += 1
	time.sleep(0.01)

time.sleep(0.4)
obj = box(length=30,width=0.2,color=color.cyan,pos=vector(0,0,0))
time.sleep(3)

mix1 = cylinder(length=8,radius=0.4,color=color.green,pos=vector(-15,0,0))
mix2 = cylinder(length=12,radius=0.4,color=color.yellow,pos=vector(-7,0,0))
mix3 = cylinder(length=10,radius=0.4,color=color.red,pos=vector(5,0,0))

mix1.visible = False
mix2.visible = False
mix3.visible = False

density_graph = gcurve(color=color.blue)

value = 0
while (value <= 20):
	rate(30)
	rand_value = random.choice(range(5,25))

	if 5 < rand_value <= 8:
		mix1.visible = False
		mix2.visible = False
		mix3.visible = False
		obj.color = color.green

	if 8 < rand_value <= 13:
		mix1.visible = False
		mix2.visible = False
		mix3.visible = False
		obj.color = color.yellow

	if 13 < rand_value <= 20:
		mix1.visible = False
		mix2.visible = False
		mix3.visible = False
		obj.color = color.red

	if 20 < rand_value <= 25:
		obj.visible = False
		mix1.visible = True
		mix2.visible = True
		mix3.visible = True
	else:
		mix1.visible = False
		mix2.visible = False
		mix3.visible = False
		obj.visible = True

	density_graph.plot((value,rand_value))

	value += 1
	
	time.sleep(5)
