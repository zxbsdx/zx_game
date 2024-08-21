import pygame

is_in = False
music = "./music/fly_to_the_sky.flac"

pygame.font.init()

WINDOWS = pygame.Rect(0, 0, 730, 500)
FRAME = 60
SIZE_TITLE = 35
FONT = pygame.font.SysFont('Times New Roman', size=SIZE_TITLE)

SCENE = (1000, 1000)

# 房子坐标
x = [-20, -20, 20, 20, -20, -20, 20, 20, -20, 20]
y = [-100, -100, -100, -100, 100, 100, 100, 100, -200, -200]
z = [5, -5, -5, 5, 5, -5, -5, 5, 0, 0]

xg = []
yg = []
zg = []

xfp = 80
yfp = 50
zfp = 100

xc = 80
yc = 50
zc = 50
Ry = 45
