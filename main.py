import pygame
from const_var import *
import chara
import sys
import ctypes
import random


class Game:
    # 窗口初始化
    # windowsInit
    def __init__(self):
        # 初始化变量
        self.per_squ = None
        self.square = None
        self.squ = None
        self.PRESS = PRESS
        self.mouse_d = None
        self.mouse_c = None
        self.mouse_a = None
        self.mouse_b = None
        self.is_dragging = False
        self.butt1 = None
        self.butt2 = None
        self.butt3 = None
        self.set_win = None
        self.came = None
        self.IS_GAME = IS_GAME
        self.END_ONE = END_ONE
        self.END_TWO = END_TWO
        self.x = 300
        self.y = 300
        self.one_x = 0
        self.one_y = 0
        if not is_in:
            chara.warn(title="Congregations! yuo aren't open the game", txt="恭喜ni未打开游戏")
            sys.exit()
        pygame.init()
        chara.sent(title="Congregations open the game successfully", txt="恭喜成功打开游戏")
        self.screen = pygame.display.set_mode(WINDOWS.size, pygame.RESIZABLE)
        pygame.display.set_caption("Zx_game_maze", "./images/logo.ico")
        ico = pygame.image.load("./images/logo.ico")
        pygame.display.set_icon(ico)
        pygame.display.gl_set_attribute(1, 2)
        # 播放背景音乐
        # play the background music
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        self.clock = pygame.time.Clock()

    # 检测窗口大小 最小不能小于默认
    # scan the windows size  the smallest not smaller the default
    def scan_win(self):
        try:
            if self.screen.get_size() is not None:
                width, height = self.screen.get_size()
                if (width, height) < WINDOWS.size:
                    self.screen = pygame.display.set_mode(WINDOWS.size, pygame.RESIZABLE)
        finally:
            pass

    def menu(self):  # 画个开始菜单 draw a start menu
        # self.screen.fill("black")

        # 修改logo的像素大小
        # change the logo pix
        img = pygame.image.load("./images/logo.png")
        re_img = pygame.transform.scale(img, (70, 50))

        width, height = self.screen.get_size()
        self.screen.blit(re_img, (width * 0.01, height * 0.01))
        # 开始就一定开始吗
        # Is the start will start
        self.butt1 = chara.Button("Start", (width * 0.3 + self.one_x, height * 0.4 + self.one_y), FONT, "blue", "pink", self.screen)
        self.butt1.draw()
        self.butt2 = chara.Button("Setting", (width * 0.5, height * 0.4), FONT, "blue", "pink", self.screen)
        self.butt2.draw()
        self.butt3 = chara.Button("About", (width * 0.7, height * 0.4), FONT, "red", "blue", self.screen)
        self.butt3.draw()
        # self.draw("Start", "blue", (100, 200))
        # self.draw("Setting", "blue", (240, 200))
        # self.draw("About", "red", (400, 200))

        # 检测按钮是否被按下
        # scan the button if it pressed
        if self.butt1.is_clicked():
            # 10次
            if self.PRESS < 100:
                # 消除上一按键
                self.PRESS += 1
                self.one_x = random.randint(0, 300)
                self.one_y = random.randint(0, 300)
            if self.PRESS == 9:
                self.PRESS += 1
                self.one_x = 0
                self.one_y = 0
                chara.show_mess("Rest or not", 'blue', self.screen, 86)

            if self.PRESS == 100:
                chara.show_mess("Ok you win", 'red', self.screen, 100)
                self.game_start()

        if self.butt2.is_clicked():
            self.setting()
        if self.butt3.is_clicked():
            if self.PRESS == 99:
                chara.warn('well', 'Hope you don\'t see the code to find it')
                # tip or coffee?
            self.__quit()

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
                        return  # 退出设置并返回菜单 quit the setting and back to the menu

            self.__update()  # 更新显示 update display

    @staticmethod
    def draw(text, color, ps, screen):
        font = pygame.font.Font(size=SIZE_TITLE, name='hehe')
        img = font.render(text, True, color)
        screen.blit(img, ps)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.IS_GAME == 1:
                    self.__quit()
                self.IS_GAME = 1
                self.game_start()
            # 检测键盘按键  detect the keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.screen.get_flags() & pygame.FULLSCREEN != 0:
                        self.screen = pygame.display.set_mode(WINDOWS.size, pygame.RESIZABLE)
                    print("Esc was pressed")

        # 按键事件 为什么这需要按着鼠标才能检测到事件？？
        # KeyEvent why it needed press the mouse can detect the event
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
        # create a camera object
        self.came = chara.Camera("blue", (self.x, self.y), self.screen)
        self.squ = chara.Square(200, "purple", (200, 300), self.screen)
        self.squ.draw()
        self.square = chara.Squ(100, (125, 135, 225), (300, 460), self.screen)

        chara.show_mess("what can I say", 'pink', self.screen, 86)
        # self.per_squ = chara.Perspective_squ(x, y, z, xc, yc, zc, xg, yg, zg, Ry, self.screen)
        # self.per_squ.perspective(xfp, yfp, zfp)

    def mouse_move(self):
        click = pygame.mouse.get_pressed()
        if click[0]:
            self.is_dragging = True
            self.mouse_a, self.mouse_b = pygame.mouse.get_pos()
        else:
            self.is_dragging = False
        if self.is_dragging:
            self.mouse_c, self.mouse_d = pygame.mouse.get_pos()
            self.x += self.mouse_c - self.mouse_a
            self.y += self.mouse_d - self.mouse_b

    def update(self):
        self.came.update()
        self.squ.update()
        self.square.update(self.came.ps[1])

    def game_start(self):
        if self.screen.get_flags() & pygame.FULLSCREEN == 0:
            self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.DOUBLEBUF)
        # 成功解决按键不反应bug
        # successfully solved the keyEvent not to act bug
        pygame.key.stop_text_input()

        # 提问阶段
        while True:
            # 一个分支 Do you get the python?
            # 敲代码路线

            # maze game
            self.event()

            # 小心一直往前走你可能真的到达那个地方
            # 迷宫路线
            self.build_scene()

            # 当两结局都达成
            if END_ONE and END_TWO:
                pass
            # 更新显示 update display
            self.update()
            self.__update()


if __name__ == '__main__':
    # 代码是写给人读的，只不过能附带在机器上运行罢了
    # Code is written to read which just can run in the machine
    game = Game()
    game.game_start_menu()

