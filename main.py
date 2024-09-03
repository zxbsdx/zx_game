import pygame
from const_var import *
import chara
import sys
import ctypes
import random
import os
import json


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
        self.open_value = 0
        self.st = None
        self.FP = FP

        # 导入json文件
        with open(js, 'r') as jso:
            self.st = json.load(jso)
        # print(self.st['language'])

        with open(out_var, 'r') as file:
            for line in file:
                line = line.strip()  # 去掉行首尾的空格
                if line.startswith("OPEN ="):
                    # 分割字符串以获取变量值
                    key_value = line.split('=')  # 切分为 ['OPEN ', ' 0']
                    if len(key_value) == 2:  # 确保有两个部分
                        self.open_value = int(key_value[1].strip())  # 将值转换为整数
                        break  # 找到后可以退出循环
        if self.open_value < 7:
            if self.open_value == 0:
                # 出现一次写入json
                def event_1():
                    self.st["language"] = "eh"
                    with open(js, 'w') as jso:
                        json.dump(self.st, jso, indent=4)  # indent=4 是为了使 JSON 文件更加可读

                def event_2():
                    self.st["language"] = "eh"
                    with open(js, 'w') as jso:
                        json.dump(self.st, jso, indent=4)  # indent=4 是为了使 JSON 文件更加可读

                chara.show_choice("eh", 'ch', 'language', event_1(), event_2())

                chara.warn(title="Superbia", txt="恭喜ni未打开游戏")
            if self.open_value == 1:
                chara.warn(title="Envidia", txt="ni不会在想这是什么鬼游戏？")
            if self.open_value == 2:
                chara.warn(title="Ira", txt="有没有可能游戏在ni看到的那一刻就已经开始了呢？")
            if self.open_value == 3:
                chara.warn(title="Acedia", txt="ni有没有觉得有点意思起来了呢")
            if self.open_value == 4:
                chara.warn(title="Avaritia", txt="恭喜ni未打开游戏")
            if self.open_value == 5:
                chara.warn(title="Gula", txt="emmmmm 加油 ni马上就到抵达了")
            if self.open_value == 6:
                chara.warn(title="Luxuria", txt="真的是最后一次了")

            self.open_value += 1
            with open(out_var, 'w') as file:
                file.write(f"OPEN = {self.open_value}\n")  # 写入格式化字符串
            sys.exit()
        pygame.init()
        if self.st['is_in'] is False:
            chara.sent(title="Congregations open the game successfully", txt="恭喜成功打开游戏")
            # 修改数据
            self.st['is_in'] = True

            # 将更新后的数据写回 JSON 文件
            with open(js, 'w') as jso:
                json.dump(self.st, jso, indent=4)  # indent=4 是为了使 JSON 文件更加可读

        self.open_value += 1
        with open(out_var, 'w') as file:
            file.write(f"OPEN = {self.open_value}\n")

        self.screen = pygame.display.set_mode(WINDOWS.size, pygame.RESIZABLE)
        pygame.display.set_caption("Zx_game_maze?", "./images/logo.ico")
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
        pa = pygame.image.load(page)
        re_img = pygame.transform.scale(pa, (WINDOWS.width, WINDOWS.height))
        width, height = self.screen.get_size()
        self.screen.blit(re_img, (width * 0.0001, height * 0.0001))
        # 修改logo的像素大小
        # change the logo pix
        img = pygame.image.load("./images/logo.png")
        re_img = pygame.transform.scale(img, (70, 50))

        width, height = self.screen.get_size()
        self.screen.blit(re_img, (width * 0.01, height * 0.01))
        choose = [0, 1, 2]
        choose_is = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.FP += 1
                    print("right")
                if event.key == pygame.K_LEFT:
                    self.FP -= 1
                if event.key == pygame.K_UP:
                    # up为确认
                    if choose[self.FP] == 0:
                        choose_is = True
                    if choose[self.FP] == 1:
                        self.setting()
                    if choose[self.FP] == 2:
                        self.__quit()
                if event.key == pygame.K_DOWN:
                    pass
        if self.FP >= 3 or self.FP < 0:
            self.FP %= 3
        # 兼容键盘选择
        if choose[self.FP] == 0:
            chara.put_pic(triangle, (width * 0.3 + self.one_x - 20, height * 0.4 + self.one_y + 10, 0, 0), self.screen)
            self.butt1 = chara.Button("Start", (width * 0.3 + self.one_x, height * 0.4 + self.one_y - 10), FONT, "blue",
                                      "pink", self.screen)
            self.butt1.draw()
        elif choose[self.FP] == 1:
            chara.put_pic(triangle, (width * 0.5 - 20, height * 0.4 + 10, 0, 0), self.screen)
            self.butt2 = chara.Button("Setting", (width * 0.5, height * 0.4 - 10), FONT, "blue", "pink",
                                      self.screen)
            self.butt2.draw()

        elif choose[self.FP] == 2:
            chara.put_pic(triangle, (width * 0.7 - 20, height * 0.4 + 10, 0, 0), self.screen)
            self.butt3 = chara.Button("About", (width * 0.7, height * 0.4 - 10), FONT, "red", "blue",
                                      self.screen)
            self.butt3.draw()

        # 开始就一定开始吗
        # Is the start will start
        if choose[self.FP] != 0:
            self.butt1 = chara.Button("Start", (width * 0.3 + self.one_x, height * 0.4 + self.one_y), FONT, "blue",
                                      "pink", self.screen)
            self.butt1.draw()
        if choose[self.FP] != 1:
            self.butt2 = chara.Button("Setting", (width * 0.5, height * 0.4), FONT, "blue", "pink",
                                      self.screen)
            self.butt2.draw()
        if choose[self.FP] != 2:
            self.butt3 = chara.Button("About", (width * 0.7, height * 0.4), FONT, "red", "blue",
                                      self.screen)
            self.butt3.draw()
        # self.draw("Start", "blue", (100, 200))
        # self.draw("Setting", "blue", (240, 200))
        # self.draw("About", "red", (400, 200))

        # 检测按钮是否被按下
        # scan the button if it pressed
        if self.butt1.is_clicked() or choose_is:
            # 10次
            if self.PRESS < 100:
                # 消除上一按键?
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
        self.FP = 0
        while True:
            self.screen.fill("black")
            choose = [0, 1, 2]
            if choose[self.FP] == 0:
                chara.put_pic("./images/triangle_t.png", (width * 0.5 - 260, height * 0.5 - 210), self.screen)
                self.draw("Volume", "yellow", (width * 0.5 - 230, height * 0.5 - 200), self.screen)
            if choose[self.FP] == 1:
                chara.put_pic("./images/triangle_t.png", (width * 0.5 - 260, height * 0.5 - 150), self.screen)
                self.draw("Sound", "yellow", (width * 0.5 - 230, height * 0.5 - 150), self.screen)
            if choose[self.FP] == 2:
                chara.put_pic("./images/triangle_t.png", (width * 0.5 - 260, height * 0.5 - 100), self.screen)
                self.draw("Light", "yellow", (width * 0.5 - 230, height * 0.5 - 100), self.screen)

            if choose[self.FP] != 0:
                self.draw("Volume", "yellow", (width * 0.5 - 250, height * 0.5 - 200), self.screen)

            if choose[self.FP] != 1:
                self.draw("Sound", "yellow", (width * 0.5 - 250, height * 0.5 - 150), self.screen)
            if choose[self.FP] != 2:
                self.draw("Light", "yellow", (width * 0.5 - 250, height * 0.5 - 100), self.screen)

            # 画个拉条
            pygame.draw.line(self.screen, 'white', (width * 0.5 - 100, height * 0.5 - 185),
                             (width * 0.5 + 50, height * 0.5 - 185))
            pygame.draw.circle(self.screen, 'green', (width * 0.5 - 100, height * 0.5 - 185), 5, 0)
            pygame.draw.line(self.screen, 'white', (width * 0.5 - 100, height * 0.5 - 150),
                             (width * 0.5 + 50, height * 0.5 - 150))
            pygame.draw.circle(self.screen, 'green', (width * 0.5 - 100, height * 0.5 - 150), 5, 0)
            pygame.draw.line(self.screen, 'white', (width * 0.5 - 100, height * 0.5 - 100),
                             (width * 0.5 + 50, height * 0.5 - 100))
            pygame.draw.circle(self.screen, 'green', (width * 0.5 - 100, height * 0.5 - 100), 5, 0)

            back_button = chara.Button("Back", (width * 0.9, height * 0.9), FONT, "red", "blue", self.screen)
            back_button.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.FP -= 1
                        print("up")
                    if event.key == pygame.K_DOWN:
                        self.FP += 1
                    if event.key == pygame.K_LEFT:
                        return
                    if event.key == pygame.K_RIGHT:
                        pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.is_clicked():
                        self.screen.fill("black")
                        return  # 退出设置并返回菜单 quit the setting and back to the menu
            if self.FP >= 3 or self.FP < 0:
                self.FP %= 3
            self.__update()  # 更新显示 update display

    @staticmethod
    def draw(text, color, ps, screen):
        font = pygame.font.Font(size=SIZE_TITLE)
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
