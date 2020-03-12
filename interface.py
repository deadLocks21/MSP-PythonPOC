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
        self.nomDb.set("Connexion à la base de données {}".format(self.dB.getName()))
        self.nomTable = StringVar()


        # Interface graphique
        self.l_nomDB = Label(self.root, textvariable=self.nomDb)
        self.l_nomDB.place(anchor='n', width=800, height=50, x=400, y=10)

        self.e_nomTable = Entry(self.root, textvariable=self.nomTable, background="white", justify="center")
        self.e_nomTable.place(anchor='center', width=600, height=35, x=400, y=85)

        self.b_chercherTable = Button(self.root, text="Voir contenu de la table", command=self.b_affichage)
        self.b_chercherTable.place(anchor='n', width=250, height=35, x=400, y=110)

        self.l_tableFausse = Label(self.root, text="La table que tu m'as donné ne marche pas ...", fg='red')
        # self.l_tableFausse.place(anchor='n', width=250, height=35, x=400, y=150)

        # self.f_res = Frame(self.root, background="white", highlightbackground="black", bd=2)
        self.f_results = VerticalScrolledFrame(self.root)
        self.f_results.place(anchor="n", width=700, height=400, x=400, y=190)

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
                buttons.append(ButtonElDB(self.f_results.interior, contenu[i], self.nomTable.get()).getBt())
                buttons[-1].pack()


class ButtonElDB:
    def __init__(self, root, t, tableName):
        self.r = root
        self.t = t
        self.tableName = tableName

        self.bt = Button(self.r,text=self.textBt(),width=94, height=2, relief="flat", command=self.affInfo)

    def setTableName(self, name):
        self.tableName = name

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
        def add():
            data = ""
            listData = recupInfos()

            for i in range(len(keyName)):
                try:
                    listData[i] = int(listData[i])
                except ValueError:
                    pass


                if type(listData[i]) == str:
                    laData = "'{}'".format(listData[i])
                else:
                    laData = listData[i]

                data += "{}, ".format(laData)

            data = data[:len(data)-2]

            print(data)

            dB = DbClass()
            dB.ajoutLigne(self.tableName,data)

        def modifier():
            data = ""
            listData = recupInfos()

            for i in range(len(keyName)):
                if type(listData[i]) == str:
                    laData = "'{}'".format(listData[i])
                else:
                    laData = listData[i]

                data += "{} = {}, ".format(keyName[i], laData)

            data = data[:len(data)-2]

            print(data)

            dB = DbClass()
            dB.modifierLigne(self.tableName,data, "{} = {}".format(keyName[0], c1.getEntry()))

        def supprimer():
            dB = DbClass()

            dB.supprimerLigne(self.tableName, "{} = {}".format(keyName[0], c1.getEntry()))
            root.destroy()



        def remplirCanvas():
            t = self.t
            lK = len(keyName)
            print(lK)

            try:
                if lK >= 1:
                    c1.setNom(keyName[0])
                    c1.setData(t[keyName[0]])
                    c1.aff()

                if lK >= 2:
                    c2.setNom(keyName[1])
                    c2.setData(t[keyName[1]])
                    c2.aff()

                if lK >= 3:
                    c3.setNom(keyName[2])
                    c3.setData(t[keyName[2]])
                    c3.aff()

                if lK >= 4:
                    c4.setNom(keyName[3])
                    c4.setData(t[keyName[3]])
                    c4.aff()

                if lK >= 5:
                    c5.setNom(keyName[4])
                    c5.setData(t[keyName[4]])
                    c5.aff()

                if lK >= 6:
                    c6.setNom(keyName[5])
                    c6.setData(t[keyName[5]])
                    c6.aff()

                if lK >= 7:
                    c7.setNom(keyName[6])
                    c7.setData(t[keyName[6]])
                    c7.aff()

                if lK >= 8:
                    c8.setNom(keyName[7])
                    c8.setData(t[keyName[7]])
                    c8.aff()
            except IndexError:
                pass

        def recupInfos():
            res = []

            if lK >= 1:
                res.append(c1.getEntry())

            if lK >= 2:
                res.append(c2.getEntry())

            if lK >= 3:
                res.append(c3.getEntry())

            if lK >= 4:
                res.append(c4.getEntry())

            if lK >= 5:
                res.append(c5.getEntry())

            if lK >= 6:
                res.append(c6.getEntry())

            if lK >= 7:
                res.append(c7.getEntry())

            if lK >= 8:
                res.append(c8.getEntry())

            return res

        root = Tk()
        root.title('Data')
        root.geometry("600x400")

        keyName = self.getKeyName()

        champs = VerticalScrolledFrame(root)
        champs.place(anchor="n", width=500, height=340, x=300, y=10)

        add = Button(root, text="Ajouter", command=add)
        add.place(anchor="n", width=100, height=35, x=150, y=355)

        supprimer = Button(root, text="Supprimer", command=supprimer)
        supprimer.place(anchor="n", width=100, height=35, x=300, y=355)

        modifier = Button(root, text="Modifier", command=modifier)
        modifier.place(anchor="n", width=100, height=35, x=450, y=355)

        t = self.t
        lK = len(keyName)

        if lK >= 1:
            c1 = CanvasDeChamp(champs)

        if lK >= 2:
            c2 = CanvasDeChamp(champs)

        if lK >= 3:
            c3 = CanvasDeChamp(champs)

        if lK >= 4:
            c4 = CanvasDeChamp(champs)

        if lK >= 5:
            c5 = CanvasDeChamp(champs)

        if lK >= 6:
            c6 = CanvasDeChamp(champs)

        if lK >= 7:
            c7 = CanvasDeChamp(champs)

        if lK >= 8:
            c8 = CanvasDeChamp(champs)

        remplirCanvas()

        root.mainloop()



class CanvasDeChamp:
    def __init__(self, root):
        self.root = root

        self.data = StringVar()

        self.canvas = Canvas(self.root.interior, highlightthickness=0)
        self.n = Label(self.canvas, text="self.nom.get")
        self.n.grid(row=0, column=0)
        Label(self.canvas, text=" ").grid(row=1, column=0)
        self.champ = Entry(self.canvas,textvariable=self.data, width=50, justify="center")
        self.champ.grid(row=0, column=1)


    def modifNom(self, nom):
        return "{} :".format(nom)


    def getValue(self):
        return self.champ.get()

    def setNom(self, nom):
        self.n.config(text=nom)

    def setData(self, data):
        self.champ.insert(0, data)

    def aff(self):
        self.canvas.pack()

    def getEntry(self):
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
