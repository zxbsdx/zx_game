import pygame
import numpy as np
import math
from tkinter.messagebox import *
import tkinter
from PIL import ImageTk, Image


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
    # x, y, z是物体实际坐标， xg， yg， zg是地面坐标
    def __init__(self, x, y, z, xc, yc, zc, xg, yg, zg, Ry, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.xc = xc
        self.yc = yc
        self.zc = zc
        self.xg = xg
        self.yg = yg
        self.zg = zg
        self.Ry = Ry
        self.screen = screen

        for i in np.arange(len(x)):
            xg.append(x[i] + self.xc)
            yg.append(x[i] + self.yc)
            zg.append(x[i] + self.zc)

    # 按y轴旋转，实现3d效果
    def roty(self, xc, yc, zc):
        a = [self.x, self.y, self.z]
        b = [math.cos(self.Ry), 0, math.sin(self.Ry)]
        xpp = np.inner(a, b)
        b = [0, 1, 0]
        ypp = np.inner(a, b)
        b = [-math.sin(self.Ry), 0, math.cos(self.Ry)]
        zpp = np.inner(a, b)
        [xg, yg, zg] = [xpp + xc, ypp + yc, zpp + zc]
        return [xg, yg, zg]

    def draw(self):
        for i in np.arange(len(self.x)):
            # 使用 pygame.draw.rect
            # 每个矩形的矩形对象
            start_pos = (self.xg[i], self.yg[i])
            if i + i > 9:
                break
            end_pos = (self.xg[i + 1], self.yg[i + 1])  # 如果想要绘制到下一个点

            # 绘制矩形到屏幕
            # pygame.draw.rect(self.screen, 'green', rect)
            pygame.draw.line(self.screen, 'green', start_pos, end_pos)

            # 实现摄像头与物体远近的变化， zfg表示纵向深度的变化
    def perspective(self, xfp, yfp, zfp):
        for i in range(len(self.x)):
            self.plothousey(self.xc, self.yc, self.zc)
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
            self.draw()

    def plothousey(self, xc, yc, zc):
        for i in range(len(self.x)):
            [self.xg[i], self.yg[i], self.zg[i]] = self.roty(xc, yc, zc)

    def update(self, *args, **kwargs):
        super().update()


# 弹出提示
def sent(title, txt):
    print(showinfo(title=title, message=txt))


def warn(title, txt):
    print(showwarning(title=title, message=txt))


def show_mess(txt, color, screen, size):
    font = pygame.font.Font(None, size)
    text = font.render(txt, True, color)
    screen.blit(text, (200, 200))


# 特色选择框
def show_choice(butt1, butt2, txt, event1=None, event2=None):
    tk = tkinter.Tk()
    # 获取屏幕大小 弹出框居中
    x = 280
    y = 220
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.geometry("%dx%d+%d+%d" % (x, y, (width-x)/2, (height-y)/2))
    tk.config(bg="white")
    # tk.attributes('-alpha', 0.5)
    # 设置窗口置顶显示
    tk.attributes('-topmost', 1)
    # 设置无状态栏
    tk.overrideredirect(True)

    # 让背景透明
    tk.wm_attributes('-transparentcolor', 'white')  # 设置透明颜色

    def close_window():
        tk.destroy()

    if event1 is None:
        event1 = close_window

    if event2 is None:
        event2 = close_window

    # 添加背景
    image = Image.open("./images/butt_ch.png").convert("RGBA")
    photo = ImageTk.PhotoImage(image=image)
    images = tkinter.Label(tk, image=photo, bg='white')  # 使用 bg='pink' 使背景透明
    images.image = photo  # 保持对图像的引用
    images.place(y=-90, x=0)
    # 添加文字
    ques = tkinter.Label(tk, text=txt)
    ques.config(bg='red', fg='brown', width=10, height=1)
    ques.place(y=5, x=10)

    butt_1 = tkinter.Button(tk, text=butt1)
    butt_1.config(bg="brown", fg="red", width=7, height=1)
    butt_1.size()
    butt_1.place(y=140, x=50)

    butt_2 = tkinter.Button(tk, text=butt2)
    butt_2.config(bg="pink", fg="red", width=7, height=1)
    butt_2.place(y=140, x=180)

    # 绑定事件
    butt_1.bind("<Button-1>", lambda event: event1())
    butt_2.bind("<Button-1>", lambda event: event2())

    tk.mainloop()


def put_pic(path, ps, screen):
    # 放一张图片
    img = pygame.image.load(path)
    screen.blit(img, ps)


