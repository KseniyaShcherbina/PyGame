import pygame
import time
pygame.init()

white = (255, 255, 255)
green = (34, 187, 19)
red = (255, 0, 0)
black = (0, 0, 0)
W = 650
H = 600
speed = 10
dis = pygame.display.set_mode((W, H))
pygame.display.set_caption("Беги!")
pygame.display.set_icon(pygame.image.load("img/beg2.png"))
clock = pygame.time.Clock()



def loos(a, b,c):
    font1 = pygame.font.SysFont('Arial', b)
    loos = font1.render(a, 1, c)
    dis.blit(loos, (20, H // 2 - 30))


def win(a):
    font2 = pygame.font.SysFont('Arial', 80)
    win = font2.render(a, 1, green)
    dis.blit(win, (W // 2 - 200, H // 2 - 80))


def gameLoop():
    game_over = False
    game_close = False

    pesok = pygame.image.load("img/pesok.jpg").convert()
    water = pygame.image.load("img/voda.png").convert()
    rect_water1 = water.get_rect(centerx=140, bottom=H)
    rect_water2 = water.get_rect(centerx=405, bottom=H)
    grass = pygame.image.load("img/trava1.jpg").convert()
    dirt = pygame.image.load("img/gr.jpg").convert()
    zabor = pygame.image.load("img/zb2.png").convert_alpha()
    dom = pygame.image.load("img/dom2.png").convert_alpha()
    rect_dom = dom.get_rect(centerx=590, bottom=160)
    trassa = pygame.image.load("img/trassa.png").convert_alpha()
    vova = pygame.image.load("img/1.png").convert_alpha()
    rect_vova = vova.get_rect(centerx=40, bottom=300)
    krok1 = pygame.image.load("img/kr1.png").convert_alpha()
    rect_krok1 = krok1.get_rect(centerx=130, bottom=370)
    rect_krok2 = krok1.get_rect(centerx=400, bottom=100)
    plot = pygame.image.load("img/plot.png").convert_alpha()
    rect_plot = plot.get_rect(centerx=135, bottom=70)
    rect_plot2 = plot.get_rect(centerx=400, bottom=400)
    str = pygame.image.load("img/str.png").convert_alpha()
    kaktus = pygame.image.load("img/kaktus.png").convert_alpha()

    while not game_over:
        while game_close == True:
            dis.fill(black)
            loos('Вы проиграли! 1 - Начать заново 2 - Выход', 35,red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_1:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rect_vova.x -= 90
                    if rect_vova.x < 0:
                        rect_vova.x = -35
                elif event.key == pygame.K_RIGHT:
                    rect_vova.x += 90
                    if rect_vova.x > W - rect_vova.width:
                        rect_vova.x = 520
                elif event.key == pygame.K_UP:
                    rect_vova.y -= 20
                    if rect_vova.y < 0:
                        rect_vova.y = 0
                elif event.key == pygame.K_DOWN:
                    rect_vova.y += 20
                    if rect_vova.bottom > H:
                        rect_vova.bottom = H

        dis.blit(pesok, (0, 0))
        dis.blit(water, rect_water1)
        dis.blit(dirt, (190, 0))
        dis.blit(water, rect_water2)
        dis.blit(grass, (460, 0))
        dis.blit(dom, rect_dom)
        dis.blit(trassa, (460, 130))
        dis.blit(zabor, (500, 130))
        dis.blit(krok1, rect_krok1)
        dis.blit(plot, rect_plot)
        dis.blit(krok1, rect_krok2)
        dis.blit(plot, rect_plot2)
        dis.blit(kaktus, (270, 180))
        dis.blit(str, (240, 400))
        dis.blit(vova, rect_vova)

        if rect_krok1.y < H:
            rect_krok1.y += speed
        else:
            rect_krok1.y = 0
        if rect_krok2.y < H:
            rect_krok2.y += speed + 10
        else:
            rect_krok2.y = 0
        if rect_plot.y < H:
            rect_plot.y += speed
        else:
            rect_plot.y = 0
        if rect_plot2.y < H:
            rect_plot2.y += speed + 10
        else:
            rect_plot2.y = 0

        if rect_water1.collidepoint(rect_vova.center) and not rect_plot.collidepoint(
                rect_vova.center) and not rect_krok1.collidepoint(rect_vova.center):
            loos("Вы утонули!", 100, white)
            pygame.display.update()
            time.sleep(3)
            game_close = True
        elif rect_plot.collidepoint(rect_vova.center):
            rect_vova.y += speed
            if rect_vova.bottom == H:
                game_close = True
        elif rect_krok1.collidepoint(rect_vova.center) or rect_krok2.collidepoint(rect_vova.center):
            loos("Вас съел крокодил!",80,white)
            pygame.display.update()
            time.sleep(3)
            game_close = True
        elif rect_water2.collidepoint(rect_vova.center) and not rect_plot2.collidepoint(
                rect_vova.center) and not rect_krok2.collidepoint(rect_vova.center):
            game_close = True
        elif rect_plot2.collidepoint(rect_vova.center):
            rect_vova.y += speed + 10
            if rect_vova.bottom == H:
                game_close = True
        elif rect_dom.collidepoint(rect_vova.center):
            dis.fill(white)
            win('Вы выйграли!')
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(10)

    pygame.quit()
    quit()


gameLoop()
