import pygame
from const_var import *
import chara
import sys


class Game:
    # 窗口初始化
    def __init__(self):
        # 初始化变量
        self.is_dragging = False
        self.butt1 = None
        self.butt2 = None
        self.butt3 = None
        self.set_win = None
        self.came = None

        self.x = 300
        self.y = 300

        pygame.init()
        self.screen = pygame.display.set_mode(WINDOWS.size, pygame.RESIZABLE)
        pygame.display.set_caption("Zx_game_maze")
        ico = pygame.image.load("./images/logo.ico")
        pygame.display.set_icon(ico)
        pygame.display.gl_set_attribute(1, 2)
        self.clock = pygame.time.Clock()

    # 检测窗口大小 最小不能小于默认
    def scan_win(self):
        try:
            if self.screen.get_size() is not None:
                width, height = self.screen.get_size()
                if (width, height) < WINDOWS.size:
                    self.screen = pygame.display.set_mode(WINDOWS.size, pygame.RESIZABLE)
        finally:
            pass

    def menu(self):  # 画个开始菜单
        self.screen.fill("black")

        # 修改logo的像素大小
        img = pygame.image.load("./images/logo.png")
        re_img = pygame.transform.scale(img, (70, 50))

        width, height = self.screen.get_size()
        self.screen.blit(re_img, (width * 0.01, height * 0.01))
        self.butt1 = chara.Button("Start", (width * 0.3, height * 0.4), FONT, "blue", "pink", self.screen)
        self.butt1.draw()
        self.butt2 = chara.Button("Setting", (width * 0.5, height * 0.4), FONT, "blue", "pink", self.screen)
        self.butt2.draw()
        self.butt3 = chara.Button("About", (width * 0.7, height * 0.4), FONT, "red", "blue", self.screen)
        self.butt3.draw()
        # self.draw("Start", "blue", (100, 200))
        # self.draw("Setting", "blue", (240, 200))
        # self.draw("About", "red", (400, 200))

        # 检测按钮是否被按下
        if self.butt1.is_clicked():
            print("Game start!")
            self.game_start()
        if self.butt2.is_clicked():
            self.setting()
        if self.butt3.is_clicked():
            print("About")

    def setting(self):
        width, height = self.screen.get_size()
        while True:
            self.screen.fill("black")
            self.draw("Volume", "yellow", (width * 0.5, height * 0.5), self.screen)
            back_button = chara.Button("Back", (width * 0.9, height * 0.9), FONT, "red", "blue", self.screen)
            back_button.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.is_clicked():
                        return  # 退出设置并返回菜单

            self.__update()  # 更新显示

    @staticmethod
    def draw(text, color, ps, screen):
        font = pygame.font.Font(size=SIZE_TITLE, name='hehe')
        img = font.render(text, True, color)
        screen.blit(img, ps)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__quit()
            # 检测键盘按键
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.screen.get_flags() & pygame.FULLSCREEN != 0:
                        self.screen = pygame.display.set_mode(WINDOWS.size, pygame.RESIZABLE)
                    print("Esc was pressed")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 左键点击
                        self.is_dragging = True

                        print("左键")

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # 左键松开
                        self.is_dragging = False

                if event.type == pygame.MOUSEMOTION:
                    if self.is_dragging:
                        # 修改物体的位置
                        mouse_x, mouse_y = event.pos

        # 按键事件 为什么这需要按着鼠标才能检测到事件？？

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x -= 10
        if key[pygame.K_s]:
            self.y += 10
        if key[pygame.K_d]:
            self.x += 10
        if key[pygame.K_w]:
            self.y -= 10

    @staticmethod
    def __quit():
        pygame.quit()
        exit()

    def __update(self):
        pygame.display.flip()
        self.clock.tick(60)

    def game_start_menu(self):
        while True:
            self.menu()
            self.__update()
            self.event()
            self.scan_win()

    def build_scene(self):
        self.screen.fill("white")
        # pygame.draw.line(self.screen, "pink", (200, 300), (500, 500))
        # 创建个摄像头对象
        self.came = chara.Camera("blue", (self.x, self.y), self.screen)
        squ = chara.Square(200, "purple", (200, 300))
        squ.draw(self.screen)

    def game_start(self):
        if self.screen.get_flags() & pygame.FULLSCREEN == 0:
            self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.DOUBLEBUF)

        while True:
            self.event()
            self.build_scene()

            # 更新显示
            self.came.update()
            self.__update()


if __name__ == '__main__':
    game = Game()
    game.game_start_menu()
