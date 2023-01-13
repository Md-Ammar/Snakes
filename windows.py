import accessories as acc
import pygame
import random
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE

pygame.init()
w, h = 1000, 700
win = pygame.display.set_mode((w, h), HWSURFACE | DOUBLEBUF | RESIZABLE)

clock = pygame.time.Clock()

score = 0
font1 = pygame.font.SysFont('old english text', 45)
font2 = pygame.font.SysFont('chiller', 25, True)

#defaults
Design = False
transition = False#transitioning colours
checkered = True
multicolor = False
border = True

des_coord = []
design = []
for i in range(0, 5):
    design.append(False)
design[4] = True

Color = Color_2 = []
colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200),
          (200, 200, 0), (0, 200, 200), (200, 0, 200),
          (200, 100, 100), (100, 200, 100), (100, 100, 200)]
# red, green, blue
# yellow, cyan, pink
# white, black, deep cream

Pcolor = colors[0]  # defaults
Scolor = colors[1]
pcolor_rect = 0
scolor_rect = 0
bg_rects = []
for i in range(w//30):
    bg_rects.append([random.randrange(0, w), random.randrange(0, h), random.randrange(5, 30), acc.random_color()])

# def background():
#     for i in range(random.randrange(5, 20)):
#         size = random.randrange(0, 30)
#         box = pygame.Rect(random.randrange(0, w - size), random.randrange(0, h - size), size, size)
#         # pygame.draw.circle(win, (random.randrange(0, 255),
#         #                          random.randrange(0, 255),
#         #                          random.randrange(0, 255)), (box.x, box.y), size//2)
#         pygame.draw.rect(win, (random.randrange(0, 255),
#                                random.randrange(0, 255),
#                                random.randrange(0, 255)), (box.x, box.y, size, size))
#     pygame.display.update()

def background2():
    for i in bg_rects:
        i[1] += 10
        if i[1] >= h:
            bg_rects.pop(bg_rects.index(i))
            bg_rects.append([random.randrange(0, w), 0, random.randrange(5, 30), acc.random_color()])
        else:
            pygame.draw.circle(win, acc.random_color(), (i[0], i[1]), i[2], 1)
            # pygame.draw.rect(win, acc.random_color(), (i[0], i[1], 5, 15))

def menu(scr):
    global Pcolor, Scolor, colors, w, h, Type, Bg, run
    global pos_img, init_pos_img

    if Pcolor == 0: Pcolor = colors[1]
    if Scolor == 0: Scolor = colors[2]
    n = True
    b = "NEW GAME" if scr == 0 else "CONTINUE"
    name = ''

    # j = 0
    # ttr = 0
    while n:
        win.fill((0, 0, 0))
        background2()
        # for k in range(0,w): # rainbow effect
        #     j+=1
        #     if j<=255:
        #         pygame.draw.line(win,(j,0,0),(k,0),(k,h))
        #     elif j<=255*2:
        #         pygame.draw.line(win,((255*2-j),j-255,0),(k,0),(k,h))
        #     elif j<=255*3:
        #         pygame.draw.line(win,(0,(255*3-j),j-255*2),(k,0),(k,h))
        #     else:
        #         j=1
        # win.fill((0,0,0))

        # for i in range(0, len(bgs)): # moving images
        #     img = bgs[i]
        #     if pos_img[bgs.index(img)] < w:
        #         win.blit(pygame.transform.scale(img, (1000, 700)), (pos_img[bgs.index(img)], 0))
        #     for i in range(0, len(pos_img)):
        #         pos_img[i] -= 5
        #     if pos_img[len(pos_img) - 1] < 0:
        #         for i in range(0, len(init_pos_img)):
        #             pos_img[i] = init_pos_img[i]

        # j += 1
        # if ttr < 500:
        #     ttr += 10
        #     # pygame.draw.rect(win,(0,200,200),(250,100,ttr,100))
        #     acc.msg_heading("THE SNAKE GAME", (0, 0, 0), 150)
        # else:
        #     pass
        #     pygame.draw.rect(win,(0,200,200),(250,100,ttr,100))]
        pygame.draw.rect(win, (0, 0, 0), (w // 2 - 250, 125, 500, 50))
        pygame.draw.rect(win, acc.changing_colors(), (w//2 - 250, 125, 500, 50), 1)
        acc.msg_heading("THE SNAKE GAME", acc.fire_color(), 150)

        acc.msg("Developer: Ammar", (0, 0, 0), w - 180, h - 30)

        start = acc.buttons(b, w // 2 - 25, 400, True)
        custom = acc.buttons("CUSTOMIZE", w // 2 - 25, 450, True)

        if name == '':
            txtbx = (w // 2 - 50, 500)
            acc.msg("PLAYER NAME:", (0, 0, 0), w // 2 - 250, 500)
            pygame.draw.rect(win, (200, 200, 200), (txtbx, (200, 30)))  # textbox
            pygame.draw.rect(win, (100, 100, 100), (txtbx, (200, 30)), 2)
            win.blit(font2.render("ENTER TEXT HERE", 1, (100, 100, 100)), txtbx)
        else:
            acc.msg("GREETINGS " + str(name), (200, 0, 200), w // 2 - 50, 500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                w = acc.w = screen.get_width()
                h = acc.h = screen.get_height()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    acc.transition(True)
                    n = False
                if event.key == pygame.K_ESCAPE:
                    n = False
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if pygame.Rect(txtbx, (200, 30)).collidepoint(x, y):
                    name = acc.textbox(txtbx, 200)
                if start.collidepoint(x, y):
                    acc.transition(True)
                    n = False
                if custom.collidepoint(x, y):
                    n = False
                    customize()
        pygame.display.update()
        clock.tick(10)


def color(c):  # recieves coordinates list
    global colors
    for i in range(0, len(colors)):
        pygame.draw.rect(win, colors[i], c[i])
        if colors[i] == (0, 0, 0): pygame.draw.rect(win, (255, 255, 255), c[i], 1)


def set_col_coord():
    global Color, Color_2, pcolor_rect, scolor_rect
    Color = []
    Color_2 = []
    for i in range(0, len(colors)):  # colors
        Color.append(((w // 2 - 150) + i * 50, 200, 25, 25))
    for i in range(0, len(colors)):
        Color_2.append(((w // 2 - 150) + i * 50, 250, 25, 25))
    pcolor_rect = Color[colors.index(Pcolor)]
    scolor_rect = Color_2[colors.index(Scolor)]


def customize():
    global run, checkered, colors, Color, Color_2, Pcolor, Scolor, pcolor_rect, scolor_rect, transition, w, h, multicolor,design, Design, border
    n = True
    set_col_coord()

    for i in range(0, 5):
        des_coord.append(acc.buttons("     ", w // 2 + 50, 400 + i * 50, True))
    while n:
        win.fill((0, 200, 200))

        acc.msg_heading("CUSTOMIZE", (200, 0, 200), 100)#x=w//2-400
        acc.msg("COLOUR SETTINGS:", (0, 0, 0), w // 2 - 400, 300)
        acc.msg("DESIGN SETTINGS:", (0, 0, 0), w // 2 - 400, 350)

        check = acc.buttons("CHECKS", w // 2 - 140, 300, checkered)
        multi = acc.buttons("MULTICOLOR", w // 2 - 20, 300, multicolor)
        Transition = acc.buttons("TRANSITION", w // 2 + 140, 300, transition)

        DESIGN = acc.buttons("TEXTURE", w // 2 - 60, 350, design)
        Border = acc.buttons("BORDER", w // 2 + 60, 350, border)

        done = acc.buttons("DONE", w // 2 - 30, 650, True)

        if Design:
            for i in range(0, 5):
                acc.msg("DESIGN " + str(i + 1) + ":", (0, 0, 0), w // 2 - 100, 400 + i * 50)
                acc.buttons("     ", des_coord[i].x, des_coord[i].y, True)
                if design[i]:
                    pygame.draw.rect(win, (0, 255, 0), des_coord[i], 3)
                else:
                    pygame.draw.rect(win, (255, 0, 0), des_coord[i], 3)

            p = [w // 2 + 50 + 10, 400 + 10]
            pygame.draw.rect(win, (255, 255, 255), (w // 2 + 50 + 2, 400 + 2, 40, 25))
            pygame.draw.line(win, (0, 0, 0), (p[0] + 4, p[1]), (p[0] + 4, p[1] + 10), 2)
            pygame.draw.line(win, (0, 0, 0), (p[0], p[1] + 4), (p[0] + 10, p[1] + 4), 2)
            pygame.draw.line(win, (0, 0, 0), p, (p[0] + 10, p[1] + 10), 2)
            pygame.draw.line(win, (0, 0, 0), (p[0] + 10, p[1]), (p[0], p[1] + 10), 2)

            p = [w // 2 + 50 + 10, 450 + 10]
            pygame.draw.rect(win, (255, 255, 255), (w // 2 + 50 + 2, 450 + 2, 40, 25))
            pygame.draw.circle(win, (0, 0, 0), (p[0] + 5, p[1] + 5), random.randrange(1, 5))

            p = [w // 2 + 50 + 10, 500 + 10]
            pygame.draw.circle(win, (255, 255, 255), (p[0] + 5, p[1] + 5), random.randrange(1, 10), 1)

            p = [w // 2 + 50 + 10, 550 + 10]
            d = random.randrange(1, 10)
            pygame.draw.rect(win, (200, 200, 200), (p[0] + 5 - d, p[1] + 5 - d, d * 2, d * 2), 1)

            p = [w // 2 + 50 + 10, 600 + 10]
            pygame.draw.rect(win, (255, 255, 255), (w // 2 + 50 + 2, 600 + 2, 40, 25))
            pygame.draw.line(win, (0, 0, 0),
                             (random.randrange(p[0], p[0] + 10), random.randrange(p[1], p[1] + 10)),
                             (random.randrange(p[0], p[0] + 10), random.randrange(p[1], p[1] + 10)), 2)

        pygame.draw.rect(win, (0, 255, 0) if Design else (255, 0, 0), DESIGN, 3)
        pygame.draw.rect(win, (0, 255, 0) if border else (255, 0, 0), Border, 3)

        if not transition or multicolor:
            pygame.draw.rect(win, (255, 0, 0), Transition, 3)

            if checkered:
                pygame.draw.rect(win, (0, 255, 0), check, 3)  # acc.buttonstaysgreen
                pygame.draw.rect(win, (0, 0, 0), ((w // 2 - 360), 195, int((len(colors) + 1) * 25 * 2 + 140), 90))
                pygame.draw.rect(win, (200, 0, 0), ((w // 2 - 360), 195, int((len(colors) + 1) * 25 * 2 + 140), 90), 3)
                acc.msg("COLOUR 1:", Pcolor, w // 2 - 340, 200)
                acc.msg("COLOUR 2:", Scolor, w // 2 - 340, 250)
                color(Color)  # sending coords
                color(Color_2)  # sending coords
                if scolor_rect != 0:
                    pygame.draw.rect(win, acc.fire_color(), scolor_rect, 5)

            if not checkered:
                pygame.draw.rect(win, (255, 0, 0), check, 3)  # buttonred
                pygame.draw.rect(win, (0, 0, 0), ((w // 2 - 360), 195, int((len(colors) + 1) * 25 * 2 + 140), 35))
                pygame.draw.rect(win, (200, 0, 0), ((w // 2 - 360), 195, int((len(colors) + 1) * 25 * 2 + 140), 35), 3)
                acc.msg("COLOUR 1:", Pcolor, w // 2 - 340, 200)  # sending coords
                color(Color)

            if pcolor_rect != 0:
                pygame.draw.rect(win, acc.fire_color(), pcolor_rect, 5)

        else:
            # acc.msg_heading("CHANGING COLOURS",changing_colors(),h//2-150)
            acc.msg("CHANGING COLOURS", acc.changing_colors(), w // 2 - 100, h // 2 - 150)
            pygame.draw.rect(win, (100, 100, 100), check, 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                n = False
                pygame.display.quit()
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                w = screen.get_width()
                h = screen.get_height()
                for i in range(0, 4):
                    des_coord[i] = acc.buttons("     ", w // 2 + 50, 400 + i * 50, True)
                set_col_coord()  # reset color coord list

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    n = False
                if event.key == pygame.K_ESCAPE:
                    n = False
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if multi.collidepoint(x, y):
                    multicolor = True if not multicolor else False

                if Transition.collidepoint(x, y):
                    transition = True if not transition else False

                if not transition:
                    for c in Color:
                        c = pygame.Rect(c)
                        if c.collidepoint(x, y):
                            pcolor_rect = c
                            Pcolor = colors[Color.index(c)]
                            break
                    if checkered:
                        for c in Color_2:
                            c = pygame.Rect(c)
                            if c.collidepoint(x, y):
                                scolor_rect = c
                                Scolor = colors[Color_2.index(c)]
                                break

                if done.collidepoint(x, y):
                    pygame.draw.rect(win, (0, 255, 0), done, 3)
                    n = False

                if check.collidepoint(x, y):
                    pygame.draw.rect(win, (0, 255, 0), check, 3)
                    if checkered:
                        checkered = False
                    elif not checkered:
                        checkered = True
                    n = False
                    customize()

                if DESIGN.collidepoint(x, y):
                    if Design:
                        Design = False
                    else:
                        Design = True

                if Design:
                    for d in des_coord:
                        if d.collidepoint(x, y):
                            for i in range(0, len(design)):
                                design[i] = False
                            if design[des_coord.index(d)]:
                                design[des_coord.index(d)] = False
                            else:
                                design[des_coord.index(d)] = True

                if Border.collidepoint(x, y):
                    border = True if not border else False

        pygame.display.update()
        clock.tick(15)
