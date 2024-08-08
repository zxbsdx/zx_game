import pygame
from const_var import *
import chara
import sys


class Game:
    # 窗口初始化
    def __init__(self):
        self.butt1 = None
        self.butt2 = None
        self.butt3 = None
        self.set_win = None
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOWS.size, pygame.RESIZABLE)
        pygame.display.set_caption("Zx_game_maze")
        pygame.display.gl_set_attribute(1, 2)
        self.clock = pygame.time.Clock()

    # 检测窗口大小 最小不能小于默认
    def scan_win(self):
        width, height = self.screen.get_size()
        if (width, height) < WINDOWS.size:
            self.screen = pygame.display.set_mode(WINDOWS.size, pygame.RESIZABLE)

    def menu(self):  # 画个开始菜单
        self.screen.fill("black")
        img = pygame.image.load("./images/logo.png")

        width, height = self.screen.get_size()
        self.screen.blit(img, (width * 0.01, height * 0.01))
        self.butt1 = chara.Button("Start", (width * 0.3, height * 0.4), FONT, "blue", "pink", self.screen)
        self.butt1.draw(self.screen)
        self.butt2 = chara.Button("Setting", (width * 0.5, height * 0.4), FONT, "blue", "pink", self.screen)
        self.butt2.draw(self.screen)
        self.butt3 = chara.Button("About", (width * 0.7, height * 0.4), FONT, "red", "blue", self.screen)
        self.butt3.draw(self.screen)
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
            back_button.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.is_clicked():
                        return  # 退出设置并返回菜单

            self.__update()  # 更新显示

    def draw(self, text, color, ps, screen):
        font = pygame.font.Font(size=SIZE_TITLE)
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

    @staticmethod
    def __quit():
        pygame.quit()
        exit()

    def __update(self):
        pygame.display.flip()
        self.clock.tick(FRAME)

    def game_start_menu(self):
        while True:
            self.menu()
            self.__update()
            self.event()
            self.scan_win()

    def build_scene(self):
        self.screen.fill("white")
        pygame.draw.line(self.screen, "pink", (20, 20), (500, 500))

    def game_start(self):
        if self.screen.get_flags() & pygame.FULLSCREEN == 0:
            self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.DOUBLEBUF)

        while True:
            self.build_scene()
            self.event()
            self.set_win()
            self.__update()


if __name__ == '__main__':
    game = Game()
    game.game_start_menu()
