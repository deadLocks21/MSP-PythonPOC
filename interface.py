#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from tkinter import *
from bdd import *


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title('Python POC')  # Nom de la fenêtre
        self.root.geometry("800x600")  # Taille de la fenêtre
        self.root.resizable(False, False)  # Ne pas redimensionner fenêtre

        myDb = DbClass()
        myDb.connect()

        self.root.mainloop()
