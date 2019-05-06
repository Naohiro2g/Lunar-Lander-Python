x = 100
y = 0

lander = Actor('rocket')
lander.topleft = 0,0

WIDTH = 300
HEIGHT = 300

ang = 0

def draw():
	screen.clear()
	lander.draw()
	screen.draw.line((500, 500), (500, 500),(255, 255, 255))
	lander.angle = ang

def update(dt):
	print(dt)
	lander.right += 2
	if lander.right >= WIDTH:
		lander.left = 0

def on_mouse_down(pos):
	if lander.collidepoint(pos):
		lander.left = 0

def on_key_down(key):
	global ang
	if key.name == 'LEFT':
		rotate(ang+13)
	elif key.name == 'RIGHT':
		rotate(ang-13)

def rotate(newAng):
	global ang
	if newAng > 90:
		ang = 90
	elif newAng < -90:
		ang = -90
	else:
		ang = newAng
	lander.angle = ang