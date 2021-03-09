############################################################################
# Final Project
# File name: billiard_ball1_1231.py
# add: in air, bounce (actually not used)
############################################################################

from visual import * 

g = 9.8
m = 171E-3
size = 5.715E-2/2
mu_r = 0.01 # rolling friction
mu_k = 0.20
flr_resti_coe = 0.5 # resistance coefficient
zero = vector(0, 0 ,0)
r = vector(0, -size, 0)

I = 2. / 5 * m * size ** 2
f = mu_k * m * g
ro_f = mu_r * m * g # rolling friction

dt = 0.001

def collide(b1, b2):
	if mag(b1.pos-b2.pos) < 2*size and dot(b1.pos-b2.pos, b1.v-b2.v) < 0:
		v1_prime = b1.v - dot(b1.v-b2.v, b1.pos-b2.pos)/mag2(b1.pos-b2.pos)*(b1.pos-b2.pos)
		v2_prime = b2.v - dot(b2.v-b1.v, b2.pos-b1.pos)/mag2(b2.pos-b1.pos)*(b2.pos-b1.pos)
		b1.v = v1_prime
		b2.v = v2_prime
		return True
	return False

def inside(h, d):
	return h**2 + d**2 < 1

class billiard:
	def __init__(self, pos, color):
		self.ball = sphere(pos = pos - r, radius = size, material = materials.earth, color = color, make_trail = True, retain = 600)
		self.pos = pos - r
		self.v = zero
		self.omega = zero
		self.direction = zero # velocity of the point contacting the ground

	def reset(self, pos):
		self.pos = pos - r
		self.ball.pos = self.pos
		self.v = zero
		self.omega = zero
		self.direction = zero

	def hit(self, F, h, d):
		if inside(h, d):
			y = vector(0, 1, 0)
			F_h = F - proj(F, y) # projection on the x-z plane
			R = (d*norm(cross(F_h, y)) + h*y - (1-h**2-d**2)**0.5 * norm(F_h)) * size
			self.v = F_h * dt/ m
			self.omega = cross(R, F) * dt / I
			self.direction = -norm(cross(self.omega, r) + self.v)

	def time_lapse(self, dt):
		if self.pos.y > size  : # in air
			self.v += vector(0, -g, 0) * dt

		elif mag(cross(self.omega, r) + self.v) > 0.01 : # not pure rotation yet
			self.v += self.direction * f / m * dt
			self.omega += cross(r, self.direction) * f / I * dt
		else :
			prev = self.v
			self.v -= ro_f / m * dt * norm(self.v)
			self.omega = cross(self.v, r)/mag2(r)

		if self.pos.y <= size and self.v.y < 0 : # bounce
			self.v.y = -flr_resti_coe * self.v.y

		self.pos += self.v * dt
		self.ball.pos = self.pos
		self.ball.rotate(axis = self.omega, angle = mag(self.omega) * dt)
		self.direction = -norm(cross(self.omega, r) + self.v)

	def stop(self):
		return 0.5 * m * mag2(self.v) + 0.5 * I * mag2(self.omega) <= 0.00005
