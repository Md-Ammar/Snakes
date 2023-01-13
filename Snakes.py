import pygame
import random
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE

import windows as wd
import accessories

pygame.init()
w, h = 1000, 700
win = pygame.display.set_mode((w, h), HWSURFACE | DOUBLEBUF | RESIZABLE)
# pygame.display.toggle_fullscreen
pygame.display.set_caption("The Snake-a game by ammar")

clock = pygame.time.Clock()
fps = 20

left = up = down = False
right = True
run = True
pause = False
crash = False

food_count = 0
score = 0
init_length = 15

parts = []  # body

wd.menu(score)

# def paused():
#     global pause, clock
#     n = True
#     while n:
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:  # resume
#                     n = False
#                     pause = False
#         clock.tick(5)


def restart():
    global left, right, up, down, pause, parts, crash, food_count, score
    Snake.x = w // 2
    Snake.y = h // 2
    Snake.len = init_length
    up = down = left = False
    right = True
    pause = False
    crash = False
    score = 0
    parts = []
    if Snake.fx > w or Snake.fy > h: food_count = 0  # gen_Food if not in screen


class snake:
    def __init__(self, x, y, Len, width):
        self.x = x
        self.y = y
        self.len = Len
        self.vel = width//2
        self.wid = width
        self.fx = 0
        self.fy = 0
        self.fclr = (0, 0, 0)
        self.multicolorlist = list(accessories.random_color() for _ in range(self.len))

    def draw(self):
        global pause, crash
        if not crash:
            pass
        self.move()
        self.body()

    def move(self):
        global up, down, left, right, pause, crash, h
        if True:
            if (self.x >= 0) and (self.x <= w) and (self.y >= 50) and (self.y <= h):
                if right:
                    self.x += self.vel
                if left:
                    self.x -= self.vel
                if up:
                    self.y -= self.vel
                if down:
                    self.y += self.vel
            else:
                crash = True

    def body(self):  # body of snake
        global parts, food_count, fx, fy, score, checkered, crash, transition

        if len(parts) <= self.len:
            if not crash:
                parts.append((self.x, self.y))

            self.draw_part()
            if not crash:
                self.self_crash(parts)
                self.check_food(parts)

                pygame.display.update()
        else:
            if not crash:
                parts.pop(0)

    def draw_part(self):
        for p in parts:
            if p == parts[len(parts) - 1]:  # head
                color = (200, 0, 200)
                if right:
                    head = (p[0], p[1] + 5)
                if left:
                    head = (p[0] + 5 + 5, p[1] + 5)
                if up:
                    head = (p[0] + 5, p[1] + 5 + 5)
                if down:
                    head = (p[0] + 5, p[1])
                pygame.draw.circle(win, wd.Pcolor, head, 5)
                e_color = random.randrange(0, 255, 254)
                pygame.draw.circle(win, (e_color, e_color, e_color), head, 2)  # eye
            else:  # trail
                if wd.checkered:
                    if parts.index(p) % 2 == 0:
                        color = wd.Pcolor
                    elif parts.index(p) % 2 == 1:
                        color = wd.Scolor
                elif not wd.checkered:
                    color = wd.Pcolor
                if wd.transition:
                    color = accessories.changing_colors()
                pygame.draw.rect(win, color, (p, (self.wid, self.wid)))

                if wd.multicolor:
                    pygame.draw.rect(win, self.multicolorlist[parts.index(p)], (p, (self.wid, self.wid)))

                if wd.border:
                    pygame.draw.rect(win, (0, 0, 0), (p, (self.wid, self.wid)), 1)
            if wd.Design:
                if wd.design[0]:
                    pygame.draw.line(win, (0, 0, 0), (p[0] + 4, p[1]), (p[0] + 4, p[1] + 10), 2)
                    pygame.draw.line(win, (0, 0, 0), (p[0], p[1] + 4), (p[0] + 10, p[1] + 4), 2)
                    pygame.draw.line(win, (0, 0, 0), p, (p[0] + 10, p[1] + 10), 2)
                    pygame.draw.line(win, (0, 0, 0), (p[0] + 10, p[1]), (p[0], p[1] + 10), 2)
                elif wd.design[1]:
                    pygame.draw.circle(win, (0, 0, 0), (p[0] + 5, p[1] + 5), random.randrange(0, 5))
                elif wd.design[2]:
                    d = random.randrange(1, 10)
                    pygame.draw.circle(win, (255, 255, 255), (p[0] + 5, p[1] + 5), d, 1)
                elif wd.design[3]:
                    d = random.randrange(1, 10)
                    pygame.draw.rect(win, (200, 200, 200), (p[0] + 5 - d, p[1] + 5 - d, d * 2, d * 2), 1)
                elif wd.design[4]:
                    pygame.draw.line(win, (0, 0, 0),
                                     (random.randrange(p[0], p[0] + self.wid), random.randrange(p[1], p[1] + self.wid)),
                                     (random.randrange(p[0], p[0] + self.wid), random.randrange(p[1], p[1] + self.wid)),
                                     2)

    def self_crash(self, part):
        global crash
        head = part[len(part) - 1]
        second = part[len(part) - 2]

        for p in part:
            if part.index(p) != (len(part) - 1) and pygame.Rect(head, (self.wid, self.wid)).collidepoint(
                    p) and not crash and p != second:
                if p in part:
                    crash = True; break
                    d = part.index(p)
                    # print("cut off body at "+str(d))
                    if Snake.len - d >= 6:  # cut off length
                        Snake.len -= d
                    elif Snake.len - d <= 6:
                        Snake.len = 6
                        print("MINIMUM LENGTH")

    def gen_food(self):
        self.fx = random.randrange(0 + 10, w - 20, self.wid)
        self.fy = random.randrange(50 + 10, h - 20, self.wid)
        self.fclr = (random.randrange(0, 255),
                                     random.randrange(0, 255),
                                     random.randrange(0, 255))

    def draw_food(self):
        # for i in range(7, 1, -1):
        pygame.draw.circle(win, self.fclr, (self.fx, self.fy), self.vel)

    def check_food(self, part):# eaten
        global food_count, fx, fy, score
        head = part[len(part) - 1]

        if food_count == 0:
            self.gen_food()
            food_count += 1
        self.draw_food()

        if pygame.Rect(head, (self.wid, self.wid)).colliderect(pygame.Rect(self.fx-5, self.fy-5, 10, 10)):  # eat
            food_count -= 1
            score += 1
            Snake.len += 1
            Snake.multicolorlist.append(accessories.random_color())

