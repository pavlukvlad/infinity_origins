import pygame, os, sys, random, time, json
from pygame.locals import *
from data.py.AnimationLoader.f import *
from data.py.Text.f import *
from data.py.Physics.f import *
from data.py.Core.f import *
from data.py.Entity.f import *


d1 = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '1.png')))
d2 = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '2.png')))
d3 = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '3.png')))
gb1 = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '0.png')))
gb2 = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '5.png')))
gb3 = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '6.png')))
gb4 = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '7.png')))
s1 = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '4.png')))
g1 = None
g2 = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass_d', '1.png')))
g3 = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass_d', '2.png')))
rf = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass_d', '3.png')))
bf = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass_d', '4.png')))
tr1 = [pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/1', '0.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/1', '1.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/1', '2.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/1', '3.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/1', '4.png'))),]
tr2 = [pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/2', '0.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/2', '1.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/2', '2.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/2', '3.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/2', '4.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/2', '5.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/2', '6.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/2', '7.png'))),pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/2', '8.png'))),]
tr3 = [pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/3', '0.png'))), pygame.image.load(resource_path(os.path.join('data/png/blocks/tree/3', '1.png')))]
io = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '8.png')))
go = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '10.png')))
co = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '9.png')))
copo = pygame.image.load(resource_path(os.path.join('data/png/blocks/grass', '11.png')))
