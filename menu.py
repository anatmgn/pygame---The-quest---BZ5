import pygame as pg
from pygame.locals import *

from main import *
from entities import *
from constants import *

class Menu: ###EN DESARROLLO###
    def __init__(self,options):
        self.options=options
        self.font=pg.font.Font(FONT,FONT_SIZE_MEDIUM)
        #self.selected=False #Modificado por el siguiente
        self.selected=0
        self.total=len(self.options)
        self.pressed=False

    def update(self):
        key=pg.key.get_pressed()

        if not self.pressed:
            if key[K_UP]:
                self.selected-=1
            elif key[K_DOWN]:
                self.selected+=1
            elif key[K_RETURN]:
                title,function=self.options[self.selected]
                print ("Selecciona la opción '%s'." %(title))
                function()###
        
        if self.selected<0:
            self.selected=0
        elif self.selected>self.total-1:
            self.selected=self.total-1

        self.pressed=key[K_UP] or key[K_DOWN] or key[K_RETURN]

    def print(self,screen):
        total=self.total
        index=0
        option_height=30#
        x=200#
        y=300#

        for (title,function) in self.options:
            if index==self.selected:
                colour=TEXT_STRONG_COLOUR
            else:
                colour=TEXT_WEAK_COLOUR

            image=self.font.render(titulo,1,colour)
            position=(x,y+option_height*index)
            index+=1
            screen.blit(image,position)
            