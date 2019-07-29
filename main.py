from controller import controller
import view
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    app = controller(root)
    root.mainloop()