from Physics.TimeHandler import *
from Terrain.Terrain import *

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def applyPhysics(object):

    terrainHandler = TerrainHandlerSingleton()

    dt = timeHandler.getDelta()
    object.vel[0] += dt * (object.force[0] / object.mass - object.vel[0] * object.airResistance)
    object.vel[1] += dt * (object.force[1] / object.mass - object.mass - object.vel[1] * object.airResistance)

    object.pos[0] += dt * object.vel[0]
    object.pos[1] += dt * object.vel[1]

    collisions = terrainHandler.getCollisions(object.pos,object.width,object.height)
    for collision in collisions:
        tile = collision[0]
        object.onTerrainCollision(tile)
        direction = collision[1]
        if direction in tile.collisionDirections:
            if direction == CollisionDirection.UP:
                object.pos[1] = tile.pos[1] + 0.5 + object.height / 2.0
                object.vel[1] = max(object.vel[1],0)
            elif direction == CollisionDirection.DOWN:
                object.pos[1] = tile.pos[1] - 0.5 - object.height / 2.0
                object.vel[1] = min(object.vel[1],0)
            elif direction == CollisionDirection.RIGHT:
                object.pos[0] = tile.pos[0] + 0.5 + object.width / 2.0
                object.vel[0] = max(object.vel[0],0)
            elif direction == CollisionDirection.LEFT:
                object.pos[0] = tile.pos[0] + 0.5 + object.width / 2.0
                object.vel[0] = min(object.vel[0],0)