import tkinter as tk
from colormap import rgb2hex

class view(tk.Toplevel):
    def __init__(self, master): 
        tk.Toplevel.__init__(self, master)

        c = tk.Canvas(self, bg='black', height=500, width=600).pack()

class buttons(tk.Toplevel):
    def __init__(self, master, color): 
        tk.Toplevel.__init__(self, master)
        self.buttonframe = tk.Frame(self)
        font = ('Helvetica', '30')
        print(color)
        hex = rgb2hex(color[0], color[1], color[2])
        self.bw = tk.Button(self.buttonframe, width=10, height=2, bg=hex, fg='white', text='white', font=font)
        self.bw.grid(row=0, column=0)
        self.bb = tk.Button(self.buttonframe, width=10, height=2, bg=hex, fg='black', text='black', font=font)
        self.bb.grid(row=0, column=1)
        self.buttonframe.pack()

