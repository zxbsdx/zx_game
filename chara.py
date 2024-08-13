import pygame


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
    def __init__(self, size, color, ps):
        super().__init__()
        self.size = size
        self.ps = ps
        self.color = color

    def draw(self, screen):
        width, height = screen.get_size()
        x = self.ps[0]
        y = self.ps[1]

        front_top_left = (x, y)
        front_top_right = (x + self.size, y)
        front_bottom_left = (x, y + self.size)
        front_bottom_right = (x + self.size, y + self.size)

        back_top_left = (x + self.size // 2, y - self.size // 2)
        back_top_right = (x + self.size + self.size // 2, y - self.size // 2)
        back_bottom_left = (x + self.size // 2, y + self.size // 2)
        back_bottom_right = (x + self.size + self.size // 2, y + self.size // 2)

        # 绘制正方体的前面
        # pygame.draw.polygon(screen, (125, 135, 225),
        #                     [front_top_left, front_top_right, front_bottom_right, front_bottom_left])

        # # 绘制正方体的背面
        # pygame.draw.polygon(screen, (125, 135, 225),
        #                     [back_top_left, back_top_right, back_bottom_right, back_bottom_left])

        # 连接上下面
        pygame.draw.line(screen, self.color, front_top_left, front_bottom_left)
        pygame.draw.line(screen, self.color, front_top_right, front_bottom_right)
        pygame.draw.line(screen, self.color, back_bottom_right, back_top_right)
        pygame.draw.line(screen, self.color, back_bottom_left, back_top_left)

        # 连接左右面
        pygame.draw.line(screen, self.color, back_bottom_left, back_bottom_right)
        pygame.draw.line(screen, self.color, back_top_right, back_top_left)
        pygame.draw.line(screen, self.color, front_top_left, front_top_right)
        pygame.draw.line(screen, self.color, front_bottom_left, front_bottom_right)

        # 连接前后面
        pygame.draw.line(screen, self.color, front_top_left, back_top_left)
        pygame.draw.line(screen, self.color, front_top_right, back_top_right)
        pygame.draw.line(screen, self.color, front_bottom_left, back_bottom_left)
        pygame.draw.line(screen, self.color, front_bottom_right, back_bottom_right)


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
