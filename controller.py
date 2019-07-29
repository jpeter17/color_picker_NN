from model import model
from view import view, buttons
import numpy as np

class controller():
    def __init__(self, root):
        data = []
        color = np.random.choice(range(256), size=3)
        self.model = model()
        self.view1 = view(root)
        self.view2 = buttons(self.view1, color) 
        self.view2.bw.config(command=self.white_pressed)
        self.view2.bb.config(command=self.black_pressed)
        return None

    def white_pressed(self):
        
        return None

    def black_pressed(self):
        return None
