from Display.SpritesHandler import *
from Terrain.Terrain import *
from EventsHandler import *
from Player.Player import *
from time import *

spritesHandler = SpritesHandlerSingleton()

pos = (screenWidthPix/2,screenHeightPix/2)
angle = 0

terrain = Terrain()
terrain.generate(1000)

player = Player((300,300))

cameraPos = (0,0)

eventsHandler = EventsHandlerSingleton()


print(screenWidth)

running = True
def quit():
    global running
    running = False

nFrames = 0
t0 = time()


eventsHandler.registerKeyboardCallback(pygame.K_x,quit)

while running:

    nFrames+=1



    spritesHandler.displaySprite("bg.png",(0,0))

    player.doStep()

    terrain.render(cameraPos)


    eventsHandler.poll()

    if eventsHandler.isKeyPressed(pygame.K_w):
        cameraPos = (cameraPos[0],cameraPos[1]+0.03)
    if eventsHandler.isKeyPressed(pygame.K_s):
        cameraPos = (cameraPos[0],cameraPos[1]-0.03)
    if eventsHandler.isKeyPressed(pygame.K_a):
        cameraPos = (cameraPos[0]-0.03,cameraPos[1])
    if eventsHandler.isKeyPressed(pygame.K_d):
        cameraPos = (cameraPos[0]+0.03,cameraPos[1])
    if eventsHandler.isKeyPressed(pygame.K_q):
        angle += 0.2
    if eventsHandler.isKeyPressed(pygame.K_e):
        angle -= 0.2

    spritesHandler.drawFrame()

    t1 = time()
    if t1 - t0 > 1:
        print("fps : ", nFrames / (t1 - t0))
        t0 = time()
        nFrames = 0



pygame.quit()
