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
        self.con = None

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
            print('[DATABASE] Connection Error !!')
