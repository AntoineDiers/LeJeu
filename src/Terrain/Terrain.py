from GlobalVariables import *
from Display.SpritesHandler import *

class Floor:
    def __init__(self):
        pass
    def render(self,x,y,cam_x,cam_y):
        spriteHandler = SpritesHandlerSingleton()
        xOnScreen = screenWidthPix/2 + pixelsPerTile * (0.5 + x - cam_x)
        yOnScreen = screenHeightPix/2 - pixelsPerTile * (0.5 + y - cam_y)
        spriteHandler.displaySprite("tile.png",(xOnScreen,yOnScreen))

class Terrain:
    def __init__(self):
        self.tiles = {}
    def generate(self, width):
        for i in range(width):
            self.tiles[i] = {}
            self.tiles[i][0] = Floor()
    def getTile(x,y):
        if x in self.tiles:
            if y in self.tiles[x]:
                return self.tiles[x][y]
        return None
    def render(self,cameraPos):
        xmin = int(cameraPos[0] - screenWidth/2 - 1)
        xmax = int(cameraPos[0] + screenWidth/2 + 1)
        ymin = int(cameraPos[1] - screenHeight/2 - 1)
        ymax = int(cameraPos[1] + screenHeight/2 + 1)
        for x in range(xmin,xmax):
            for y in range(ymin,ymax):
                if x in self.tiles:
                    if y in self.tiles[x]:
                        self.tiles[x][y].render(x,y,cameraPos[0],cameraPos[1])