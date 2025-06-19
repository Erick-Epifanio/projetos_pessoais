import tkinter as tk

class main:
    def  __init__(self):
        self.root = tk.Tk()
    
    def assets(self):
        self.root.geometry("600x400")
        self.root.resizable(False, False)
    def run(self):
        self.root.mainloop

win = main()
win.assets()
win.run()