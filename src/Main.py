from Display.SpritesHandler import *
from Display.CameraHandler import *
from Terrain.Terrain import *
from EventsHandler import *
from Player.Player import *
from time import *
from Physics.Physics import *

pygame.init()

player = Player([10,3])
cameraHandler = CameraHandlerSingleton(None)
spritesHandler = SpritesHandlerSingleton()
eventsHandler = EventsHandlerSingleton()

terrain = TerrainHandlerSingleton()
terrain.generate(1000)

running = True
def quit():
    global running
    running = False

nFrames = 0
t0 = time()


eventsHandler.registerKeyboardCallback(pygame.K_x,quit)
eventsHandler.registerKeyboardCallback(pygame.K_r,player.reset)

while running:

    timeHandler.startNewFrame()
    if timeHandler.getDelta() is not None:

        nFrames+=1
        spritesHandler.displaySprite("bg.png",cameraHandler.getPos())

        player.doStep()
        terrain.render()
        eventsHandler.poll()

        spritesHandler.drawFrame()

        t1 = time()
        if t1 - t0 > 1:
            print("fps : ", nFrames / (t1 - t0))
            t0 = time()
            nFrames = 0



pygame.quit()
