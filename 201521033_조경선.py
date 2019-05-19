"""Pygame_201521033 조경선"""
"""20180616 fianl assignment for 창의소프트웨어입문"""

import pygame, sys
import random
from pygame.locals import *
from time import sleep

#base variable
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
bg_width = 800
bg_height = 550
FPS = 30 #frame
dir_up = 0
dir_down = 1

#fish info
fish_width = 70
fish_height = 54
fish_x = 50
fish_y = bg_height / 2
fish_dir = random.randrange(0, 1)

#kid info
kid_width = 70
kid_height = 57
kid_x = 700
kid_y = 270

#bean info
miss_bean = 3
bean_x = fish_x + fish_width - 5
bean_y = fish_y

#display text
def txt_dis(text):
    global Background
    txtfont = pygame.font.Font(None, 50)
    text_ob = txtfont.render(text, True, BLACK)
    textpos = text_ob.get_rect()
    textpos.center = (bg_width/2, bg_height/2)
    Background.blit(text_ob, textpos)
    pygame.display.update()


#When you miss bean
def miss(count):
    global Background
    font = pygame.font.SysFont(None, 20)
    text = font.render('Life: ' + str(count), True, BLACK)
    Background.blit(text, (700,10))

#When game is over
def gameover():
    global Background
    fontobj = pygame.font.Font('freesansbold.ttf', 32)
    textSurob = fontobj.render('Game over', True, RED)
    text_pos = textSurob.get_rect()
    text_pos.center = (bg_width/2, bg_height/2)
    Background.blit(textSurob, text_pos)
    pygame.display.update()
    sleep(1)
    pygame.quit()
    sys.exit()

#drawing the object
def draw_object(obj, x, y):
    global Background
    Background.blit(obj,(x,y))

def init_bg():
    global Background, kid2_img, fish2_img, heart_img
    Background.fill(WHITE)
    kid2_img = pygame.image.load('kid2.png')
    fish2_img = pygame.image.load('fish2.png')
    heart_img = pygame.image.load('heart.png')
    draw_object(kid2_img, bg_width*0.55, bg_height*0.1)
    draw_object(heart_img, 250, bg_height*0.1)
    draw_object(fish2_img, 300, bg_height*0.17)

    name_font = pygame.font.SysFont(None, 20)
    name_text = name_font.render('Chokyungsun 201521033', True, BLACK)
    Background.blit(name_text, (10, 530))

#main
def run_Game():
    global Background, fps_clock, fish_img, kid_img, bean_img
    global fish_dir, fish_y, fish_x, kid_y, kid_x, bean_x,bean_y, miss_bean

    kid_xchange = 0
    kid_ychange = 0

    #for pressing key event
    keystate = pygame.key.get_pressed()
    if keystate[K_DOWN]:
        kid_ychange += 8
    if keystate[K_UP]:
        kid_ychange -= 8
    if keystate[K_RIGHT]:
        kid_xchange += 8
    if keystate[K_LEFT]:
        kid_xchange -= 8

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                kid_ychange += 8
            if event.key == K_UP:
                kid_ychange -= 8
            if event.key == K_RIGHT:
                kid_xchange += 8
            if event.key == K_LEFT:
                kid_xchange -= 8

    Background.fill(WHITE)
    name_font = pygame.font.SysFont(None, 20)
    name_text = name_font.render('Chokyungsun 201521033', True, BLACK)
    Background.blit(name_text, (10, 530))

    #relocate the kid_y
    kid_y += kid_ychange
    if kid_y < 0:
        kid_y = 0
    elif kid_y > bg_height - kid_height:
        kid_y = bg_height - kid_height

    #relocate the kid_x
    kid_x += kid_xchange
    if kid_x < 580:
        kid_x = 580
    elif kid_x > bg_width - kid_width:
        kid_x = bg_width - kid_width

    # moving fish
    if fish_dir == dir_up:
        fish_y -= 5
        if fish_y == 0:
            fish_dir = dir_down
    elif fish_dir == dir_down:
        fish_y += 5
        if fish_y == 500:
            fish_dir = dir_up

    draw_object(fish_img, fish_x, fish_y)
    draw_object(kid_img, kid_x, kid_y)
    pygame.draw.line(Background, BLACK, (580,0),(580,bg_height),1)

    #Bean
    miss(miss_bean)
    bean_x += 15
    if bean_x >= bg_width:
        miss_bean -= 1;
        miss(miss_bean)
        if miss_bean <= 0:
            gameover()
        bean_x = fish_x + fish_width - 5
        bean_y = fish_y
    if kid_x - kid_width/2 <= bean_x and bean_x <= kid_x+kid_width/2:
        if kid_y - kid_height/2 <= bean_y and bean_y <= kid_y + kid_height/2:
            bean_x = fish_x + fish_width - 5
            bean_y = fish_y

    draw_object(bean_img, bean_x,  bean_y)



    pygame.display.update()
    fps_clock.tick(FPS)
    run_Game()

#init game
def init_Game():
    global Background, fps_clock, kid_img, bean_img, fish_img

    pygame.init()
    Background = pygame.display.set_mode((bg_width, bg_height))  # (width, height)
    pygame.display.set_caption('짱구붕어빵게임')  # title

    init_bg()

    txt_dis('<<Eat the beans!!>>')
    sleep(2)
    init_bg()
    txt_dis('3')
    sleep(1)
    init_bg()
    txt_dis('2')
    sleep(1)
    init_bg()
    txt_dis('1')
    sleep(1)

    # image load
    fish_img = pygame.image.load('fish.png')
    kid_img = pygame.image.load('kid.png')
    bean_img = pygame.image.load('blackbullet.png')
    fps_clock = pygame.time.Clock()

init_Game()
run_Game()

