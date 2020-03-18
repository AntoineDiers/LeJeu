import pygame

screenWidth = 1920
screenHeight = 1080

class Sprite:
    def __init__(self, filename):
        self.usedThisFrame = True
        try:
            self.image = pygame.image.load("../assets/"+filename).convert_alpha()
            self.isValid = True
        except:
            self.isValid = False

class SpritesHandler:
    def __init__(self):
        self.loadedSprites = {}
        pygame.init()
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))#,pygame.FULLSCREEN)

    def displaySprite(self, filename, pos, angle = 0, size = None, alpha = None):

        if self.screen is not None:

            # Load the sprite
            sprite = None
            if filename in self.loadedSprites:
                sprite = self.loadedSprites.get(filename)
            else:
                sprite = Sprite(filename)
                if sprite.isValid:
                    self.loadedSprites[filename] = sprite
                else:
                    sprite = None

            if sprite is not None:


                image = sprite.image

                # TODO : rotation, alpha, size
                if size is not None:
                    image = pygame.transform.scale(image,size)

                self.screen.blit(image,pos)
                self.loadedSprites[filename].usedThisFrame = True

    def drawFrame(self):
        pygame.display.flip()
        for sprite in self.loadedSprites:
            if not self.loadedSprites[sprite].usedThisFrame:
                self.loadedSprites.pop(sprite)
            else:
                self.loadedSprites[sprite].usedThisFrame = False





