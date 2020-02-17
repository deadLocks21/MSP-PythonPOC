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

        # Objet représentant la DB
        self.dB = DbClass()

        # Variables
        self.nomDb = StringVar()
        self.nomDb.set("Connection à la base de données {}".format(self.dB.getName()))
        self.nomTable = StringVar()

        # Interface graphique
        self.l_nomDB = Label(self.root, textvariable=self.nomDb)
        self.l_nomDB.place(anchor='n', width=800, height=50, x=400, y=10)

        self.e_nomTable = Entry(self.root, textvariable=self.nomTable, background="white", justify="center")
        self.e_nomTable.place(anchor='center', width=600, height=35, x=400, y=85)

        self.b_chercherTable = Button(self.root, text="Voir contenue de la table", command=self.b_affichage)
        self.b_chercherTable.place(anchor='n', width=250, height=35, x=400, y=110)

        self.l_tableFausse = Label(self.root, text="La table que tu m'as donné ne marche pas ...", fg='red')
        # self.l_tableFausse.place(anchor='n', width=250, height=35, x=400, y=150)

        # self.f_res = Frame(self.root, background="white", highlightbackground="black", bd=2)
        self.f_results = VerticalScrolledFrame(self.root)
        self.f_results.place(anchor="n", width=700, height=400, x=400, y=190)

        buttons = []
        for i in range(20):
            buttons.append(ButtonElDB(self.f_results.interior, i).getBt())
            buttons[-1].pack()

        self.dB.connect()

        self.root.mainloop()

    def b_affichage(self):
        exist = self.dB.existanceTable(self.nomTable.get())

        if not exist:
            self.l_tableFausse.place(anchor='n', width=250, height=35, x=400, y=150)
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

    def getBt(self):
        return self.bt


class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

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
