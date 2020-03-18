from Display.SpritesHandler import *

spritesHandler = SpritesHandler()

pos = (0,0)

running = True
while running:
    spritesHandler.displaySprite("bg.png",(0,0))
    spritesHandler.displaySprite("player.png",pos)

    keys=pygame.key.get_pressed()
    print(keys)
    if keys[pygame.K_w]:
        pos = (pos[0],pos[1]-1)
    if keys[pygame.K_s]:
        pos = (pos[0],pos[1]+1)
    if keys[pygame.K_a]:
        pos = (pos[0]-1,pos[1])
    if keys[pygame.K_d]:
        pos = (pos[0]+1,pos[1])

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.unicode)
        if event.type == pygame.QUIT:
            running = False
    spritesHandler.drawFrame()

pygame.quit()
