import pygame
import numpy as np
import math


class Camera(pygame.sprite.Sprite):
    def __init__(self, color, ps, screen, speed=10):
        super().__init__()
        self.ps = ps
        self.color = color
        self.screen = screen
        self.speed = speed

    def update(self, *args, **kwargs):
        super().update()
        pygame.draw.circle(self.screen, self.color, self.ps, 20, 0)


# 创建一个正方体
class Square(pygame.sprite.Sprite):
    def __init__(self, size, color, ps, screen):
        super().__init__()
        self.back_bottom_right = None
        self.back_bottom_left = None
        self.back_top_right = None
        self.back_top_left = None
        self.front_bottom_right = None
        self.front_bottom_left = None
        self.front_top_right = None
        self.front_top_left = None
        self.mouse_d = None
        self.mouse_c = None
        self.ob = ps
        self.x = self.ob[0]
        self.y = self.ob[1]
        self.width, self.height = screen.get_size()
        self.screen = screen
        self.is_dragging = False
        self.mouse_a = 0
        self.mouse_b = 0
        self.size = size
        self.ps = ps
        self.color = color

    def draw(self):
        self.front_top_left = (self.x, self.y)
        self.front_top_right = (self.x + self.size, self.y)
        self.front_bottom_left = (self.x, self.y + self.size)
        self.front_bottom_right = (self.x + self.size, self.y + self.size)

        self.back_top_left = (self.x + self.size // 2, self.y - self.size // 2)
        self.back_top_right = (self.x + self.size + self.size // 2, self.y - self.size // 2)
        self.back_bottom_left = (self.x + self.size // 2, self.y + self.size // 2)
        self.back_bottom_right = (self.x + self.size + self.size // 2, self.y + self.size // 2)

        # 绘制正方体的前面
        # pygame.draw.polygon(screen, (125, 135, 225),
        #                     [front_top_left, front_top_right, front_bottom_right, front_bottom_left])

        # # 绘制正方体的背面
        # pygame.draw.polygon(screen, (125, 135, 225),
        #                     [back_top_left, back_top_right, back_bottom_right, back_bottom_left])
        # 连接上下面
        pygame.draw.line(self.screen, self.color, self.front_top_left, self.front_bottom_left)
        pygame.draw.line(self.screen, self.color, self.front_top_right, self.front_bottom_right)
        pygame.draw.line(self.screen, self.color, self.back_bottom_right, self.back_top_right)
        pygame.draw.line(self.screen, self.color, self.back_bottom_left, self.back_top_left)

        # 连接左右面
        pygame.draw.line(self.screen, self.color, self.back_bottom_left, self.back_bottom_right)
        pygame.draw.line(self.screen, self.color, self.back_top_right, self.back_top_left)
        pygame.draw.line(self.screen, self.color, self.front_top_left, self.front_top_right)
        pygame.draw.line(self.screen, self.color, self.front_bottom_left, self.front_bottom_right)

        # 连接前后面
        pygame.draw.line(self.screen, self.color, self.front_top_left, self.back_top_left)
        pygame.draw.line(self.screen, self.color, self.front_top_right, self.back_top_right)
        pygame.draw.line(self.screen, self.color, self.front_bottom_left, self.back_bottom_left)
        pygame.draw.line(self.screen, self.color, self.front_bottom_right, self.back_bottom_right)

    def update(self, *args, **kwargs):
        super().update()
        click = pygame.mouse.get_pressed()
        if click[0]:  # Left mouse button pressed
            self.x = 300
            self.y = 460
        self.draw()

            
class Button:
    def __init__(self, text, pos, font, color, hover_color, screen):
        self.text = text
        self.pos = pos
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.screen = screen
        self.rect = self.font.render(self.text, True, self.color).get_rect(center=pos)

    def draw(self):
        # 检测鼠标位置
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.render(self.hover_color)  # 鼠标悬停时的颜色
        else:
            self.render(self.color)  # 正常颜色

    def render(self, color):
        # 绘制按钮文本
        text_surface = self.font.render(self.text, True, color)
        self.screen.blit(text_surface, self.rect.topleft)

    def is_clicked(self):
        # 检查按钮是否被点击
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        return self.rect.collidepoint(mouse_pos) and click[0]  # 检测左键点击


class Squ(pygame.sprite.Sprite):
    def __init__(self, size, color, ps, screen):
        super().__init__()
        self.x = ps[0]
        self.y = ps[1]
        self.width, self.height = screen.get_size()
        self.screen = screen
        self.is_dragging = False
        self.size = size
        self.color = color

    def draw(self, camera_height):
        # 计算正方体前视图的缩放比例
        scale = 1 - (camera_height / 500)  # 500可以调整以改变深度效果
        scaled_size = self.size * scale

        # 计算顶点
        front_bottom_left = (self.x, self.y + scaled_size)
        front_bottom_right = (self.x + scaled_size, self.y + scaled_size)
        front_top_left = (self.x, self.y)
        front_top_right = (self.x + scaled_size, self.y)

        back_bottom_left = (self.x + scaled_size / 2, self.y + scaled_size / 2)
        back_bottom_right = (self.x + scaled_size + scaled_size / 2, self.y + scaled_size / 2)
        back_top_left = (self.x + scaled_size / 2, self.y - scaled_size / 2)
        back_top_right = (self.x + scaled_size + scaled_size / 2, self.y - scaled_size / 2)

        # 绘制正方体的各个边
        pygame.draw.line(self.screen, self.color, front_top_left, front_bottom_left)
        pygame.draw.line(self.screen, self.color, front_top_right, front_bottom_right)
        pygame.draw.line(self.screen, self.color, back_bottom_right, back_top_right)
        pygame.draw.line(self.screen, self.color, back_bottom_left, back_top_left)
        pygame.draw.line(self.screen, self.color, back_bottom_left, back_bottom_right)
        pygame.draw.line(self.screen, self.color, back_top_right, back_top_left)
        pygame.draw.line(self.screen, self.color, front_top_left, front_top_right)
        pygame.draw.line(self.screen, self.color, front_bottom_left, front_bottom_right)
        pygame.draw.line(self.screen, self.color, front_top_left, back_top_left)
        pygame.draw.line(self.screen, self.color, front_top_right, back_top_right)
        pygame.draw.line(self.screen, self.color, front_bottom_left, back_bottom_left)
        pygame.draw.line(self.screen, self.color, front_bottom_right, back_bottom_right)

    def update(self, camera_height):
        super().update()
        self.draw(camera_height)


# 创建一个透视变换的正方体对象
class Perspective_squ(pygame.sprite.Sprite):
    def __init__(self, x, y, z, xg, yg, zg):
        self.x = x
        self.y = y
        self.z = z
        self.xg = xg
        self.yg = yg
        self.zg = zg

    def roty(self, xc, yc, zc, Ry):
        a = [self.x, self.y, self.z]
        b = [math.cos(Ry), 0, math.sin(Ry)]
        xpp = np.inner(a, b)
        b = [0, 1, 0]
        ypp = np.inner(a, b)
        b = [-math.sin(Ry), 0, math.cos(Ry)]
        zpp = np.inner(a, b)
        [xg, yg, zg] = [xpp + xc, ypp + yc, zpp + zc]
        return [xg, yg, zg]

    def squrey(self, xc, yc, zc, Ry):
        for i in range(len(self.x)):
            [self.xg[i], self.yg[i], self.zg[i]] = self.roty(xc, yc, zc, self.x[i], self.y[i], self.z[i], Ry)

    def perspective(self, xfp, yfp, zfp):
        for i in range(len(self.x)):
            a = self.xg[i] - xfp
            b = self.yg[i] - yfp
            c = self.zg[i] + abs(zfp)
            q = np.sqrt(a * a + b * b + c * c)
            ux = a / q
            uy = b / q
            uz = c / q
            qh = q * abs(zfp) / (self.zg[i] + abs(zfp))
            xh = ux * qh + xfp
            yh = uy * qh + yfp
            zh = 0
            self.xg[i] = xh
            self.yg[i] = yh
            self.zg[i] = zh

    def draw(self):
        pass

    def update(self, *args, **kwargs):
        super().update()
