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

        self.c_res = Canvas(self.root, background="white", highlightbackground="black", bd=2)
        self.c_res.place(anchor="n", width=700, height=400, x=400, y=190)


        self.dB.connect()

        self.root.mainloop()

    def b_affichage(self):
        exist = self.dB.existanceTable(self.nomTable.get())

        if not exist:
            self.l_tableFausse.place(anchor='n', width=250, height=35, x=400, y=150)
            self.nomTable.set("")
        else:
            self.l_tableFausse.place_forget()
