import pygame as pg
from pygame.locals import *
import sys,random,os
from random import *

from entities import *
from constants import *
from menu import *

class Game:

    clock=pg.time.Clock()
    level=1
    score=0

    def __init__(self):
    ### PANTALLA ###   
        pg.display.set_caption(GAME_NAME)
        self.screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.background_image=pg.transform.scale(pg.image.load(BACKGROUND_IMAGE),(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.blit(self.background_image, (0, 0))

    ### ELEMENTOS EN PANTALLA ###
        self.rocket=Rocket()
        self.asteroid=Asteroid()

        self.asteroidsGroup=pg.sprite.Group()
        self.rocketGroup=pg.sprite.Group()
        
        self.asteroidsGroup.add(self.asteroid)
        self.rocketGroup.add(self.rocket)
    
        self.new_asteroids_number=0
        self.simultaneus_asteroids=SIMULTANEUS_ASTEROIDS

        self.game_over=False
    
    ### FUENTES ###   
        pg.font.init()
        self.font_small=pg.font.Font(FONT,FONT_SIZE_SMALL)
        self.font_medium=pg.font.Font(FONT,FONT_SIZE_MEDIUM)
        self.font_big=pg.font.Font(FONT,FONT_SIZE_BIG)
    
    ### PUNTUACIÓN Y NIVEL EN PANTALLA, BASE ###
        self.scoreboard=self.font_small.render('Puntuación: ',True,TEXT_WEAK_COLOUR)
        self.level_scoreboard=self.font_small.render('Nivel: ',True,TEXT_WEAK_COLOUR)
        self.scoreboard_data=self.font_small.render(str(self.score),True,TEXT_WEAK_COLOUR)
        self.level_scoreboard_data=self.font_small.render(str(self.level),True,TEXT_WEAK_COLOUR)
        
    ### MÚSICA ###
        pg.mixer.init()
        
        self.explosion_sound=pg.mixer.music.load(EXPLOSION_SOUND)
        self.game_over_sound=pg.mixer.music.load(GAME_OVER_SOUND)
        self.game_music=pg.mixer.music.load(GAME_MUSIC)

        if self.game_over==False:
            pg.mixer.music.play(-1)

    def draw_text(self,text, font, surface, x, y, main_color, background_color=None):   
    ### FUNCIÓN PARA ACONDICIONAR TEXTOS ###
        textobj = font.render(text, True, main_color)
        textrect = textobj.get_rect()
        textrect.centerx = x
        textrect.centery = y
        surface.blit(textobj, textrect)

    def credits(self):
    ### CRÉDITOS DEL JUEGO ###
        self.screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.background_image=pg.transform.scale(pg.image.load(BACKGROUND_IMAGE),(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.blit(self.background_image, (0, 0))
        credits1=self.draw_text(CREDITS1,self.font_small,self.screen,SCREEN_WIDTH/2,SCREEN_HEIGHT/4,TEXT_WEAK_COLOUR)
        credits2=self.draw_text(CREDITS2,self.font_small,self.screen,SCREEN_WIDTH/2,SCREEN_HEIGHT/2,TEXT_WEAK_COLOUR)
        credits3=self.draw_text(CREDITS3,self.font_small,self.screen,SCREEN_WIDTH/2,SCREEN_HEIGHT*3/4,TEXT_WEAK_COLOUR)
        
        pg.display.flip()      
        pg.time.delay(WAIT)          
       
    def instructions(self):
    ### INSTRUCCIONES DEL JUEGO ###
        self.screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.background_image=pg.transform.scale(pg.image.load(BACKGROUND_IMAGE),(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.blit(self.background_image, (0, 0))
        intructions1=self.draw_text(INSTRUCTIONS1,self.font_small,self.screen,SCREEN_WIDTH/2,SCREEN_HEIGHT/4,TEXT_WEAK_COLOUR)
        intructions2=self.draw_text(INSTRUCTIONS2,self.font_small,self.screen,SCREEN_WIDTH/2,SCREEN_HEIGHT/2,TEXT_WEAK_COLOUR)
        intructions3=self.draw_text(INSTRUCTIONS3,self.font_small,self.screen,SCREEN_WIDTH/2,SCREEN_HEIGHT*3/4,TEXT_WEAK_COLOUR)
        
        pg.display.flip()      
        pg.time.delay(WAIT)          
       
    def newAsteroid(self,click): 
    ###FUNCIÓN PARA CREAR NUEVOS ASTEROIDES###
        self.asteroid=Asteroid(randint((SCREEN_WIDTH-20),(SCREEN_WIDTH+20)),randint((SCREEN_HEIGHT/50),(SCREEN_HEIGHT-50)))
        self.asteroidsGroup.add(self.asteroid)
        self.asteroid.speed=(randint(ASTEROID_MIN_SPEED,ASTEROID_MAX_SPEED))
        self.new_asteroids_number+=1

    def gameOver(self,click):
    ### FIN DEL JUEGO, PANTALLA FIN ### REVISAR, NO FUNCIONA
        self.asteroid.game_over()

    def handleEvents(self):
    ### GESTIÓN DE EVENTOS ###
        for event in pg.event.get():
            if event.type==QUIT:
                self.quit()
            
            if event.type==K_SPACE:
                self.mainloop()

            if event.type==KEYDOWN:
                if event.key==K_UP:
                    self.rocket.rect.y = max(0,self.rocket.rect.y - self.rocket.rocket_speed)

                if event.key==K_DOWN:
                    self.rocket.rect.y=min(self.rocket.rect.y + self.rocket.rocket_speed,535)

        keys_pressed=pg.key.get_pressed()

        if keys_pressed[K_SPACE]:
            self.playing=True
            self.mainloop()
        if keys_pressed[K_UP]:
            self.rocket.rect.y=max(0,self.rocket.rect.y - self.rocket.rocket_speed)
        if keys_pressed[K_DOWN]:
            self.rocket.rect.y=min(self.rocket.rect.y + self.rocket.rocket_speed,535)

    def nextLevel(self,click):
    ### NIVELES DE DIFICULTAD ### REVISAR, NO FUNCIONA
        if  self.score>200:
            self.level+=1 
            self.asteroid=Asteroid(randint(780,840),randint(10,550))
            self.asteroid.speed=(randint(ASTEROID_MIN_SPEED*2,ASTEROID_MAX_SPEED*self.level))
            self.asteroidsGroup.add(self.asteroid)
            self.new_asteroids_number+=1

    def update_game(self,click):
    ### ACTUALIZA PANTALLA Y ELEMENTOS DEL JUEGO ###
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
    ### BUCLE DE JUEGO, DEFINE QUÉ SUCEDE EN EL JUEGO ###    
        self.handleEvents()
        self.rocket.crash_check(self.asteroidsGroup)

        self.number_of_asteroids = len(self.asteroidsGroup)

        if self.number_of_asteroids<self.simultaneus_asteroids:
            self.newAsteroid(click)
        
        if  self.new_asteroids_number>self.simultaneus_asteroids:
            self.score+=self.new_asteroids_number*10
            self.scoreboard_data=self.font_small.render(str(self.score),True,TEXT_WEAK_COLOUR)
            
        self.update_game(click)

    def mainloop(self):
    ### BUCLE PRINCIPAL ###
        self.playing=True
        self.handleEvents()
        while self.playing:
            click=self.clock.tick(FPS)

            if self.rocket.crash_check(self.asteroidsGroup):
                self.gameOver(click) 
            else:
                self.game_loop(click)
                
            pg.display.flip()

    def quit(self):
    ### SALIR ###
        print ("Gracias por jugar a",GAME_NAME)
        sys.exit(0)

if __name__=='__main__':
    exit_game=False
    click=clock.tick(FPS)
    game=Game()
   
    pg.font.init()
    screen=pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    background_image=pg.transform.scale(pg.image.load(BACKGROUND_IMAGE),(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(background_image, (0, 0))
    
    font_big=pg.font.Font(FONT,FONT_SIZE_BIG)#
    game_name= font_big.render(GAME_NAME,True,TEXT_STRONG_COLOUR)
    screen.blit(game_name,(100, 150))
    
    options=[
        ("Jugar",game.mainloop),
        ("Instrucciones",game.instructions),
        ("Créditos",game.credits),
        ("Salir",game.quit)
    ]
    menu=Menu(options)

    while not exit_game:
        for event in pg.event.get():
            if event.type==QUIT:
                exit_game=True
        screen.blit(background_image,(0,0))
        screen.blit(game_name,(100, 150))
        menu.update()
        menu.print(screen)

        pg.display.flip()
        pg.time.delay(10)
 