import pygame


class Camera(pygame.sprite.Sprite):
    def __init__(self, speed, ps):
        self.speed = speed
        self.ps = ps


# 创建一个正方体
class Square(pygame.sprite.Sprite):
    def __init__(self, size, color, ps):
        self.size = size
        self.ps = ps
        self.color = color

    def draw(self, screen):
        pygame.draw.line(screen, self.color)


class Button:
    def __init__(self, text, pos, font, color, hover_color, screen):
        self.text = text
        self.pos = pos
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.rect = self.font.render(self.text, True, self.color).get_rect(center=pos)
        self.screen = screen

    def draw(self, screen):
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
