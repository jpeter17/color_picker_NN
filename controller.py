from model import model
from view import view
import numpy as np

class controller():
    def __init__(self, root):
        self.model = model()
        self.view = view(root, self.model.color)
        self.view.bw.config(command=self.white_pressed)
        self.view.bb.config(command=self.black_pressed)

    def color_changed(self, color):
        self.view.set_color(color)

    def white_pressed(self):
        self.color_changed(self.model.recieve_data([1, 0]))

    def black_pressed(self):
        self.color_changed(self.model.recieve_data([0, 1]))