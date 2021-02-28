############################################################################
# Final Project
# File name: table_1231_1.py
# table module (only module)
############################################################################

from visual import *
from billiard_ball_1231 import *
t_length = 0.3048 *  8
t_width = 0.3048 * 4
t_height = 0.635 * size * 2

cus_resti_coe = 0.75
cushion_mu = 0.2

class table :
	def __init__(self) :
		self.pos = vector(0, 0 ,0)
		self.box_left = box(pos = vector(-0.5 * t_length-size, t_height/2, 0), length = 2 * size, width = t_width+4*size, height = t_height, color = (0.2, 0.5, 0.7))
		self.box_right = box(pos = vector(0.5 * t_length+size, t_height/2, 0), length = 2 * size, width = t_width+4*size, height = t_height, color = (0.2, 0.5, 0.7))
		self.box_upper = box(pos = vector(0, t_height/2, -0.5 * t_width-size), length = t_length + 4 * size, width = 2 * size, height = t_height, color = (0.2, 0.5, 0.7))
		self.box_lower = box(pos = vector(0, t_height/2, 0.5 * t_width+size), length = t_length + 4 * size, width = 2 * size, height = t_height, color = (0.2, 0.5, 0.7))
		self.floor = box(pos = vector(0, 0, 0), length = t_length+4*size, height = 0.01 * size, width = t_width+4*size, color = (0.1, 0.5, 0.2))
	
	def cushion_compressed(self, ball) :
		if abs(ball.pos.x) >= t_length/2 - size and ball.v.x * ball.pos.x > 0 :
			N = -vector(1, 0, 0) * m * (1 + cus_resti_coe) * ball.v.x / dt
			cpr_r = vector(0, t_height - size, 0) + sqrt(size ** 2 - (size - t_height) ** 2)*norm(vector(ball.pos.x, 0, 0))
			friction = -norm(cross(ball.omega, cpr_r) + vector(0, 0, ball.v.z)) * mag(N) * cushion_mu
			ball.v.x = -cus_resti_coe * ball.v.x
			ball.v.z += friction.z * dt
			ball.omega += cross(cpr_r, N + friction) / I * dt

		if abs(ball.pos.z) >= t_width/2 - size and ball.v.z * ball.pos.z > 0 :
			N = -vector(0, 0, 1) * m * (1 + cus_resti_coe) * ball.v.z / dt
			cpr_r = vector(0, t_height - size, 0) + sqrt(size ** 2 - (size - t_height) ** 2)*norm(vector(0, 0, ball.pos.z))
			friction = -norm(cross(ball.omega, cpr_r) + vector(ball.v.x, 0, 0)) * mag(N) * cushion_mu
			ball.v.z = -cus_resti_coe * ball.v.z
			ball.v.x += friction.x * dt
			ball.omega += cross(cpr_r, N + friction) / I * dt
