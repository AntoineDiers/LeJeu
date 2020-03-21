from GlobalVariables import *
from math import *
from EventsHandler import *
from Display.SpritesHandler import *
from Physics.Physics import *

class Player:
    def __init__(self,pos):

        self.startPos = [pos[0],pos[1]]

        # Physics
        self.pos = pos
        self.vel = [0,0]
        self.force = [0,0]
        self.angle = 0
        self.mass = 200
        self.airResistance = 10
        self.width = 2
        self.height = 4

        self.cameraHandler = CameraHandlerSingleton(self)
        self.eventsHandler = EventsHandlerSingleton()
        self.eventsHandler.registerMouseCallback(LEFT_CLICK,self.shoot)
        self.eventsHandler.registerKeyboardCallback(pygame.K_SPACE,self.jump)
        self.spritesHandler = SpritesHandlerSingleton()

        # Speed
        self.ms = 20

        # Jump
        self.nMaxJumps = 1
        self.availableJumps = 0
        self.jumpSpeed = 120

    def reset(self):
        self.pos[0] = self.startPos[0]
        self.pos[1] = self.startPos[1]
        self.vel = [0,0]
        self.force = [0,0]

    def onTerrainCollision(self,object):
        limitAngle = atan2(self.height,self.width)
        angleToObject = atan2(object.pos[1] - self.pos[1],object.pos[0] - self.pos[0])
        angleToObject = angleToObject % (2*pi)
        if angleToObject > pi:
            angleToObject = angleToObject - 2*pi
        if angleToObject < - limitAngle and angleToObject > - pi + limitAngle:
            self.availableJumps = self.nMaxJumps


    def shoot(self,mousePos):
        print("pewpew")

    def jump(self):
        if self.availableJumps > 0:
            self.vel[1] += self.jumpSpeed
            self.availableJumps -= 1

    def doStep(self):
        mousePos = self.eventsHandler.getMousePos()
        cameraPos = self.cameraHandler.getPos()

        self.force[0] = 0
        if self.eventsHandler.isKeyPressed(pygame.K_d):
            self.force[0] += self.ms * self.airResistance * self.mass;
        if self.eventsHandler.isKeyPressed(pygame.K_a):
            self.force[0] -= self.ms * self.airResistance * self.mass;

        playerPosOnScreenX = screenWidthPix/2 + (self.pos[0] - cameraPos[0]) * pixelsPerTile
        playerPosOnScreenY = screenHeightPix/2 - (self.pos[1] - cameraPos[1]) * pixelsPerTile

        self.angle = atan2(- mousePos[1] + playerPosOnScreenY,mousePos[0] - playerPosOnScreenX)
        applyPhysics(self)

        self.render()

    def render(self):
        self.spritesHandler.displaySprite("player.png",self.pos,self.angle)