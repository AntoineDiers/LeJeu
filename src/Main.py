from Display.SpritesHandler import *

spritesHandler = SpritesHandlerSingleton()

pos = (0,0)
angle = 0

running = True
while running:
    spritesHandler.displaySprite("bg.png",(0,0))
    spritesHandler.displaySprite("player.png",pos,angle)

    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos = (pos[0],pos[1]-1)
    if keys[pygame.K_s]:
        pos = (pos[0],pos[1]+1)
    if keys[pygame.K_a]:
        pos = (pos[0]-1,pos[1])
    if keys[pygame.K_d]:
        pos = (pos[0]+1,pos[1])

    if keys[pygame.K_q]:
        angle += 0.2
    if keys[pygame.K_e]:
        angle -= 0.2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    spritesHandler.drawFrame()

pygame.quit()
