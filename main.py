import pygame as pg
from pygame.locals import *
import sys,random,os
from random import *

from entities import *
from constants import *

class Start():
    def __init__(self):

        pg.font.init()

        self.screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.display=pg.display.set_caption (GAME_NAME)
        self.background_image=pg.image.load('resources/images/menu.jpg').convert()
        self.background_image=pg.transform.scale(self.background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.font=pg.font.Font('resources/fonts/dorado.ttf', 32)

        self.screen.blit(self.background_image, (0, 0))

        self.font_small=pg.font.Font(FONT,FONT_SIZE_SMALL)#
        self.font_medium=pg.font.Font(FONT,FONT_SIZE_MEDIUM)#
        self.font_big=pg.font.Font(FONT,FONT_SIZE_BIG)#
        
        self.game_name= elf.font_big.render(GAME_NAME,True,TEXT_STRONG_COLOUR)
        self.start=self.font_medium.render(START_MODE,True,TEXT_WEAK_COLOUR)
        self.instructions=self.font_small.render(INSTRUCTIONS,True,TEXT_WEAK_COLOUR)
      
        self.screen.blit(self.GAME_NAME,(130, 150))
        self.screen.blit(self.START,(120, 400))
        self.screen.blit(self.INSTRUCTIONS,(90, 450))

    def handleEvents(self):
        for event in pg.event.get():
            if event.type==QUIT:               
                quit()
            if event.typ==K_SPACE:
                self.mainloop()

class Game:
    clock=pg.time.Clock()
    level=1
    score=0

    def __init__(self):
        pg.font.init()
      
        self.screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pg.display.set_caption(GAME_NAME)
        self.background_image=pg.image.load(BACKGROUND_IMAGE)
        self.background_image=pg.transform.scale(self.background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.font_small=pg.font.Font(FONT,FONT_SIZE_SMALL)#
        self.font_medium=pg.font.Font(FONT,FONT_SIZE_MEDIUM)#
        self.font_big=pg.font.Font(FONT,FONT_SIZE_BIG)#

        self.rocket=Rocket()
        self.asteroid=Asteroid()

        self.asteroidsGroup=pg.sprite.Group()
        self.rocketGroup=pg.sprite.Group()
        
        self.asteroidsGroup.add(self.asteroid)
        self.rocketGroup.add(self.rocket)

        self.new_asteroids_number=0
        self.simultaneus_asteroids=SIMULTANEUS_ASTEROIDS

        self.level=1

        pg.mixer.init()
        self.game_music=pg.mixer.music.load(GAME_MUSIC)
        pg.mixer.music.play(-1)

    def newAsteroid(self,click): 
        self.asteroid=Asteroid(randint(780,840),randint(10,550))
        self.asteroid.speed=(randint(ASTEROID_MIN_SPEED,ASTEROID_MAX_SPEED))
        self.asteroidsGroup.add(self.asteroid)
        self.new_asteroids_number+=1
      
    def text(self):
        self.scoreboard=self.font_small.render('Puntuación: ',True,TEXT_WEAK_COLOUR)
        self.level_scoreboard=self.font_small.render('Nivel: ',True,TEXT_WEAK_COLOUR)
        self.scoreboard_data=self.font_small.render(str(self.score),True,TEXT_WEAK_COLOUR)
        self.level_scoreboard_data=self.font_small.render(str(self.level),True,TEXT_WEAK_COLOUR)
        
    def quit(self):
        pg.quit()
        sys.exit()

    def gameOver(self,click):
        self.handleEvents(click)
        
        self.game_over1=self.font_big.render(GAME_OVER_1_TEXT,True,TEXT_STRONG_COLOUR)
        self.game_over2=self.font_medium.render(GAME_OVER_2_TEXT,True,TEXT_WEAK_COLOUR)
      
        self.screen.blit(self.game_over1,(130, 150))
        self.screen.blit(self.game_over2,(120, 400))

    def handleEvents(self):
        for event in pg.event.get():
            if event.type==QUIT:
                self.quit()

            if event.type==KEYDOWN:
                if event.key==K_UP:
                    self.rocket.rect.y = max(0,self.rocket.rect.y - self.rocket.rocket_speed)

                if event.key==K_DOWN:
                    self.rocket.rect.y=min(self.rocket.rect.y + self.rocket.rocket_speed,535)

                if event.key==K_SPACE:
                    self.playing=False

        keys_pressed=pg.key.get_pressed()

        if keys_pressed[K_UP]:
            self.rocket.rect.y=max(0,self.rocket.rect.y - self.rocket.rocket_speed)
        if keys_pressed[K_DOWN]:
            self.rocket.rect.y=min(self.rocket.rect.y + self.rocket.rocket_speed,535)


    def nextLevel(self,click):
        if  self.score>200:
            self.level+=1 
            self.asteroid=Asteroid(randint(780,840),randint(10,550))
            self.asteroid.speed=(randint(ASTEROID_MIN_SPEED*2,ASTEROID_MAX_SPEED*self.level))
            self.asteroidsGroup.add(self.asteroid)
            self.new_asteroids_number+=1

    def update_game(self,click):

        self.screen.blit(self.background_image,(0,0))
        self.screen.blit(self.scoreboard,(10,10))
        self.screen.blit(self.scoreboard_data,(170,10))
        self.screen.blit(self.level_scoreboard,(10,40))
        self.screen.blit(self.level_scoreboard_data,(80,40))

        self.asteroidsGroup.update(click)
        self.rocketGroup.update(click)

        self.asteroidsGroup.draw(self.screen)
        self.rocketGroup.draw(self.screen)
        
    def game_loop(self,click):    
        self.handleEvents()
        self.rocket.crash_check(self.asteroidsGroup)

        self.number_of_asteroids = len(self.asteroidsGroup)
        if self.number_of_asteroids<self.simultaneus_asteroids:
            self.newAsteroid(click)
        
        if  self.new_asteroids_number>self.simultaneus_asteroids:
            self.score=self.new_asteroids_number*10
        
        self.text()
        self.update_game(click)

    def mainloop(self):
        self.playing=True
        while self.playing:

            click=self.clock.tick(FPS)

            if not self.rocket.crash_check(self.asteroidsGroup):
                self.game_loop(click)
            else:
                self.gameOver(click)

            pg.display.flip()

if __name__=='__main__':
    pg.init()
    game=Game()
    game.mainloop()