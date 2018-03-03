from vpython import *
import random
import time
import pygame

pygame.init()

label(pos=vector(0,8,0),text='Density Flow of Vehicles',color=color.white,box=False,height=20)
obj = box(length=6,width=0.2,color=color.yellow,pos=vector(0,0,0))

density_graph = gcurve(color=color.blue)

#green_music = pygame.mixer.Sound('green.wav')
#yellow_music = pygame.mixer.Sound('yellow.wav')
#red_music = pygame.mixer.Sound('red.wav')

mix1 = box(length=6,width=0.2,color=color.green,pos=vector(-15,0,0))
mix2 = box(length=10,width=0.2,color=color.yellow,pos=vector(-9,0,0))
mix3 = box(length=9,width=0.2,color=color.red,pos=vector(0,0,0))

value = 0
while (value <= 20):
	rate(30)
	obj.pos = vector(-15,0,0)
	obj.length = random.choice(range(5,25))

	if 5 < obj.length <= 8:
		mix1.visible = False
		mix2.visible = False
		mix3.visible = False
		obj.color = color.green
		#pygame.mixer.Sound.play(green_music)

	if 8 < obj.length <= 13:
		mix1.visible = False
		mix2.visible = False
		mix3.visible = False
		obj.color = color.yellow
		#pygame.mixer.Sound.play(yellow_music)

	if 13 < obj.length <= 19:
		mix1.visible = False
		mix2.visible = False
		mix3.visible = False
		obj.color = color.red
		#pygame.mixer.Sound.play(red_music)

	if 20 <= obj.length <= 25:
		obj.visible = False
		mix1.visible = True
		mix2.visible = True
		mix3.visible = True
	else:
		mix1.visible = False
		mix2.visible = False
		mix3.visible = False
		obj.visible = True

	density_graph.plot((value,obj.length))

	value += 1
	
	time.sleep(5)