def redrawgamewindow():
    global pause, w, h, run

    win.fill((0, 0, 0))

    if not wd.transition:
        pygame.draw.rect(win, accessories.changing_colors(), (0, 50, w, h - 50), 1)
    else:
        pygame.draw.rect(win, (0, 255, 0), (0, 50, w, h - 50), 1)
        pygame.draw.rect(win, (0, 255, 0), (0 + 3, 50 + 3, w - 6, h - 50 - 6), 1)

    menu = accessories.buttons("MENU", 3, 3, True)
    customize = accessories.buttons("CUSTOMIZE", w - 130, 3, True)
    Restart = accessories.buttons("RESTART", w - 230, 3, True)

    accessories.msg("Food eaten:" + str(score), (255, 255, 255), w // 2 - 20, 0)
    accessories.msg("Length:" + str(Snake.len), (255, 255, 255), w // 2 - 15, 20)

    if not pause:
        Snake.draw()
    elif pause:
        accessories.msg_heading("PAUSED", (0, 255, 0), h // 2)
        pygame.display.update()
    if crash:
        accessories.msg_heading("YOU CRASHED!", (200, 0, 0), h // 2)
        accessories.msg('SCORE:' + str(score), (200, 200, 0), w // 2 - 50, h // 2 + 30)
        accessories.msg('LENGTH:' + str(Snake.len), (200, 200, 0), w // 2 - 50, h // 2 + 50)
        pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            pygame.display.quit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
            w = screen.get_width()
            h = screen.get_height()
            restart()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if pygame.Rect(menu).collidepoint(x, y):
                accessories.transition(False)
                wd.menu(score)
            if pygame.Rect(customize).collidepoint(x, y):
                wd.customize()
            if pygame.Rect(Restart).collidepoint(x, y):
                restart()


Snake = snake(w // 2, h // 2, init_length, 10)

while run:
    clock.tick(fps)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False

    if keys[pygame.K_m]:
        accessories.transition(False)
        wd.menu(score)

    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        Snake.vel = 7
        fps = 60
    else:
        Snake.vel = 5
        fps = 25

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if not left:
            up = down = left = False
            right = True
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if not right:
            up = down = right = False
            left = True
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        if not down:
            right = down = left = False
            up = True
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if not up:
            up = right = left = False
            down = True

    if keys[pygame.K_SPACE] and not crash:
        if pause:
            pause = False
        elif not pause:
            pause = True

    if keys[pygame.K_r]: restart()

    redrawgamewindow()
pygame.quit()
