#!/usr/bin/env python3
# -*- coding : utf-8 -*-

from tkinter import *
from bdd import *


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title('Python POC')  # Nom de la fenêtre
        self.root.geometry("400x200")  # Taille de la fenêtre
        self.root.resizable(False, False)  # Ne pas redimensionner fenêtre

        # Objet représentant la DB
        self.dB = DbClass()

        # Variables
        self.nomDb = StringVar()
        self.nomDb.set("Connection à la base de données {}".format(self.dB.getName()))
        self.nomTable = StringVar()




        # Interface graphique
        self.l_nomDB = Label(self.root, textvariable=self.nomDb)
        self.l_nomDB.place(anchor='nw', width=400, height=50, x=0, y=10)

        self.e_nomTable = Entry(self.root, textvariable=self.nomTable, background="white", justify="center")
        self.e_nomTable.place(anchor='center', width=300, height=35, x=200, y=85)

        self.b_chercherTable = Button(self.root, text="Voir contenue de la table", command=self.b_affichage)
        self.b_chercherTable.place(anchor='n', width=200, height=35, x=200, y=150)

        self.l_tableFausse = Label(self.root, text="La table que tu m'as donné ne marche pas ...", fg='red')
        # self.l_tableFausse.place(anchor='n', width=250, height=35, x=400, y=150)

        self.dB.connect()

        self.root.mainloop()

    def b_affichage(self):
        exist = self.dB.existanceTable(self.nomTable.get())

        # ctn = self.dB.contenuTable(self.nomTable.get())
        # print(ctn)

        if not exist:
            self.l_tableFausse.place(anchor='n', width=250, height=35, x=200, y=110)
            self.nomTable.set("")
        else:
            self.l_tableFausse.place_forget()


class ButtonElDB:
    def __init__(self, root, t):
        self.root = root

        self.bt = Button(self.root, text=t, command=self.fermer)
        self.bt.pack()

    def fermer(self):
        self.bt.pack_forget()


class ScrollableCanvas(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        canvas = Canvas(self, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 500, 500))

        vbar = Scrollbar(self, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview)

        canvas.config(width=200, height=200)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=LEFT, expand=True, fill=BOTH)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)
