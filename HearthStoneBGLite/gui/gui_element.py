
from renderer import Renderer

class GUI_Element():
    def __init__(self):
        Renderer.addCallableToLoop(self.draw)
        self.subscribe()
    def kill(self):
        Renderer.removeCallableFromLoop(self.draw)
        self.unsubscribe()
    def restore(self):
        Renderer.addCallableToLoop(self.draw)
        self.subscribe()
    def draw(self, dt):
        raise NotImplementedError("Must override draw()")
    def subscribe(self):
        raise NotImplementedError("Must override subscribe()")
