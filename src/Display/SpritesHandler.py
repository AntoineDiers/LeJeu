import pygame
from GlobalVariables import *
from math import *
from Display.CameraHandler import *

class Sprite:
    def __init__(self, filename):
        self.usedThisFrame = True
        try:
            self.image = pygame.image.load("../assets/"+filename).convert_alpha()
            self.isValid = True
        except:
            self.isValid = False

class SpritesHandlerSingleton:
    class SpritesHandler:
        def __init__(self):
            self.loadedSprites = {}
            self.screen = pygame.display.set_mode((screenWidthPix, screenHeightPix))#,pygame.FULLSCREEN)
            self.cameraHandler = CameraHandlerSingleton(None)

        def rotate(self, image, pos, originPos, angle):

            # calcaulate the axis aligned bounding box of the rotated image
            w, h       = image.get_size()
            box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
            box_rotate = [p.rotate(angle) for p in box]
            min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
            max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

            # calculate the translation of the pivot
            pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
            pivot_rotate = pivot.rotate(angle)
            pivot_move   = pivot_rotate - pivot

            # calculate the upper left origin of the rotated image
            origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

            # get a rotated image
            rotated_image = pygame.transform.rotate(image, angle)

            return rotated_image, origin


        def displaySprite(self, filename, pos, angle, size, alpha):

            cameraPos = self.cameraHandler.getPos()
            posOnScreenX = screenWidthPix/2 + (pos[0] - cameraPos[0]) * pixelsPerTile
            posOnScreenY = screenHeightPix/2 - (pos[1] - cameraPos[1]) * pixelsPerTile
            posOnScreen = (posOnScreenX,posOnScreenY)

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

                if size is not None:
                    image = pygame.transform.scale(image,size)
                if angle is not None:
                    image,posOnScreen = self.rotate(image,posOnScreen,image.get_rect().center,180.0 * angle / pi)
                else:
                    posOnScreen = (posOnScreenX - image.get_rect().center[0] ,posOnScreenY - image.get_rect().center[1])

                if posOnScreen[0] < -image.get_rect()[2]:
                    return
                if posOnScreen[0] > screenWidthPix:
                    return
                if posOnScreen[1] < -image.get_rect()[3]:
                    return
                if posOnScreen[1] > screenHeightPix:
                    return

                self.screen.blit(image,posOnScreen)
                self.loadedSprites[filename].usedThisFrame = True

        def drawFrame(self):
            pygame.display.flip()
            spritesToRemove = []
            for sprite in self.loadedSprites:
                if not self.loadedSprites[sprite].usedThisFrame:
                    spritesToRemove.append(sprite)
                else:
                    self.loadedSprites[sprite].usedThisFrame = False
            for sprite in spritesToRemove:
                self.loadedSprites.pop(sprite)
    instance = None
    def __init__(self):
        if not SpritesHandlerSingleton.instance:
            SpritesHandlerSingleton.instance = SpritesHandlerSingleton.SpritesHandler()
    def displaySprite(self, filename, pos, angle = None, size = None, alpha = None):
        SpritesHandlerSingleton.instance.displaySprite(filename, pos, angle, size, alpha)
    def drawFrame(self):
        SpritesHandlerSingleton.instance.drawFrame()






