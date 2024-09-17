import pygame
import ctypes
import os
import json

# 是开始亦或是结束
# Congratulations Is it a start or end

RAIN = pygame.USEREVENT

music = "./music/fly_to_the_sky.flac"
IS_GAME = 0
END_ONE = False
END_TWO = False
pygame.font.init()

PRESS = 0

WINDOWS = pygame.Rect(0, 0, 600, 600)
FRAME = 60
SIZE_TITLE = 35
FONT = pygame.font.Font("./font/手写.ttf", 30)
FP = 0

SCENE = (1000, 1000)

GAME_STATE = {
    'level': 0
}

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


# 加载外部文件
out_var = './extend/out_var'
js = './extend/st.json'

# 加载dll
language_dll = ctypes.CDLL('./extend/language.dll')

# picture
triangle = "./images/triangle.png"
page = './images/page.jpg'


