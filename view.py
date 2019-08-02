import tkinter as tk
from colormap import rgb2hex

class view(tk.Toplevel):
    def __init__(self, master, color, guess, confidence): 
        tk.Toplevel.__init__(self, master)
        self.c = tk.Canvas(self, bg='black', height=500, width=600)
        self.guess = guess
        buttonframe = tk.Frame(self)
        font = ('Helvetica', '30')
        self.hex = rgb2hex(color[0], color[1], color[2])
        self.bw = tk.Button(buttonframe, width=10, height=2, bg=self.hex, fg='white', text='white', font=font)
        self.bw.grid(row=0, column=0)
        self.bb = tk.Button(buttonframe, width=10, height=2, bg=self.hex, fg='black', text='black', font=font)
        self.bb.grid(row=0, column=1)
        txt = 'Confidence: ' + str(confidence)
        self.confidence = self.c.create_text(300, 100, fill = 'white', font='Times 20', text=txt)
        if self.guess == 1:
            self.guess_oval = self.c.create_oval(170, 450, 210, 490, fill='white')
        elif self.guess == 0:
            self.guess_oval = self.c.create_oval(400, 450, 440, 490, fill='white')
        self.c.pack()
        buttonframe.pack()

    def update(self, data):
        print(data)
        self.hex = rgb2hex(data[0][0], data[0][1], data[0][2])
        self.bw.config(bg=self.hex)
        self.bb.config(bg=self.hex)
        txt = 'Confidence: ' + str(data[1])
        self.c.itemconfigure(self.confidence, text=txt)
        if data[2] == 1 and self.guess == 0:
            self.c.move(self.guess_oval, -200, 0)
            self.guess = 1
        elif data[2] == 0 and self.guess == 1:
            self.c.move(self.guess_oval, 200, 0)
            self.guess = 0 
