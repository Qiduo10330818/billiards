############################################################################
# Final Project
# File name: main_0103_2.py
# 
############################################################################

from visual import *
from visual.graph import *
from billiard_ball_1231 import *
from table_1231_1 import *
from random import random
#import matplotlib.pyplot as plt

scene = display(width = 600, height = 300, background = (0.5, 0.5, 0.6), center = vector(0, size/2.0, 0))
scene.forward = vector(0, -1, 0)
scene1 = gdisplay(x = 600, width = 800, height = 800, title = "0103_1", xtitle = "incident_angle", ytitle = "rebound_angle", background = (0.2, 0.2, 0.2))
scene2 = gdisplay(x = 600, width = 800, height = 800, title = "0103_1", xtitle = "incident_angle", ytitle = "rebound_speed/incident_speed", background = (0.2, 0.2, 0.2))

x = gdots(gdisplay = scene1)
y = gdots(gdisplay = scene2)


table1 = table()
L = 0.3048 * 1.2
pos = vector(-0.3048 * 2, 0, -0.5)
h = 0.0
d = 0.0
ball = billiard(pos, color.orange)
for j in range(-9, 10, 3) :
	#h = j / 8.0
	d = j / 10.0
	print 'd, h =', d, h
	for i in range(80) : # different incident angle
		incident_angle = i / 180.0 * pi
		F = vector(0, -100, -1000 * 0.35)
		F = F.rotate(axis = vector(0, 1, 0), angle = -incident_angle)
		ball.reset(vector(-L * sin(incident_angle), 0, L * cos(incident_angle)-0.3048 * 2))
		ball.hit(F, h, d)
		while True :
			rate(1000 * 2)
			if ball.v == vector(0, 0, 0) or mag(cross(ball.omega, r) + ball.v) < 0.01 :
			#if ball.stop():
				break
			ball.time_lapse(dt)
			pre_v = vector(ball.v)
			table1.cushion_compressed(ball)	
			if ball.v.z > 0 :
				x.plot(pos = (incident_angle / pi * 180, diff_angle(ball.v, vector(0, 0, 1)) / pi * 180))
				#if abs(pre_v)
				y.plot(pos = (incident_angle / pi * 180, abs(ball.v) / abs(pre_v)))
				break
	x.color = (0.5 + random() / 2, 0.5 + random() / 2, 0.5 + random() / 2)
	y.color = x.color

print 'end'

