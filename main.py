import time
import pygame
from const_var import *
import chara
import sys
import random
import os
import json
import getpass


# 果然游戏开发还是用引擎 c语言吧


class Game:
    # 窗口初始化
    # windowsInit
    def __init__(self):
        # 初始化变量
        self.bright = 100
        self.value = 100
        self.light = 0
        self.volume = 0
        self.sound = 0
        self.text = []
        self.yzx = 33
        self.xyz = 22
        self.cloud_3 = 800
        self.expand = None
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
        self.one_x = 0  # start
        self.one_y = 0
        self.open_value = 0
        self.st = None
        self.FP = FP
        self.cloud = -200
        self.cloud_1 = -250
        self.cloud_2 = -150

        # 导入json文件
        with open(js, 'r') as jso:
            self.st = json.load(jso)
        # print(self.st['language'])

        # 获取系统名称
        self.st["name"] = os.getlogin()
        with open(js, 'w') as jso:
            json.dump(self.st, jso, indent=4)

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
                    self.st["language"] = "ch"
                    with open(js, 'w') as jso:
                        json.dump(self.st, jso, indent=4)

                chara.show_choice("English", 'Chinese', 'language', event_1(), event_2())

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
        pygame.display.set_caption("Coze", "./images/logo.ico")
        ico = pygame.image.load("./images/logo.ico")
        pygame.display.set_icon(ico)
        pygame.display.gl_set_attribute(1, 2)
        # 播放背景音乐
        pygame.mixer.init()
        # play the background music
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        self.clock = pygame.time.Clock()

        # 设置事件时间
        pygame.time.set_timer(RAIN, 1000)

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
        # img = pygame.image.load("./images/logo.png")
        # re_img = pygame.transform.scale(img, (70, 50))

        # self.screen.blit(re_img, (width * 0.01, height * 0.01))
        choose = [0, 1, 2]
        choose_is = False

        # 召唤七色云彩
        self.cloud += 1
        chara.put_pic('./images/cloud.png', (self.cloud, height * 0.4), self.screen, (102, 56))
        if self.cloud == 1000:
            self.cloud = -300
        self.cloud_1 += 0.5
        chara.put_pic('./images/cloud.png', (self.cloud_1, height * 0.4 - 50), self.screen, (102, 56))
        if self.cloud_1 == 800:
            self.cloud_1 = -150
        self.cloud_2 += 2
        chara.put_pic('./images/cloud.png', (self.cloud_2, height * 0.4 - 230), self.screen, (102, 56))
        if self.cloud_2 == 2000:
            self.cloud_2 = -300

        # 获得该成就 出现乌云
        if self.st["wait_while"]:
            self.cloud_3 -= 0.5
            chara.put_pic('./images/cloud_r.png', (self.cloud_3, height * 0.4 - 120), self.screen, (102, 56))
            if self.cloud_3 == -300:
                self.cloud_3 = 800

            with open('./extend/st.json', 'rb') as jso:
                self.st = json.load(jso)
                # 成就判断
                if self.st["cloud"] == 5:
                    print("hehe achievement 1!!")
                    self.st['cloud'] = 6
                    self.st["wait_while"] = True
                    self.st['cloud'] += 1
            with open('./extend/st.json', 'w') as jso:
                json.dump(self.st, jso, indent=4)

        # 按键捕获 有点问题
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.FP += 1
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
            if event.type == RAIN:
                # 下雨事件
                pass

        if self.FP >= 3 or self.FP < 0:
            self.FP %= 3
        # 兼容键盘选择
        if choose[self.FP] == 0:
            chara.put_pic(triangle, (width * 0.3 + self.one_x - 20, height * 0.4 + self.one_y + 10 + 45, 0, 0),
                          self.screen, (22, 22))
            self.butt1 = chara.Button("Start", (width * 0.3 + self.one_x, height * 0.4 + self.one_y - 10 + 45), FONT,
                                      "blue",
                                      "pink", self.screen)
            self.butt1.draw()
        elif choose[self.FP] == 1:
            chara.put_pic(triangle, (width * 0.5 - 20, height * 0.4 + 10 + 45, 0, 0), self.screen, (22, 22))
            self.butt2 = chara.Button("Setting", (width * 0.5, height * 0.4 - 10 + 45), FONT, "blue", "pink",
                                      self.screen)
            self.butt2.draw()

        elif choose[self.FP] == 2:
            chara.put_pic(triangle, (width * 0.7 - 20, height * 0.4 + 10 + 45, 0, 0), self.screen, (22, 22))
            self.butt3 = chara.Button("About", (width * 0.7, height * 0.4 - 10 + 45), FONT, "red", "blue",
                                      self.screen)
            self.butt3.draw()

        # 提示
        chara.show_mess("Left and Right to move", 'green', self.screen, 20, (width * 0.1, height * 0.95))
        chara.show_mess("UP is confirm", 'green', self.screen, 20, (width * 0.5 + 50, height * 0.95))

        # 开始就一定开始吗
        # Is the start will start
        if choose[self.FP] != 0:
            self.butt1 = chara.Button("Start", (width * 0.3 + self.one_x, height * 0.4 + self.one_y + 45), FONT, "blue",
                                      "pink", self.screen)
            self.butt1.draw()
        if choose[self.FP] != 1:
            self.butt2 = chara.Button("Setting", (width * 0.5, height * 0.4 + 45), FONT, "blue", "pink",
                                      self.screen)
            self.butt2.draw()
        if choose[self.FP] != 2:
            self.butt3 = chara.Button("About", (width * 0.7, height * 0.4 + 45), FONT, "red", "blue",
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
                chara.show_mess("Rest or not", 'blue', self.screen, 86, (200, 200))

            if self.PRESS == 100:
                chara.show_mess("Ok you win", 'red', self.screen, 100, (200, 200))
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
                chara.put_pic("./images/triangle_t.png", (width * 0.5 - 260, height * 0.5 - 200), self.screen, (22, 22))
                chara.show_mess("Volume", "yellow", ps=(width * 0.5 - 220, height * 0.5 - 200), screen=self.screen,
                                size=22)
            if choose[self.FP] == 1:
                chara.put_pic("./images/triangle_t.png", (width * 0.5 - 260, height * 0.5 - 150), self.screen, (22, 22))
                chara.show_mess("Sound", "yellow", ps=(width * 0.5 - 220, height * 0.5 - 150), screen=self.screen,
                                size=22)
            if choose[self.FP] == 2:
                chara.put_pic("./images/triangle_t.png", (width * 0.5 - 260, height * 0.5 - 100), self.screen, (22, 22))
                chara.show_mess("Light", "yellow", ps=(width * 0.5 - 220, height * 0.5 - 100), screen=self.screen,
                                size=22)

            if choose[self.FP] != 0:
                chara.show_mess("Volume", "yellow", ps=(width * 0.5 - 230, height * 0.5 - 200), screen=self.screen,
                                size=22)

            if choose[self.FP] != 1:
                chara.show_mess("Sound", "yellow", ps=(width * 0.5 - 230, height * 0.5 - 150), screen=self.screen,
                                size=22)
            if choose[self.FP] != 2:
                chara.show_mess("Light", "yellow", ps=(width * 0.5 - 230, height * 0.5 - 100), screen=self.screen,
                                size=22)

            # 读取音量和亮度初始化
            self.value = pygame.mixer.music.get_volume()
            self.bright = chara.get_brightness()

            self.sound = chara.map_value(self.value, 0, 1, 195, 350)
            self.light = chara.map_value(self.bright, 0, 100, 195, 350)
            # 画个拉条
            pygame.draw.line(self.screen, 'white', (width * 0.5 - 100, height * 0.5 - 185),
                             (width * 0.5 + 50, height * 0.5 - 185))
            pygame.draw.circle(self.screen, 'green', (width * 0.5 + 50 - self.sound, height * 0.5 - 185), 5, 0)
            pygame.draw.line(self.screen, 'white', (width * 0.5 - 100, height * 0.5 - 135),
                             (width * 0.5 + 50, height * 0.5 - 135))
            pygame.draw.circle(self.screen, 'green', (width * 0.5 + 50 - self.volume, height * 0.5 - 135), 5, 0)
            pygame.draw.line(self.screen, 'white', (width * 0.5 - 100, height * 0.5 - 85),
                             (width * 0.5 + 50, height * 0.5 - 85))
            pygame.draw.circle(self.screen, 'green', (width * 0.5 + 50 - self.light, height * 0.5 - 85), 5, 0)

            back_button = chara.Button("Back", (width * 0.9, height * 0.9), FONT, "red", "blue", self.screen)
            back_button.draw()

            # 拖动拉条
            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()
            xxx = (195, 100)
            yyy = (350, 133)
            xxxx = (195, 150)
            yyyy = (350, 180)
            xx_xx = (195, 200)
            yy_yy = (350, 230)

            # 输出变量的值
            chara.show_mess(f"{int(self.value)}", 'orange', self.screen, 22, (width * 0.5 + 100, height * 0.5 - 195))
            chara.show_mess(f"{int(self.bright)}", 'orange', self.screen, 22, (width * 0.5 + 100, height * 0.5 - 95))

            if click[0]:
                if chara.is_within_bounds(mouse, xxx, yyy):
                    self.sound = -(pygame.mouse.get_pos()[0] - width * 0.5 + 50) + 95
                    # 调整音量
                    sound = pygame.mouse.get_pos()[0]
                    self.value = chara.map_value(sound, 195, 350, 0, 100)
                    pygame.mixer.music.set_volume(self.value)

                if chara.is_within_bounds(mouse, xxxx, yyyy):
                    self.volume = -(pygame.mouse.get_pos()[0] - width * 0.5 + 50) + 95
                if chara.is_within_bounds(mouse, xx_xx, yy_yy):
                    self.light = -(pygame.mouse.get_pos()[0] - width * 0.5 + 50) + 95
                    bright = pygame.mouse.get_pos()[0]
                    self.bright = chara.map_value(bright, 195, 350, 0, 100)
                    chara.set_brightness(self.bright)
            else:
                pass
            # 测试代码 找准位置
            # pygame.draw.circle(self.screen, 'pink', (pygame.mouse.get_pos()), 2, 0)
            # if pygame.mouse.get_pressed()[0]:
            #     print(pygame.mouse.get_pos())
            # 提示
            chara.show_mess('Up and down to move', 'yellow', self.screen, 20, (width * 0.1 - 50, height * 0.95))
            chara.show_mess('Right is confirm.', 'yellow', self.screen, 20, (width * 0.5 + 120, height * 0.95))
            chara.show_mess('Left is return', 'yellow', self.screen, 20, (width * 0.3 + 50, height * 0.95))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.FP -= 1
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
                elif event.key == pygame.K_q:
                    self.__quit()

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

        chara.show_mess("what can I say", 'pink', self.screen, 86, (200, 200))
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

    # 建立敲代码场景
    def create_scene(self):
        # 导入全景图片
        bg = pygame.image.load("./images/game.jpg")
        w, h = self.screen.get_size()
        bg_scale = pygame.transform.scale(bg, (w, h))
        self.screen.blit(bg_scale, (0, 0))

        def com_expand():
            self.expand = True

        def water():
            chara.show_mess('It\'s a cup of water', 'pink', self.screen, 60, (200, 200))

        def mouse():
            chara.show_mess('what can i say', 'pink', self.screen, 60, (200, 200))

        def knife():
            chara.show_mess('Is this a knife?', 'pink', self.screen, 60, (200, 200))

        if self.expand:
            chara.put_pic('./images/code.png', (125, 27), self.screen, (398, 243))

        # 测试代码 找准位置
        pygame.draw.circle(self.screen, 'pink', (pygame.mouse.get_pos()), 2, 0)
        if pygame.mouse.get_pressed()[0]:
            print(pygame.mouse.get_pos())

        # 点击事件
        chara.click((214, 58), (419, 171), com_expand)
        chara.click((67, 158), (105, 235), water)
        chara.click((616, 299), (644, 374), mouse)
        chara.click((22, 303), (101, 338), knife)
        chara.click((522, 320), (608, 343), knife)

    def code_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.IS_GAME == 1:
                    self.__quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.screen.get_flags() & pygame.FULLSCREEN != 0:
                        self.screen = pygame.display.set_mode((645, 481), pygame.RESIZABLE)

    def game_start(self):
        # 全屏还不是时候
        if self.screen.get_flags() & pygame.FULLSCREEN == 0:
            self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.DOUBLEBUF)
        # 成功解决按键不反应bug
        # successfully solved the keyEvent not to act bug
        pygame.key.stop_text_input()

        # 提问阶段
        if self.open_value == 8:
            chara.write("输入你的name:", 'name_in')

        def eve1():
            self.st["python"] = True
            with open(js, 'w') as jso:
                json.dump(self.st, jso, indent=4)

        if self.open_value == 8:
            chara.show_choice('会', '不会', 'Do you get the python?', eve1())

        executed = False  # 标志变量

        while True:
            # 一个分支 Do you get the python?

            # 敲代码路线

            if self.st["open_win"]:
                chara.show_mess('press the Esc to continue', 'white', self.screen, 88, (120, 250))
                if self.st['python']:
                    self.create_scene()
                    self.code_event()
                # maze game
                else:

                    # 小心一直往前走你可能真的到达那个地方
                    # 迷宫路线
                    self.build_scene()
                    self.update()

                # 当两结局都达成
                if END_ONE and END_TWO:
                    pass
                # 更新显示 update display

            # 全屏过剧情
            # 假锁屏 输入密码
            if not self.screen.get_flags() & pygame.FULLSCREEN == 0:
                # 图片适应背景
                chara.put_pic(chara.get_background(), (0, 0), self.screen, (1920, 1080))

                # 放大细节 输入后出现提示 输入的密码是。。。。
                def cli():
                    self.xyz += 20
                    self.yzx += 20
                    if self.xyz > 123:
                        self.xyz = 123
                        self.yzx = 137

                def login():
                    print('ok')
                chara.put_pic('./images/lock.png', (590, 350), self.screen, (self.xyz, self.yzx))
                if self.xyz == 123:
                    chara.input_gai(22, (530, 300, 220, 32), self.screen, self.text, login)
                    # 如果输入正确的提示 获取密码提示
                    if self.text:
                        if self.text[0] == 'hello':
                            chara.show_mess('The password is your password for your user', 'pink', self.screen, 32, (400, 500))
                chara.click((590, 350), (590 + self.xyz, 350 + self.yzx), cli)

            else:
                # huo得成就逃逸
                if self.st["run_away"]:
                    if not executed:
                        pygame.time.wait(3000)
                    self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.DOUBLEBUF)
                    executed = True
                chara.show_mess("Where you can go?", "red", self.screen, 22, (20, 20))
                self.st["run_away"] = True
                chara.warn("警告", "这里是哪？")

                with open(js, 'w') as jso:
                    json.dump(self.st, jso, indent=4)
            self.event()
            self.__update()


if __name__ == '__main__':
    # 代码是写给人读的，只不过能附带在机器上运行罢了
    # Code is written to read which just can run in the machine
    game = Game()
    game.game_start_menu()
