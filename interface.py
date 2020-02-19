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

        self.dB.connect()

        self.root.mainloop()

    def b_affichage(self):
        exist = self.dB.existanceTable(self.nomTable.get())
        self.f_results.destroy()
        self.f_results = VerticalScrolledFrame(self.root)
        self.f_results.place(anchor="n", width=700, height=400, x=400, y=190)

        if not exist:
            self.l_tableFausse.place(anchor='n', width=250, height=35, x=400, y=150)
            self.nomTable.set("")
        else:
            self.l_tableFausse.place_forget()

            contenu = self.dB.contenuTable(self.nomTable.get())

            buttons = []
            for i in range(len(contenu)):
                buttons.append(ButtonElDB(self.f_results.interior, contenu[i]).getBt())
                buttons[-1].pack()


class ButtonElDB:
    def __init__(self, root, t):
        self.r = root
        self.t = t

        self.bt = Button(self.r,text=self.textBt(),width=94, height=2, relief="flat", command=self.affInfo)



    def fermer(self):
        self.bt.pack_forget()

    def getBt(self):
        return self.bt

    def textBt(self):
        t = self.t
        keyName = self.getKeyName()

        nbCar = int( 94 / len(keyName) )

        text = ""

        for i in range(len(keyName)):
            if nbCar - 4 < len(str(t[keyName[i]])):
                chain = " {}.. ".format(str(t[keyName[i]]))
            else:
                chain = " " + str(t[keyName[i]])

                while len(chain) <= nbCar:
                    chain += " "

            text += chain

        return text

    def getKeyName(self):
        t = self.t
        keyName = []

        for key in t.keys():
            keyName.append(key)

        return keyName

    def affInfo(self):
        def modifier():
            print(c1.getValue())

        root = Tk()
        root.title('Data')
        root.geometry("600x400")

        keyName = self.getKeyName()

        champs = VerticalScrolledFrame(root)
        champs.place(anchor="n", width=500, height=340, x=300, y=10)

        add = Button(root, text="Ajouter")
        add.place(anchor="n", width=100, height=35, x=150, y=355)

        supprimer = Button(root, text="Supprimer")
        supprimer.place(anchor="n", width=100, height=35, x=300, y=355)

        modifier = Button(root, text="Modifier", command=modifier)
        modifier.place(anchor="n", width=100, height=35, x=450, y=355)




        # c1 =

        for i in range(8):
            CanvasDeChamp(champs, "test")




        # buttons = []
        # for i in range(len(contenu)):
        #     buttons.append(ButtonElDB(self.f_results.interior, contenu[i]).getBt())
        #     buttons[-1].pack()



        root.mainloop()



class CanvasDeChamp:
    def __init__(self, root, nom):
        self.root = root

        nom = self.modifNom(nom)

        self.canvas = Canvas(self.root.interior)
        Label(self.canvas, text=nom).grid(row=0, column=0)
        Label(self.canvas, text=" ").grid(row=1, column=0)
        self.champ = Entry(self.canvas)
        self.champ.grid(row=0, column=1)

        self.canvas.pack()


    def modifNom(self, nom):
        return "{} :".format(nom)


    def getValue(self):
        return self.champ.get()


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
