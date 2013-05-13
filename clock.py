import os
import pygame
import time
import random
import math
from time import strftime, localtime
from screen import screen
import Queue
import imgthread as imgthread

queue = Queue.Queue()

screen = screen()
pygame.mouse.set_visible(0)
font = pygame.font.Font('segoeui.ttf', 90)
dateFont = pygame.font.Font('segoeui.ttf', 35)
lastTime = ""
currentImg = None
lastImg = None
imgt = imgthread.imgthread(queue)
imgt.setDaemon(True)
imgt.start()
fade = 0
while 1:
    if(not queue.empty()):
        lastImg = currentImg
        currentImg = queue.get()
        fade = 0
    if(currentImg != None):
        if(fade < 255 and lastImg != None):
            currentImg.surface.set_alpha(fade)
            lastImg.surface.set_alpha(255 - fade)
            fade += 255/60
            screen.scr.blit(lastImg.surface, (-lastImg.offset_x, -lastImg.offset_y))
            screen.scr.blit(currentImg.surface, (-currentImg.offset_x, -currentImg.offset_y))
        else:
            if(lastImg in locals() and lastImg != None):
                del(lastImg)
            currentImg.surface.set_alpha(255)
            screen.scr.blit(currentImg.surface, (-currentImg.offset_x, -currentImg.offset_y))
    else:
        screen.scr.fill((0,0,0))
    current = strftime("%I:%M:%S %p", localtime()).lstrip('0')
    currentDate = strftime("%A, %B %d", localtime())
    if(lastTime != current):
        text_surface = font.render(current, True, (255, 255, 255))
        text_surface_shadow = font.render(current, True, (0, 0, 0))
        date_surface = dateFont.render(currentDate, True, (255, 255, 255))
        date_surface_shadow = dateFont.render(currentDate, True, (0, 0, 0))
    screen.scr.blit(text_surface_shadow, (87, 437))
    screen.scr.blit(text_surface, (85, 435))
    screen.scr.blit(date_surface_shadow, (86, 551))
    screen.scr.blit(date_surface, (85, 550))
    lastTime = current
    pygame.display.update()
    time.sleep(1.0/60.0)