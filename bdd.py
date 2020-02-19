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
            self.connect()

    def existanceTable(self, table):
        try:
            with self.con.cursor() as cur:
                cur.execute("SELECT * FROM {} LIMIT 0;".format(table))
            res = True
            txt = "existe."
        except:
            res = False
            txt = "n'existe pas."

        print("[DATABASE] La table {} {}".format(table, txt))

        return res


    def contenuTable(self, table):
        try:
            with self.con.cursor() as cur:
                cur.execute("SELECT * FROM {};".format(table))
            res = cur.fetchall()
        except:
            pass

        print("[DATABASE] Récupération contenue table {}".format(table))

        return res
