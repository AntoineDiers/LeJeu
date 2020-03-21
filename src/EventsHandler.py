import pygame

class EventsHandlerSingleton:
    class EventsHandler:
        def __init__(self):
            self.pressedKeys=pygame.key.get_pressed()
            self.mousePos = pygame.mouse.get_pos()

            self.keyboardCallbacks = {}
            self.keyboardCallbackId = 0

            self.mouseCallbacks = {}
            self.mouseCallbackId = 0

        def poll(self):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in self.keyboardCallbacks:
                        for callbackId in self.keyboardCallbacks[event.key]:
                            self.keyboardCallbacks[event.key][callbackId]()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button in self.mouseCallbacks:
                        for callbackId in self.mouseCallbacks[event.button]:
                            self.mouseCallbacks[event.button][callbackId](event.pos)

            self.pressedKeys = pygame.key.get_pressed()
            self.mousePos = pygame.mouse.get_pos()

        # Keyboard State
        def isKeyPressed(self,key):
            return self.pressedKeys[key]

        # Mouse State
        def getMousePos(self):
            return self.mousePos

        # Keyboard Callbacks
        def registerKeyboardCallback(self,key,callback):
            if key in self.keyboardCallbacks:
                self.keyboardCallbacks[key][self.keyboardCallbackId] = callback
            else:
                self.keyboardCallbacks[key]={self.keyboardCallbackId:callback}
            self.keyboardCallbackId += 1
            return self.keyboardCallbackId - 1
        def unregisterKeyboardCallback(self,key,keyboardCallbackId):
            if key in self.keyboardCallbacks:
                if keyboardCallbackId in self.keyboardCallbacks[key]:
                    self.keyboardCallbacks[key].pop(keyboardCallbackId)

        # Mouse Callbacks
        def registerMouseCallback(self,button,callback):
            if button in self.mouseCallbacks:
                self.mouseCallbacks[button][self.mouseCallbackId] = callback
            else:
                self.mouseCallbacks[button]={self.mouseCallbackId:callback}
            self.mouseCallbackId += 1
            return self.mouseCallbackId - 1
        def unregisterMouseCallback(self,button,mouseCallbackId):
            if button in self.mouseCallbacks:
                if mouseCallbackId in self.mouseCallbacks[button]:
                    self.mouseCallbacks[button].pop(mouseCallbackId)

    instance = None
    def __init__(self):
        if not EventsHandlerSingleton.instance:
            EventsHandlerSingleton.instance = EventsHandlerSingleton.EventsHandler()

    def poll(self):
        EventsHandlerSingleton.instance.poll()
    def isKeyPressed(self,key):
        return EventsHandlerSingleton.instance.isKeyPressed(key)
    def getMousePos(self):
        return EventsHandlerSingleton.instance.getMousePos()
    def registerKeyboardCallback(self,key,callback):
        return EventsHandlerSingleton.instance.registerKeyboardCallback(key,callback)
    def unregisterKeyboardCallback(self,key,keyboardCallbackId):
        EventsHandlerSingleton.instance.unregisterKeyboardCallback(key,callbackId)
    def registerMouseCallback(self,button,callback):
        return EventsHandlerSingleton.instance.registerMouseCallback(button,callback)
    def unregisterMouseCallback(self,button,mouseCallbackId):
        EventsHandlerSingleton.instance.unregisterMouseCallback(button,callbackId)

















