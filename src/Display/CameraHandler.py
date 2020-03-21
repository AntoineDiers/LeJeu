class CameraHandlerSingleton:
    class CameraHandler:
        def __init__(self,player):
            self.player = player
            self.pos = player.pos
        def update(self):
            self.pos = self.player.pos
        def getPos(self):
            return self.pos

    instance = None
    def __init__(self,player):
        if not CameraHandlerSingleton.instance:
            CameraHandlerSingleton.instance = CameraHandlerSingleton.CameraHandler(player)

    def update(self):
        CameraHandlerSingleton.instance.update()
    def getPos(self):
        return CameraHandlerSingleton.instance.getPos()

