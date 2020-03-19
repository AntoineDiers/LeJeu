from Display.SpritesHandler import *
from Terrain.Terrain import *
from time import *

spritesHandler = SpritesHandlerSingleton()

pos = (screenWidthPix/2,screenHeightPix/2)
angle = 0

terrain = Terrain()
terrain.generate(100)

cameraPos = (0,0)

running = True
nFrames = 0
t0 = time()
while running:

    nFrames+=1

    spritesHandler.displaySprite("bg.png",(0,0))

    terrain.render(cameraPos)
    spritesHandler.displaySprite("player.png",pos,angle)

    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cameraPos = (cameraPos[0],cameraPos[1]+0.01)
    if keys[pygame.K_s]:
        cameraPos = (cameraPos[0],cameraPos[1]-0.01)
    if keys[pygame.K_a]:
        cameraPos = (cameraPos[0]-0.01,cameraPos[1])
    if keys[pygame.K_d]:
        cameraPos = (cameraPos[0]+0.01,cameraPos[1])

    if keys[pygame.K_q]:
        angle += 0.2
    if keys[pygame.K_e]:
        angle -= 0.2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    spritesHandler.drawFrame()

    t1 = time()
    if t1 - t0 > 1:
        print("fps : ", nFrames / (t1 - t0))
        t0 = time()
        nFrames = 0



pygame.quit()
