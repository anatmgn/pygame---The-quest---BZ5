import pygame as pg
from pygame.locals import *
import random
from random import choice,randint
from constants import *

clock=pg.time.Clock()

class Rocket(pg.sprite.Sprite):  

    def __init__(self,x=0,y=SCREEN_HEIGHT//2):
        
        pg.sprite.Sprite.__init__(self)

        self.image=pg.image.load(ROCKET_IMAGE)
        self.image=pg.transform.scale(self.image,ROCKET_RESIZE_IMAGE)

        self.boom=False       
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.x=x
        self.rect.y=y
        self.w=self.rect.w 
        self.h=self.rect.h
        self.rocket_speed=ROCKET_SPEED

    def crash_check(self,group):
        crash=pg.sprite.spritecollide(self,group,True)
        self.candidates=len(crash)
        if self.candidates>0: 
            self.boom=True

    def update(self,click):
        if not self.boom:
            self.rocket=self.image

        else:             
            self.boom=True
            pg.mixer.music.pause()
        
            self.image=pg.image.load(BOOM_IMAGE)
            self.image=pg.transform.scale(self.image,BOOM_RESIZE_IMAGE)
            self.rocket_speed=0

            pg.mixer.init()
            self.game_over_sound=pg.mixer.music.load(GAME_OVER_SOUND)
            pg.mixer.music.play()

class Asteroid(pg.sprite.Sprite):    
    score=0
    
    def __init__(self,x=randint(780, 800),y=randint(10,550),w=0,h=0,speed = 1):
        pg.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.speed=speed  
        
        self.asteroids=[]     
        
        self.image=pg.image.load(ASTEROID_IMAGE)
        self.image=pg.transform.scale(self.image,ASTEROID_RESIZE_IMAGE)
        self.asteroids.append(self.image)
        self.image=(random.choice(self.asteroids))

        self.rect=self.image.get_rect()   
        self.rect.x=x
        self.rect.y=y
        self.w=self.rect.w
        self.h=self.rect.h   

        self.boom=False 

    def update(self,click):
        self.rect.x-=self.speed
        if self.rect.x <= -self.rect.w or self.boom==True:                      
            self.kill() 
            del self

    def crash_check(self,group):
        crash=pg.sprite.spritecollide(self,group,True)
        self.candidates=len(crash)
        if self.candidates > 0: 
            self.boom=True