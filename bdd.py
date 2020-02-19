#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import pymysql


class DbClass:
    # def __init__(self, host, name, user, mdp):
    #     self.name = name
    #     self.host = host
    #     self.user = user
    #     self.mdp = mdp

    def __init__(self):
        self.name = "mydb"
        self.host = "127.0.0.1"
        self.user = "root"
        self.mdp = "root"
        # self.con = None

    def getName(self):
        return self.name

    def connect(self):
        try:
            self.con = pymysql.connect(host=self.host,
                                       user=self.user,
                                       password=self.mdp,
                                       db=self.name,
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor)

            print("[DATABASE] Connected")

        except:
            print("[DATABASE] Fail connection")
            self.connect()

    def deco(self):
        self.con.close()
        print("[DATABASE] Disconected")

    def existanceTable(self, table):
        self.connect()

        try:
            with self.con.cursor() as cur:
                cur.execute("SELECT * FROM {} LIMIT 0;".format(table))
            res = True
            txt = "existe."
        except:
            res = False
            txt = "n'existe pas."

        print("[DATABASE] La table {} {}".format(table, txt))
        self.deco()

        return res


    def contenuTable(self, table):
        self.connect()

        try:
            with self.con.cursor() as cur:
                cur.execute("SELECT * FROM {};".format(table))
            res = cur.fetchall()
        except:
            pass

        print("[DATABASE] Récupération contenue table {}".format(table))
        self.deco()

        return res


    def supprimerLigne(self, table, condition):
        self.connect()

        # try:
        #     with self.con.cursor() as cur:
        #         cur.execute("DELETE FROM '{}' WHERE '{}'".format(table, condition))
        # except:
        #     pass

        with self.con.cursor() as cur:
            cur.execute("SET FOREIGN_KEY_CHECKS=0")
            cur.execute("DELETE FROM {} WHERE {}".format(table, condition))
            cur.execute("SET FOREIGN_KEY_CHECKS=1")
            self.con.commit()

        print("[DATABASE] Suppression de {} dans la table {}".format(condition, table))

        self.deco()

    def modifierLigne(self, table, donnes, condition):
        self.connect()

        # try:
        #     with self.con.cursor() as cur:
        #         cur.execute("DELETE FROM '{}' WHERE '{}'".format(table, condition))
        # except:
        #     pass

        with self.con.cursor() as cur:
            cur.execute("SET FOREIGN_KEY_CHECKS=0")
            cur.execute("""UPDATE {} SET {} WHERE {}""".format(table,donnes, condition))
            cur.execute("SET FOREIGN_KEY_CHECKS=1")
            self.con.commit()

        print("[DATABASE] Update de {} dans la table {}".format(condition, table))

        self.deco()

    def ajoutLigne(self, table, donnes):
        self.connect()

        # try:
        #     with self.con.cursor() as cur:
        #         cur.execute("DELETE FROM '{}' WHERE '{}'".format(table, condition))
        # except:
        #     pass

        with self.con.cursor() as cur:
            cur.execute("SET FOREIGN_KEY_CHECKS=0")
            cur.execute("INSERT INTO {} VALUES ({})".format(table,donnes))
            cur.execute("SET FOREIGN_KEY_CHECKS=1")
            self.con.commit()

        print("[DATABASE] Insertion de {} dans la table {}".format(donnes, table))

        self.deco()
