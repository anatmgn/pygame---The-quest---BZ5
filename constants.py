import pygame as pg
from pygame.locals import *
import random
from random import randint

### ASTEROID ###
ASTEROID_IMAGE='./resources/images/asteroid01.png'
ASTEROID_MIN_SPEED=1
ASTEROID_MAX_SPEED=5
ASTEROID_RESIZE_IMAGE=(50,50)
SIMULTANEUS_ASTEROIDS=10

### FONT ###
FONT='resources/fonts/dorado.ttf'
FONT_SIZE_BIG=62
FONT_SIZE_MEDIUM=32
FONT_SIZE_SMALL=22

### GENERAL ###
BACKGROUND_IMAGE='resources/images/space.jpg'
BOOM_IMAGE='resources/images/boom.png'
BOOM_RESIZE_IMAGE=(110,90)
FPS = 60
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
TEXT_STRONG_COLOUR=(255,0,0) #red
TEXT_WEAK_COLOUR=(255,255,255) #white

### MUSIC ###
GAME_MUSIC='./resources/sounds/game_music.mp3'
GAME_OVER_SOUND='./resources/sounds/game_over_sound.mp3'

### ROCKET ###
ROCKET_IMAGE='./resources/images/spaceship.png'
ROCKET_RESIZE_IMAGE=(90,70)
ROCKET_SPEED=5

### TEXT ###
GAME_NAME='Another world :)'
GAME_OVER_1_TEXT='GAME OVER'
GAME_OVER_2_TEXT='<SPACE> para comenzar de nuevo'
INSTRUCTIONS='Para mover usa las flechas. Cierra ventana para salir'
START_MODE='<SPACE> para comenzar'