from model import model
from view import view
import numpy as np

class controller():
    def __init__(self, root):
        self.model = model()
        self.model.make_guess()
        self.view = view(root, self.model.color, self.model.guess, self.model.confidence)
        self.view.bw.config(command=self.white_pressed)
        self.view.bb.config(command=self.black_pressed)

    def color_changed(self, data):
        self.view.update(data)

    def white_pressed(self):
        self.color_changed(self.model.recieve_data([1, 0]))

    def black_pressed(self):
        self.color_changed(self.model.recieve_data([0, 1]))