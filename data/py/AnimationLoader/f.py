

import pygame, os, sys, os.path

FPS = 40

# File importing
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)

# Image loader
def load_img(display, path, x, y, flip):
	if flip:
		display.blit(pygame.transform.flip(pygame.image.load(resource_path(os.path.join(path[0], path[1]))).convert_alpha(), False, False), (x, y))
	elif not flip:
		display.blit(pygame.image.load(resource_path(os.path.join(path[0], path[1]))).convert_alpha(), (x, y))

def fast_load_img(display, image, x, y, flip):
	if flip:
		display.blit(pygame.transform.flip(image.convert_alpha(), False, False), (x, y))
	elif not flip:
		display.blit(image.convert_alpha(), (x, y))
		
# Animation loader
def load_anim(display, path, x, y, a_count, anim_time, flip):

	if a_count.AnimCount + 1 >= anim_time: # Animation replay
		a_count.AnimCount = 0

	if flip:
		display.blit(pygame.transform.flip(pygame.image.load(resource_path(os.path.join(path, (str(a_count.AnimCount // (anim_time // len([name for name in os.listdir(path)]))) + '.png')))), True, False), (x, y))

	elif not flip:
		display.blit(pygame.image.load(resource_path(os.path.join(path, (str(a_count.AnimCount // (anim_time // len([name for name in os.listdir(path)]))) + '.png')))), (x, y))

	a_count.AnimCount += 1

# Image outline
def Outline(display, path, x, y, line, color, fliped):
	if fliped:
		mask = pygame.mask.from_surface(pygame.transform.flip(pygame.image.load(resource_path(os.path.join(path[0], path[1])))), True, False)

	elif not fliped:
		mask = pygame.mask.from_surface(pygame.image.load(resource_path(os.path.join(path[0], path[1]))))
	mask_outline = mask.outline()
	n = 0
	for point in mask_outline:
		mask_outline[n] = (point[0] + x, point[1] + y)
		n += 1
	pygame.draw.polygon(display,color,mask_outline,line)
	return mask