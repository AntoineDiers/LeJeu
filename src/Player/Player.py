from GlobalVariables import *
from math import *
from EventsHandler import *
from Display.SpritesHandler import *

class Player:
    def __init__(self,pos):
        self.pos = pos
        self.vel = (0,0)
        self.angle = 0
        self.eventsHandler = EventsHandlerSingleton()
        self.spritesHandler = SpritesHandlerSingleton()

    def doStep(self):
        mousePos = self.eventsHandler.getMousePos()
        self.angle = atan2(- mousePos[1] + self.pos[1],mousePos[0] - self.pos[0])

        self.render()



    def render(self):
        self.spritesHandler.displaySprite("player.png",self.pos,self.angle)