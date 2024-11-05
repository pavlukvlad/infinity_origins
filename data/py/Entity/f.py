import pygame
from pygame.mouse import set_pos

class Entity(object):
	def __init__(self, rect, vel, position, movem, vertical, air, anim_data, AnimCount):
		super(Entity, self).__init__()
		self.rect=rect
		self.vel=vel
		self.movem=movem
		self.position=position
		self.vertical = vertical
		self.air=air
		self.anim_data=anim_data
		self.AnimCount = AnimCount

player = Entity(pygame.Rect(250, 125, 16, 16), 1, 'left', [0, 0], 0, 0, {}, 0)


class cloud(object):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
		
    def draw(self, surf, x, y):
        pygame.draw.circle(surf, (255,255,255), (x,y), 10)
