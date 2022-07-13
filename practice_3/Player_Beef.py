# -*- coding: utf-8 -*-
"""
Created on Sat Jul 9 13:58:01 2022

@author: Mike
"""
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.log = ""
        self.coins = 0
        self.cards = []
        self.turn = 1
    def turn(self):
        if(self.turn == 1):
            self.turn = 2
            return "tax"
        else:
            if(self.cards[0] == "ambassador"):
                return "exchange"
            elif(self.cards[1] == "ambassador"):
                return "exchange"
            elif(self.cards[0] == "assassin"):
                if(self.coins > 2):
                    target = self.find_active_target()
                    return "assassinate" + " " + target
                elif(self.cards[0] == "duke"):
                    return "tax"
                elif(self.cards[1] == "duke"):
                    return "tax"
                log_lines = self.log.split('\n')
                line = -1
                current_line = log_lines[line]
                while(current_line != ""):
                    if(current_line.split == "tax"):
                        return "income"
                    elif(current_line.split == "block_tax"):
                        return "income"
                    line = line - 1
                    current_line = log_lines[line]
                return "foreign_aid"
            elif(self.cards[1] == "assassin"):
                if(self.coins > 2):
                    target = self.find_active_target()
                    return "assassinate" + " " + target
                elif(self.cards[0] == "duke"):
                    return "tax"
                elif(self.cards[1] == "duke"):
                    return "tax"
                log_lines = self.log.split('\n')
                line = -1
                current_line = log_lines[line]
                while(current_line != ""):
                    if(current_line.split == "tax"):
                        return "income"
                    elif(current_line.split == "block_tax"):
                        return "income"
                    line = line - 1
                    current_line = log_lines[line]
                return "foreign_aid"
            else:
                if(self.coins > 6):
                    target = self.find_active_target()
                    return "coup" + " " + target
                elif(self.cards[0] == "duke"):
                    return "tax"
                elif(self.cards[1] == "duke"):
                    return "tax"
                log_lines = self.log.split('\n')
                line = -1
                current_line = log_lines[line]
                while(current_line != ""):
                    if(current_line.split == "tax"):
                        return "income"
                    elif(current_line.split == "block_tax"):
                        return "income"
                    line = line - 1
                    current_line = log_lines[line]
                return "foreign_aid"
    def react(self, hint):
        if hint == "turn":
            return self.turn()
        elif hint == "challenged":
            log_lines = self.log.split('\n')
            last_line = log_lines[-3]
            action = last_line.split()[1]
            if(action == "swap"):
                if(self.cards[0] == "ambassador"):
                    self.log += "Player_Beef shows", self.cards[0]
                    self.cards.remove(self.cards[0])
                    return "succeeded"
                elif(self.cards[1] == "ambassador"):
                    self.log += "Player_Beef shows", self.cards[1]
                    self.cards.remove(self.cards[1])
                    return "succeeded"
                else:
                    self.react("discard")
            elif(action == "assassinate"):
                if(self.cards[0] == "assassin"):
                    self.log += "Player_Beef shows", self.cards[0]
                    self.cards.remove(self.cards[0])
                    return "succeeded"
                elif(self.cards[1] == "assassin"):
                    self.log += "Player_Beef shows", self.cards[1]
                    self.cards.remove(self.cards[1])
                    return "succeeded"
                else:
                    self.react("discard")
            elif(action == "tax"):
                if(self.cards[0] == "duke"):
                    self.log += "Player_Beef shows", self.cards[0]
                    self.cards.remove(self.cards[0])
                    return "succeeded"
                elif(self.cards[1] == "duke"):
                    self.log += "Player_Beef shows", self.cards[1]
                    self.cards.remove(self.cards[1])
                    return "succeeded"
                else:
                    self.react("discard")
            elif(action == "block_tax"):
                if(self.cards[0] == "duke"):
                    self.log += "Player_Beef shows", self.cards[0]
                    self.cards.remove(self.cards[0])
                    return "succeeded"
                elif(self.cards[1] == "duke"):
                    self.log += "Player_Beef shows", self.cards[1]
                    self.cards.remove(self.cards[1])
                    return "succeeded"
                else:
                    self.react("discard")
            elif(action == "block_assassinate"):
                if(self.cards[0] == "contessa"):
                    self.log += "Player_Beef shows", self.cards[0]
                    self.cards.remove(self.cards[0])
                    return "succeeded"
                elif(self.cards[1] == "contessa"):
                    self.log += "Player_Beef shows", self.cards[1]
                    self.cards.remove(self.cards[1])
                    return "succeeded"
                else:
                    self.react("discard")
            elif(action == "block_steal"):
                if(self.cards[0] == "ambassador"):
                    self.log += "Player_Beef shows", self.cards[0]
                    self.cards.remove(self.cards[0])
                    return "succeeded"
                elif(self.cards[1] == "ambassador"):
                    self.log += "Player_Beef shows", self.cards[1]
                    self.cards.remove(self.cards[1])
                    return "succeeded"
                elif(self.cards[0] == "captain"):
                    self.log += "Player_Beef shows", self.cards[0]
                    self.cards.remove(self.cards[0])
                    return "succeeded"
                elif(self.cards[1] == "captain"):
                    self.log += "Player_Beef shows", self.cards[1]
                    self.cards.remove(self.cards[1])
                    return "succeeded"
                else:
                    self.react("discard")
            return self.turn()
        elif hint == "discard":
            if(self.cards[0] == "ambassador"):
                discard_me = self.cards[0]
                self.cards.remove(self.cards[0])
            elif(self.cards[1] == "ambassador"):
                discard_me = self.cards[1]
                self.cards.remove(self.cards[1])
            elif(self.cards[0] == "contessa"):
                discard_me = self.cards[0]
                self.cards.remove(self.cards[0])
            elif(self.cards[1] == "contessa"):
                discard_me = self.cards[1]
                self.cards.remove(self.cards[1])
            elif(self.cards[0] == "assassin"):
                discard_me = self.cards[0]
                self.cards.remove(self.cards[0])
            elif(self.cards[1] == "assassin"):
                discard_me = self.cards[1]
                self.cards.remove(self.cards[1])
            elif(self.cards[0] == "captain"):
                discard_me = self.cards[0]
                self.cards.remove(self.cards[0])
            elif(self.cards[1] == "captain"):
                discard_me = self.cards[1]
                self.cards.remove(self.cards[1])
            elif(self.cards[0] == "duke"):
                discard_me = self.cards[0]
                self.cards.remove(self.cards[0])
            return discard_me
        elif hint == "i_exchange":
            if(self.cards.len == 2):
                if(self.cards[0] == "ambassador"):
                    discard_me = self.cards[0]
                    self.cards.remove(self.cards[0])
                elif(self.cards[1] == "ambassador"):
                    discard_me = self.cards[1]
                    self.cards.remove(self.cards[1])
                elif(self.cards[2] == "ambassador"):
                    discard_me = self.cards[2]
                    self.cards.remove(self.cards[2])
                elif(self.cards[3] == "ambassador"):
                    discard_me = self.cards[3]
                    self.cards.remove(self.cards[3])
                elif(self.cards[0] == "contessa"):
                    discard_me = self.cards[0]
                    self.cards.remove(self.cards[0])
                elif(self.cards[1] == "contessa"):
                    discard_me = self.cards[1]
                    self.cards.remove(self.cards[1])
                elif(self.cards[2] == "contessa"):
                    discard_me = self.cards[2]
                    self.cards.remove(self.cards[2])
                elif(self.cards[3] == "contessa"):
                    discard_me = self.cards[3]
                    self.cards.remove(self.cards[3])
                elif(self.cards[0] == "assassin"):
                    discard_me = self.cards[0]
                    self.cards.remove(self.cards[0])
                elif(self.cards[1] == "assassin"):
                    discard_me = self.cards[1]
                    self.cards.remove(self.cards[1])
                elif(self.cards[2] == "assassin"):
                    discard_me = self.cards[2]
                    self.cards.remove(self.cards[2])
                elif(self.cards[3] == "assassin"):
                    discard_me = self.cards[3]
                    self.cards.remove(self.cards[3])
                elif(self.cards[0] == "captain"):
                    discard_me = self.cards[0]
                    self.cards.remove(self.cards[0])
                elif(self.cards[1] == "captain"):
                    discard_me = self.cards[1]
                    self.cards.remove(self.cards[1])
                elif(self.cards[2] == "captain"):
                    discard_me = self.cards[2]
                    self.cards.remove(self.cards[2])
                elif(self.cards[3] == "captain"):
                    discard_me = self.cards[3]
                    self.cards.remove(self.cards[3])
                elif(self.cards[0] == "duke"):
                    discard_me = self.cards[0]
                    self.cards.remove(self.cards[0])
            else:
                if(self.cards[0] == "ambassador"):
                    discard_me = self.cards[0]
                    self.cards.remove(self.cards[0])
                elif(self.cards[1] == "ambassador"):
                    discard_me = self.cards[1]
                    self.cards.remove(self.cards[1])
                elif(self.cards[0] == "contessa"):
                    discard_me = self.cards[0]
                    self.cards.remove(self.cards[0])
                elif(self.cards[1] == "contessa"):
                    discard_me = self.cards[1]
                    self.cards.remove(self.cards[1])
                elif(self.cards[0] == "assassin"):
                    discard_me = self.cards[0]
                    self.cards.remove(self.cards[0])
                elif(self.cards[1] == "assassin"):
                    discard_me = self.cards[1]
                    self.cards.remove(self.cards[1])
                elif(self.cards[0] == "captain"):
                    discard_me = self.cards[0]
                    self.cards.remove(self.cards[0])
                elif(self.cards[1] == "captain"):
                    discard_me = self.cards[1]
                    self.cards.remove(self.cards[1])
                elif(self.cards[0] == "duke"):
                    discard_me = self.cards[0]
                    self.cards.remove(self.cards[0])
            return
        elif hint == "income":
            rand = random.randint(0,2)
            return "pass"
        elif hint == "foreign_aid":
            if(self.cards[0] == "duke"):
                return "block"
            elif(self.cards[1] == "duke"):
                return "block"
            else:
                return "pass"
        elif hint == "tax":
            if(self.turn == 1):
                return "challenge"
            else:
                return "pass"
        elif hint == "steal":
            if(self.cards[0] == "captain"):
                return "block"
            elif(self.cards[1] == "captain"):
                return "block"
            elif(self.cards[0] == "ambassador"):
                return "block"
            elif(self.cards[1] == "ambassador"):
                return "block"
            else:
                return "pass"
        elif hint == "exchange":
            return "pass"
        elif hint == "assassinate":
            if(self.cards[0] == "contessa"):
                return "block"
            elif(self.cards[1] == "contessa"):
                return "block"
            elif(self.cards.len == 1):
                return "challenge"
            else:
                return "pass"
        elif hint == "block_foreign_aid":
            return "pass"
        elif hint == "block_steal":
            return "pass"
        elif hint == "block_assassinate":
            rand = random.randint(0,1)
            if(rand == 1):
                return "challenge"
            else:
                return "pass"
    def find_active_target(self):
        # Find all the players
        first_log_line = self.log.split('\n')[0]
        start_i = first_log_line.find('[')
        end_i = first_log_line.find(']')
        players_string = first_log_line[start_i+1:end_i]
        players_array = players_string.split(", ")
        # Remove myself
        players_array.remove(self.name)
        # You might entertain using a dictionary here: I will just double
        # the list
        players_array = double_list(players_array)
        # Find the last player that acted
        for line in self.log.split('\n'):
            if line == "":
                continue # ignore the last (empty) line
                # the difference between break and continue here is simply
                # that continue will end the iteration of the for loop, and
                # instead of being *guaranteed* to exit the for loop, will
                # enter the next iteration if there is one to do.
            player = line.split()[0]
            action = line.split()[1]
            if action == "discard" and player != self.name:
                players_array.remove(player)
        # You don't need to shuffle, but I will
        random.shuffle(players_array)
        target = players_array[0]
        return target
    def receive(self, message):
        self.log += message
        self.log += "\n"
        return
    def show(self, show_cards = False):
        print("player", self.name)
        if show_cards:
            print("cards:", self.cards)
        else:
            print("cards:", len(self.cards))
        print("coins:", self.coins)

def double_list(mylist):
    orig_len = len(mylist)
    for i in range(orig_len):
        mylist.append(mylist[i])
    return mylist