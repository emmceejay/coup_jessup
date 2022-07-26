# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:09:54 2022

@author: Daniel Mishler
"""

import Coup
import Beef
import Player_Beefier
import JoeyD
import Trey
import Markus
import Beefiest
import Player_Beefeted

gm = Coup.Game_Master()

beef = Beef.Player_Beef()
player_beefier = Player_Beefier.Player_Beefier()
joeyd = JoeyD.Player_JoeyD()
trey = Trey.Player_Trey()
markus = Markus.Player_Markus()
beefiest = Beefiest.Player_Beefiest()
beefeted = Player_Beefeted.Player_Beefeted()

players = [joeyd, beefeted]


wincounts = {}
fname = ""
for player in players:
    wincounts[player.name] = 0
    fname += player.name
wincounts["none"] = 0
fname += ".coup"
for i in range(1000):
    print("game #%d" % i)
    gm.game(players, fname = fname)
    gamefile = open(fname, "r")
    lines = gamefile.read().split('\n')
    winnerline = lines[-2]
    winner = winnerline.split()[1]
    wincounts[winner] += 1

    gamefile.close()


for player in players:
    name = player.name
    print("%s wins %d games" % (name, wincounts[name]))