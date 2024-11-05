# import all my core function
from pygame.mouse import set_pos
from pygame.sprite import collide_rect
from __init__ import *

data = {}

history_reeded = False

pygame.init() # init a pygame

screen_width = 0 # screen width
screen_heigth = 0# screen height
screen_Fullscreen = pygame.FULLSCREEN # screen FULLSCREEN

screen = pygame.display.set_mode((screen_width, screen_heigth), pygame.FULLSCREEN) # display
display = pygame.Surface((300,200))

game_map = {}
pygame.mouse.set_pos(0, 0)

display_run = True # run global cycle
menu_run = True # run menu
game_run = False # run game
clock = pygame.time.Clock() # one time

game_load = True

text_time = 0
true_scroll = [0, 0]

player_form = 1

story_1_1 = StoryText(list('Many generations ago there was such a clan what has name+- Silver. He was famous for his wealth and he can controlled+all economy of the world. But his main power was not money.'), True)
story_1_2 = StoryText(list('Members of this clan were known to people all over +the world. The main goal of the clan was to find+the end of this world. So far, the end of the world+has not been found. Many generations have explored this +world,but in the last century the Silver clan was+destroyed by Union of the Great Kingdoms. The cause+of the destruction is unknown'), False)
story_1_3 = StoryText(list('You need back repotation of the Silver Clan.+And get economy of this world. It the world+infinite? Union of the Great Kingdoms? Who is my clan?'), False)
end = StoryText('', False)


tiles_indexs = {
	'd1': [d1, True], 'd2': [d2, True], 'd3': [d3, True],
	'gb1': [gb1, True], 'gb2': [gb2, True], 'gb3': [gb3, True], 'gb4': [gb4, True],
	's1': [s1, True],
	'g1': [g1, False], 'g2': [g2, False], 'g3': [g3, False],
	'f1': [rf, False], 'f2': [bf, False],
	'tr1': [tr1, False], 'tr2': [tr2, False], 'tr3': [tr3, False],
	'io': [io, True], 'go': [go, True], 'copo': [copo, True], 'co': [co, True]
}

player.anim_data = {
	'idle': [('data/png/player/idle_1'), ('data/png/player/idle_2')],
	'run': [('data/png/player/run_1'), ('data/png/player/run_2')],
	'fall': [('data/png/player/fall_1'), ('data/png/player/fall_2')],
	'landing': [('data/png/player/landing_1'), ('data/png/player/landing_2')],
	'jumping': [('data/png/player/jumping_1'), ('data/png/player/jumping_2')],
	'start_jump': [('data/png/player/startjump_1'), ('data/png/player/startjump_2')],
	'transform': [('data/png/player/transform_1'), ('data/png/player/transform_2')],
	
}


class time(object):
	def __init__(self, AnimCount):
		super(time, self).__init__()
		self.AnimCount = AnimCount
clouds = True
menuAnim = time(0)

sound_volume = 0
music_volume = 0

class Frame(object):
	'''Class of small frames'''
	def __init__(self, background, run):
		super(Frame, self).__init__()
		self.background = background
		self.run = run

main_menu = Frame(('data/png/menu', '0.png'), True)
option_menu = Frame(('data/png/menu/option', '0.png'), False)
option_sound_menu = Frame(('data/png/menu/option/sound', '0.png'), False)
option_graphics_menu = Frame(('data/png/menu/option/graphics', '0.png'), False)
option_screen_menu = Frame(('data/png/menu/option/screen', '0.png'), False)
story_screen = Frame(None, False)
game = Frame(None, False)

main_menu_buttons = [pygame.Rect(27, 80, 77, 12), pygame.Rect(27, 100, 77, 12), pygame.Rect(27, 120, 77, 12)]
option_menu_buttons = [pygame.Rect(27, 80, 77, 12), pygame.Rect(27, 100, 77, 12), pygame.Rect(27, 120, 77, 12), pygame.Rect(27, 140, 77, 12)]
option_sound_menu_buttons = [pygame.Rect(27, 80, 77, 16), pygame.Rect(27, 100, 77, 16), pygame.Rect(27, 120, 77, 12)]
option_graphics_menu_buttons = [pygame.Rect(27, 80, 77, 12), pygame.Rect(27, 100, 77, 12)]
option_screen_menu_buttons = [pygame.Rect(27, 80, 77, 12), pygame.Rect(27, 100, 77, 12), pygame.Rect(27, 120, 77, 12), pygame.Rect(27, 140, 77, 12)]

# update frame function
def menu_Update(scr):
	load_img(display, scr.background, 0, 0, False)
	clock.tick(FPS)

background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]


