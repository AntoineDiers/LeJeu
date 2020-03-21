import numpy as np

screenWidthPix = 1920
screenHeightPix = 1080

pixelsPerTile = 24
screenHeight = screenHeightPix / pixelsPerTile
screenWidth = screenWidthPix / pixelsPerTile

playerHitBoxPix = np.array([-33,33,-55,55])
playerHitBox = playerHitBoxPix / pixelsPerTile

tilePercentageForCollision = 10

LEFT_CLICK = 1
RIGHT_CLICK = 3