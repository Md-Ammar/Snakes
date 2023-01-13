import pygame
import random
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE

pygame.init()
w, h = 700, 700
win = pygame.display.set_mode((w, h), HWSURFACE | DOUBLEBUF | RESIZABLE)

clock = pygame.time.Clock()

font1 = pygame.font.SysFont('old english text', 45)
font2 = pygame.font.SysFont('chiller', 25, True)

fire_var = 0
Fire = False
i = 0


def textbox(c, wid):
    global font2
    font2 = pygame.font.SysFont('Chiller', 25, True)
    s = ""
    n = True
    while n:
        pygame.draw.rect(win, (255, 255, 255), (c[0], c[1], wid, 30))
        pygame.draw.rect(win, (0, 200, 0), (c[0], c[1], wid, 30), 2)

        if s == "":
            win.blit(font2.render("ENTER TEXT HERE", 1, (100, 100, 100)), c)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(win, (200, 0, 0), (c[0], c[1], wid, 30), 2)
                pygame.display.update()

            if event.type == pygame.KEYDOWN:
                l = str(pygame.key.name(event.key))
                if l == "backspace": s = s[0:len(s) - 1]
                if l == "space": s += " "
                if l == "return":
                    if s != "":
                        return s
                    else:
                        pygame.draw.rect(win, (200, 0, 0), (c[0], c[1], wid, 30), 2)
                if len(l) == 1:
                    s += l
                    s = s.upper()
        txt = font2.render(s, 1, (0, 0, 0))
        win.blit(txt, c)

        if wid < txt.get_width():
            wid = txt.get_width()
        pygame.display.update()
        clock.tick(10)


def msg_heading(m, color, y):  # large text(mid)
    global font1, w
    text = font1.render(m, 1, color)
    win.blit(text, ((w - text.get_width()) // 2, y - text.get_height() // 2))


def msg(m, color, x, y):  # small text
    global font2
    text = font2.render(m, 1, color)
    win.blit(text, (x, y))


def buttons(msg, x, y, state):  # button
    global font2
    text = font2.render(msg, 1, (0, 255, 0))
    wid_button = text.get_width()
    ht_button = text.get_height()

    pygame.draw.rect(win, (0, 0, 0), (x, y, wid_button, ht_button), 0)
    pygame.draw.rect(win, (0, 255, 0) if state == True else (255, 0, 0), (x, y, wid_button, ht_button), 3)

    win.blit(text, (x, y))
    dim = pygame.Rect(x, y, wid_button, ht_button)
    return dim


color = ()


def changing_colors():
    global i, color
    if i <= 255:
        color = (i, 0, 255 - i)
    elif i <= 255 * 2:
        color = (255 * 2 - i, i - 255, 0)
    elif i <= 255 * 3:
        color = (0, 255 * 3 - i, i - 255 * 2)
    elif i > 255 * 3:
        i = 0
        color = (0, 0, 255)
    i += 1
    return color

def random_color():
    return (random.randrange(0, 255),
            random.randrange(0, 255),
            random.randrange(0, 255))

def fire_color():
    f = 15
    global fire_var, Fire
    if fire_var + f <= 255 and not Fire:
        fire_var += f
        return 255, fire_var, 0
    if fire_var == 255: Fire = True
    if fire_var - f == 0: Fire = False
    if fire_var - f >= 0 and Fire:
        fire_var -= f
        return 255, fire_var, 0
    return 255, 0, 0


def transition(b):
    global bgs
    n = True
    v = 0
    if b:
        while n:
            pygame.draw.rect(win, (0, 0, 0), (w - v, 0, v, h))
            pygame.draw.rect(win, (0, 0, 0), (0, 0, v, h))
            pygame.draw.rect(win, random_color(), (w - v, 0, v, h), 1)
            pygame.draw.rect(win, random_color(), (0, 0, v, h), 1)
            if v < w // 2:
                v += 10
            else:
                break
            pygame.display.update()
            clock.tick(40)
    else:
        while n:
            win.fill((0, 0, 0))
            pygame.draw.rect(win, (0, 0, 0), (0, 0, w // 2 - v, h))
            pygame.draw.rect(win, (0, 0, 0), (w // 2 + v, 0, w // 2 - v, h))
            pygame.draw.rect(win, random_color(), (0, 0, w // 2 - v, h), 1)
            pygame.draw.rect(win, random_color(), (w // 2 + v, 0, w // 2 - v, h), 1)
            if v < w // 2:
                v += 10
            else:
                break
            pygame.display.update()
            clock.tick(40)
