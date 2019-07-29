from model import model
from view import view, buttons
import numpy as np

class controller():
    def __init__(self, root):
        self.model = model()
        self.view1 = view(root)
        self.view2 = buttons(self.view1, self.model.color) 
        self.view2.bw.config(command=self.white_pressed)
        self.view2.bb.config(command=self.black_pressed)

    def color_changed(self, color):
        self.view2.set_color(color)

    def white_pressed(self):
        self.color_changed(self.model.recieve_data([1, 0]))

    def black_pressed(self):
        self.color_changed(self.model.recieve_data([0, 1]))