# global cycle
while display_run:

	while game_load:
		with open('data.json') as json_data:
			data = json.load(json_data)

		for var in data:
			for local_var in list(locals()):
				if var == local_var:
					locals()[local_var] = data[local_var]

			for global_var in list(globals()):
				if var == global_var:
					locals()[global_var] = data[global_var]

		game_load = False


	while menu_run:

		while main_menu.run:
			menu_Update(main_menu)
			mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)
			pygame.mouse.set_visible(False)

			for event in pygame.event.get():
				if event.type == QUIT:
					with open('data.json', 'w') as json_data:
						json.dump(data, json_data)
					sys.exit()

				if event.type == MOUSEBUTTONDOWN:
					if pygame.Rect.colliderect(mouse_rect, main_menu_buttons[0]):
						if not history_reeded:
							story_screen.run = True
						else:
							game.run = True
						game_run = True
						menu_run = False
						main_menu.run = False
						

					if pygame.Rect.colliderect(mouse_rect, main_menu_buttons[1]):
						main_menu.run = False
						option_menu.run = True

					if pygame.Rect.colliderect(mouse_rect, main_menu_buttons[2]):
						with open('data.json', 'w') as json_data:
							json.dump(data, json_data)	
						sys.exit()


			load_anim(display, 'data/png/player/idle_2', 170, 115, menuAnim, 80, True)
			load_anim(display, 'data/png/player/idle_1', 186, 115, menuAnim, 80, False)
			load_img(display, ('data/png/menu/ui', '0.png'), main_menu_buttons[0].x, main_menu_buttons[0].y, False)
			load_img(display, ('data/png/menu/ui', '1.png'), main_menu_buttons[1].x, main_menu_buttons[1].y, False)
			load_img(display, ('data/png/menu/ui', '2.png'), main_menu_buttons[2].x, main_menu_buttons[2].y, False)
			

			for button in main_menu_buttons:
				if pygame.Rect.colliderect(mouse_rect, button):
					Outline(display, ('data/png/menu/option/screen/ui', '0.png'), button.x, button.y, 1, (255, 255, 255), False)

			load_img(display, ('data/png', 'cursor.png'), mouse_rect.x, mouse_rect.y, False)
			screen.blit(pygame.transform.scale(display,screen.get_size()),(0, 0))
			pygame.display.update()

		while option_menu.run:
			menu_Update(option_menu)
			mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)
			pygame.mouse.set_visible(False)

			for event in pygame.event.get():
				if event.type == QUIT:
					with open('data.json', 'w') as json_data:
						json.dump(data, json_data)	
					sys.exit()


				if event.type == MOUSEBUTTONDOWN:
					if pygame.Rect.colliderect(mouse_rect, option_menu_buttons[0]):
						option_graphics_menu.run = True
						option_menu.run = False

					if pygame.Rect.colliderect(mouse_rect, option_menu_buttons[1]):
						option_sound_menu.run = True
						option_menu.run = False

					if pygame.Rect.colliderect(mouse_rect, option_menu_buttons[2]):
						option_screen_menu.run = True
						option_menu.run = False

					if pygame.Rect.colliderect(mouse_rect, option_menu_buttons[3]):
						menu_run = True
						main_menu.run = True
						option_menu.run = False


			load_img(display, ('data/png/menu/option/ui/sh', '0.png'), 170, 70, False)
			load_img(display, ('data/png/menu/option/ui', '0.png'), option_menu_buttons[0].x, option_menu_buttons[0].y, False)
			load_img(display, ('data/png/menu/option/ui', '1.png'), option_menu_buttons[1].x, option_menu_buttons[1].y, False)
			load_img(display, ('data/png/menu/option/ui', '2.png'), option_menu_buttons[2].x, option_menu_buttons[2].y, False)
			load_img(display, ('data/png/menu/ui', '2.png'), option_menu_buttons[3].x, option_menu_buttons[3].y, False)

			for button in option_menu_buttons:
				if pygame.Rect.colliderect(mouse_rect, button):
					Outline(display, ('data/png/menu/option/screen/ui', '0.png'), button.x, button.y, 1, (255, 255, 255), False)

			load_img(display, ('data/png', 'cursor.png'), mouse_rect.x, mouse_rect.y, False)
			screen.blit(pygame.transform.scale(display,screen.get_size()),(0, 0))
			pygame.display.update()


		while option_sound_menu.run:
			menu_Update(option_sound_menu)
			mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)
			pygame.mouse.set_visible(False)

			for event in pygame.event.get():
				if event.type == QUIT:
					with open('data.json', 'w') as json_data:
						json.dump(data, json_data)	
					sys.exit()
						
				if event.type == MOUSEBUTTONDOWN:

					if pygame.Rect.colliderect(mouse_rect, option_menu_buttons[2]):
						option_sound_menu.run = False
						option_menu.run = True

			load_anim(display, 'data/png/menu/option/sound/ui/sn', 170, 70, menuAnim, 40, False)
			load_img(display, ('data/png/menu/option/sound/ui', '0.png'), option_sound_menu_buttons[0].x, option_sound_menu_buttons[0].y, False)
			load_img(display, ('data/png/menu/option/sound/ui', '1.png'), option_sound_menu_buttons[1].x, option_sound_menu_buttons[1].y, False)
			load_img(display, ('data/png/menu/ui', '2.png'), option_sound_menu_buttons[2].x, option_sound_menu_buttons[2].y, False)

			if pygame.Rect.colliderect(mouse_rect, option_sound_menu_buttons[2]):
				Outline(display, ('data/png/menu/ui', '2.png'), option_sound_menu_buttons[2].x, option_sound_menu_buttons[2].y, 1, (255, 255, 255), False)

			load_img(display, ('data/png', 'cursor.png'), mouse_rect.x, mouse_rect.y, False)
			screen.blit(pygame.transform.scale(display,screen.get_size()),(0, 0))
			pygame.display.update()


		while option_graphics_menu.run:
			menu_Update(option_graphics_menu)
			mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)
			pygame.mouse.set_visible(False)

			for event in pygame.event.get():
				if event.type == QUIT:
					with open('data.json', 'w') as json_data:
						json.dump(data, json_data)	
					sys.exit()


				if event.type == MOUSEBUTTONDOWN:

					if pygame.Rect.colliderect(mouse_rect, option_graphics_menu_buttons[1]):
						option_graphics_menu.run = False
						option_menu.run = True

			load_img(display, ('data/png/menu/option/graphics/ui', '0.png'), option_graphics_menu_buttons[0].x, option_graphics_menu_buttons[0].y, False)
			load_img(display, ('data/png/menu/ui', '2.png'), option_graphics_menu_buttons[1].x, option_graphics_menu_buttons[1].y, False)

			for button in option_graphics_menu_buttons:
				if pygame.Rect.colliderect(mouse_rect, button):
					Outline(display, ('data/png/menu/option/screen/ui', '0.png'), button.x, button.y, 1, (255, 255, 255), False)

			load_img(display, ('data/png', 'cursor.png'), mouse_rect.x, mouse_rect.y, False)
			screen.blit(pygame.transform.scale(display,screen.get_size()),(0, 0))
			pygame.display.update()


		while option_screen_menu.run:
			menu_Update(option_screen_menu)
			mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)
			pygame.mouse.set_visible(False)

			for event in pygame.event.get():
				if event.type == QUIT:
					with open('data.json', 'w') as json_data:
						json.dump(data, json_data)	
					sys.exit()


				if event.type == MOUSEBUTTONDOWN:

					if pygame.Rect.colliderect(mouse_rect, option_screen_menu_buttons[3]):
						option_screen_menu.run = False
						option_menu.run = True

			load_img(display, ('data/png/menu/option/screen/ui', '0.png'), option_screen_menu_buttons[0].x, option_screen_menu_buttons[0].y, False)
			load_img(display, ('data/png/menu/option/screen/ui', '1.png'), option_screen_menu_buttons[1].x, option_screen_menu_buttons[1].y, False)
			load_img(display, ('data/png/menu/option/screen/ui', '2.png'), option_screen_menu_buttons[2].x, option_screen_menu_buttons[2].y, False)
			load_img(display, ('data/png/menu/ui', '2.png'), option_screen_menu_buttons[3].x, option_screen_menu_buttons[3].y, False)

			for button in option_screen_menu_buttons:
				if pygame.Rect.colliderect(mouse_rect, button):
					Outline(display, ('data/png/menu/option/screen/ui', '0.png'), button.x, button.y, 1, (255, 255, 255), False)

			load_img(display, ('data/png', 'cursor.png'), mouse_rect.x, mouse_rect.y, False)
			screen.blit(pygame.transform.scale(display,screen.get_size()),(0, 0))
			pygame.display.update()


	# game content
	while game_run:
		while story_screen.run:
			pygame.mouse.set_visible(False)
			title_story_text = ""

			clock.tick(FPS)
			display.fill((0, 0, 0))
			skip_text = False

			for event in pygame.event.get():
				if event.type == QUIT:
					with open('data.json', 'w') as json_data:
						json.dump(data, json_data)	
					sys.exit()			

				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						with open('data.json', 'w') as json_data:
							json.dump(data, json_data)	
						sys.exit()

			screen.blit(pygame.transform.scale(display,screen.get_size()),(0,0))

			pygame.display.update()

			story_1_1.story_bliting(screen, display, basic_pixel, title_story_text, story_1_2, skip_text, 120)
			story_1_2.story_bliting(screen, display, basic_pixel, title_story_text, story_1_3, skip_text, 120)
			story_1_3.story_bliting(screen, display, basic_pixel, title_story_text, end, skip_text, 120)

			if end.true:
				pygame.mouse.set_pos(0, 0)
				history_reeded = True
				data[retrieve_name(history_reeded)[0]]=history_reeded
				game.run = True
				story_screen.run = False
			

		while game.run:

			clock.tick(FPS)
			display.fill((138, 235, 241))
			keys = pygame.key.get_pressed()
			mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)
			display_enable = pygame.Rect(0,0, screen.get_width(), screen.get_height())
			pygame.mouse.set_visible(False)
			true_scroll[0] += (player.rect.x-true_scroll[0]-152)/20
			true_scroll[1] += (player.rect.y-true_scroll[1]-106)/20
			scroll = true_scroll.copy()
			scroll[0] = int(scroll[0])
			scroll[1] = int(scroll[1])

			for event in pygame.event.get():
				if event.type == QUIT:
					with open('data.json', 'w') as json_data:
						json.dump(data, json_data)	
					sys.exit()				

				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						with open('data.json', 'w') as json_data:
							json.dump(data, json_data)	
						sys.exit()
			
			for background_object in background_objects:
				obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0],background_object[1][1]-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
				if background_object[0] == 0.5:
					pygame.draw.rect(display,(20,170,150),obj_rect)
					
				else:
					pygame.draw.rect(display,(15,76,73),obj_rect)


			tile_rects = []
			for y in range(3):
				for x in range(7):
					target_x = x - 1 + int(round(scroll[0]/(part_size*16)))
					target_y = y + int(round(scroll[1]/(part_size*16)))
					target_chunk = str(target_x) + ';' + str(target_y)
					if target_chunk not in game_map:
						game_map[target_chunk] = generate_chunk(target_x,target_y)
					
					for tile in game_map[target_chunk]:
						if tile[1][0] == 'tr1' or tile[1][0] == 'tr2' or tile[1][0] == 'tr3':
							display.blit(tiles_indexs[tile[1][0]][0][tile[1][1]],(tile[0][0]*16-scroll[0],tile[0][1]*16-scroll[1]))
						else:
							display.blit(tiles_indexs[tile[1]][0],(tile[0][0]*16-scroll[0],tile[0][1]*16-scroll[1]))
							
							if tiles_indexs[tile[1]][1]:
								tile_rects.append(pygame.Rect(tile[0][0]*16,tile[0][1]*16,16,16))

			if player.movem[1] > 1:
				if player.position == 'left':
					load_anim(display, player.anim_data['fall'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 16, True)
				if player.position == 'right':
					load_anim(display, player.anim_data['fall'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 16, False)
			elif player.movem[1] < -1:
				if player.position == 'left':
					load_anim(display, player.anim_data['jumping'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 48, True)
				if player.position == 'right':
					load_anim(display, player.anim_data['jumping'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 48, False)

			elif keys[K_w]:
				if player.position == 'left':
					load_anim(display, player.anim_data['start_jump'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 48, True)
				if player.position == 'right':
					load_anim(display, player.anim_data['start_jump'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 48, False)

			elif player.movem[0] == 0:
				if player.position == 'left':
					load_anim(display, player.anim_data['idle'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 80, True)
				if player.position == 'right':
					load_anim(display, player.anim_data['idle'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 80, False)

			elif player.movem[0] > 0 or player.movem[0] < 0:
				if player.position == 'left':
					load_anim(display, player.anim_data['run'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 48, True)
				if player.position == 'right':
					load_anim(display, player.anim_data['run'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 48, False)

			elif player.movem[1] == 0:
				if player.position == 'left':
					load_anim(display, player.anim_data['landing'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 32, True)
				if player.position == 'right':
					load_anim(display, player.anim_data['landing'][player_form], player.rect.x-scroll[0], player.rect.y-scroll[1], player, 32, False)


			player.movem = [0,0]
			if keys[K_a]:
				player.movem[0] -= player.vel
				player.position = 'left'
			if keys[K_d]:
				player.movem[0] += player.vel
				player.position = 'right'
			player.movem[1]+=player.vertical
			player.vertical += 0.2							
			
			if player.vertical > 3:
				player.vertical = 3



			player.rect,collisions = move(player.rect,player.movem, tile_rects)
			
			
			if collisions['bottom']:
				player.air = 0
				player.vertical = 0	
				
			else:
				player.air += 1	

			if keys[K_w]:

				if player.air < 6:
					player.vertical = -3.1
			


			load_img(display, ('data/png', 'cursor.png'), mouse_rect.x, mouse_rect.y, False)
			screen.blit(pygame.transform.scale(display,screen.get_size()),(0, 0))
			pygame.display.update()
