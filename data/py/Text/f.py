import pygame, os, sys, time
from pygame.locals import *

clock = pygame.time.Clock()

# File importing
def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)




def clip(surf,x,y,x_size,y_size):
    handle_surf = surf.copy()
    clipR = pygame.Rect(x,y,x_size,y_size)
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


class Font():
    def __init__(self, path):
        self.spacing = 1
        self.new_line = 1
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
        font_img = pygame.image.load(resource_path(os.path.join(path[0], path[1])))
        current_char_width = 0
        self.characters = {}
        character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                self.characters[self.character_order[character_count]] = char_img.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()
        self.new_line_space_height = self.characters['A'].get_height()

    def render(self, surf, text, loc):
        x_offset = 0
        y_offset = 0
        for char in text:
            if char != ' ' and char != '+':
                surf.blit(self.characters[char], (loc[0] + x_offset, loc[1] + y_offset))
                x_offset += self.characters[char].get_width() + self.spacing

            elif char == '+':
                y_offset += ((self.characters[char].get_width()) * 1.5) * 2.5
                x_offset = 0

            else:
                x_offset += self.space_width + self.spacing


basic_pixel = Font(['data/png/fonts', 'basic_pixel.png'])
large_pixel = Font(['data/png/fonts', 'large_pixel.png'])


class StoryText(object):
    """docstring for StoryText"""
    def __init__(self, text, true):
        super(StoryText, self).__init__()
        self.text = text
        self.true = true

    def story_bliting(self, screen, surf, font, bliting_text, nextT, text_skip, CPR):
        if self.true:


            for x in self.text:
                clock.tick(CPR)
                bliting_text += x

                font.render(surf, bliting_text, (20, 40))
                screen.blit(pygame.transform.scale(surf,screen.get_size()),(0,0))
                pygame.display.update()
                text_skip = False

                if len(bliting_text) == len(self.text):
                    while not text_skip:

                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    sys.exit()

                                if event.key == K_SPACE:
                                    text_skip = True

                        font.render(surf, bliting_text + '+' + '+' + "                  Press Space, if you read this", (20, 40))
                        screen.blit(pygame.transform.scale(surf,screen.get_size()),(0,0))
                        pygame.display.update()

                    surf.fill((0, 0, 0))
                    self.true = False
                    nextT.true = True




'''
Many generations ago there was such a clan what has name+- Silver. He was famous for his wealth and he can controlled+all economy of the world. But his main power was not money.
'''

'''
Members of this clan were known to people all over +the world. The main goal of the clan was to find+the end of this world. So far, the end of the world+has not been found. Many generations have explored this +world,but in the last century the Silver clan was+destroyed by Union of the Great Kingdoms. The cause+of the destruction is unknown
'''

'''
You need back repotation of the Silver Clan.+And get economy of this world. It the world+infinite? Union of the Great Kingdoms? Who is my clan?
'''