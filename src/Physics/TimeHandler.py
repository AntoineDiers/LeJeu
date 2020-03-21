from time import *

class TimeHandlerSingleton:
    class TimeHandler:
        def __init__(self):
            self.lastFrameTime = None
            self.currentFrameTime = None
        def getTime(self):
            return self.currentTime
        def startNewFrame(self):
            self.lastFrameTime = self.currentFrameTime
            self.currentFrameTime = time()
        def getDelta(self):
            if (self.currentFrameTime is not None) and (self.lastFrameTime is not None):
                res = self.currentFrameTime - self.lastFrameTime
                if res > 0:
                    return res
            return None

    instance = None
    def __init__(self):
        if not TimeHandlerSingleton.instance:
            TimeHandlerSingleton.instance = TimeHandlerSingleton.TimeHandler()

    def getTime(self):
        return TimeHandlerSingleton.instance.getTime()
    def startNewFrame(self):
        TimeHandlerSingleton.instance.startNewFrame()
    def getDelta(self):
        return TimeHandlerSingleton.instance.getDelta()

timeHandler = TimeHandlerSingleton()