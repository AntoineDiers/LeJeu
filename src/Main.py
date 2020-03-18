from Display.SpritesHandler import *

spritesHandler = SpritesHandler()

running = True
while running:
    spritesHandler.displaySprite("bg.png",(0,0))
    spritesHandler.displaySprite("player.png",(1000,500))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False
    spritesHandler.drawFrame()

pygame.quit()
