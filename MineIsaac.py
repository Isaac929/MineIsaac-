from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

application.development_mode = False

window.borderless = False
window.set_title("MineIsaac")
app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/marble_block')
dirt_texture  = load_texture('assets/dirt_block.png')
wood_texture = load_texture('assets/wood_block.png')
bush_texture = load_texture('assets/bush_block.png')
glass_texture = load_texture('assets/glass_block.png')
gravel_texture = load_texture ('assets/gravel_block.png')
sand_texture = load_texture ('assets/sand_block.png')
cobble_texture = load_texture ('assets/cobble_block.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
punch_sound   = Audio('assets/punch_sound',loop = False, autoplay = False)
block_pick = 1

def update():
	global block_pick

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4
	if held_keys['5']: block_pick = 5
	if held_keys['6']: block_pick = 6
	if held_keys['7']: block_pick = 7
	if held_keys['8']: block_pick = 8
	if held_keys['9']: block_pick = 9
	if held_keys['0']: block_pick = 0
	

class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)

#def update():
        #test.x = Entity(model = '', scale = (,,), position = (,))

	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)
				if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = bush_texture)
				if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = glass_texture)
				if block_pick == 8: voxel = Voxel(position = self.position + mouse.normal, texture = gravel_texture)
				if block_pick == 9: voxel = Voxel(position = self.position + mouse.normal, texture = sand_texture)
				if block_pick == 0: voxel = Voxel(position = self.position + mouse.normal, texture = cobble_texture)

			if key == 'left mouse down':
				punch_sound.play()
				destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)

for z in range(20):
	for x in range(20):
		voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
player.mouse_sensitivity = (4.0, 4.0)
sky = Sky()
hand = Hand()

app.run()
