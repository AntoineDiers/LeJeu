from GlobalVariables import *
from Display.SpritesHandler import *
from Display.CameraHandler import *
from enum import Enum

class CollisionDirection(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Floor:
    def __init__(self,pos):
        self.pos = pos
        self.collisionDirections = [CollisionDirection.UP]
    def render(self,spriteHandler):
        spriteHandler.displaySprite("tile.png",self.pos)

class TerrainHandlerSingleton:
    class TerrainHandler:
        def __init__(self):
            self.tiles = {}
            self.cameraHandler = CameraHandlerSingleton(None)
            self.spriteHandler = SpritesHandlerSingleton()
        def generate(self, width):
            for i in range(width):
                self.tiles[i] = {}
                for j in range(1):
                    self.tiles[i][j] = Floor((i,j))
        def render(self):
            cameraPos = self.cameraHandler.getPos()
            xmin = int(cameraPos[0] - screenWidth/2 - 1)
            xmax = int(cameraPos[0] + screenWidth/2 + 1)
            for x in range(xmin,xmax):
                if x in self.tiles:
                    for y in self.tiles[x]:
                        self.tiles[x][y].render(self.spriteHandler)

        def getCollisions(self,pos,width,height):
            res = []
            xmin = int(pos[0] - width / 2.0 - 1)
            xmax = int(pos[0] + width / 2.0 + 1)
            for x in range(xmin,xmax):
                if x in self.tiles:
                    for y in self.tiles[x]:
                        xRel = pos[0] - x
                        yRel = pos[1] - y
                        xRelMax = width / 2.0 + 0.5
                        yRelMax = height / 2.0 + 0.5
                        if abs(xRel) < xRelMax and abs(yRel) < yRelMax:
                            collisionDirection = None
                            xPenetration = abs(abs(xRel) - xRelMax)
                            yPenetration = abs(abs(yRel) - yRelMax)
                            if xPenetration > yPenetration:
                                if yRel > 0:
                                    collisionDirection = CollisionDirection.UP
                                else:
                                    collisionDirection = CollisionDirection.DOWN
                            else:
                                if xRel > 0:
                                    collisionDirection = CollisionDirection.RIGHT
                                else:
                                    collisionDirection = CollisionDirection.LEFT
                            res.append((self.tiles[x][y],collisionDirection))
            return res


    instance = None
    def __init__(self):
        if not TerrainHandlerSingleton.instance:
            TerrainHandlerSingleton.instance = TerrainHandlerSingleton.TerrainHandler()

    def generate(self, width):
        TerrainHandlerSingleton.instance.generate(width)
    def render(self):
        TerrainHandlerSingleton.instance.render()
    def getCollisions(self,pos,width,height):
        return TerrainHandlerSingleton.instance.getCollisions(pos,width,height)
