# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 16:35:07 2022

@author: Mike
"""
import random

class Deck:
    def __init__(self, player_count, cards=[]):
        #print("__init__(deck)")
        self.deck = cards
        self.player_count = player_count * 2
    def add(self,newcard):
        #print("add")
        if type(newcard) == str:
            self.deck.append(newcard)
        else:
            print('new card must be str')
    def show(self):
        #print("show")
        for i in (self.deck):
            print(i)
    def shuffle(self):
        #print("shuffle")
        random.shuffle(self.deck)
    def draw(self):
        #print("draw")
        drawncard = []
        for i in range(0, self.player_count):
            self.shuffle()
            drawncard.append(self.deck[0])
            self.deck.remove(drawncard[-1])
        #print(drawncard)
        return drawncard
    
class Player:
    print("here")
    logg = []
    coins = 2
    def __init__(self, name, card1, card2):
        print("__init__(player)")
        self.name = name
        #self.coins = 2
        self.card1 = card1
        self.card2 = card2
        self.play = ""
        return None
    def act(self):
        #print("act")
        if(self.coins >= 7):
            self.logg.append("coup")
            self.coins = 0
            self.play = "coup"
            
        else:
            self.logg.append("tax")
            self.coins += 3
            self.play = "tax"
        print(self.coins)
        print(self.logg)
        return None
    def log(self):
        #print("log")
        if(self.logg[-1] == "tax"):
                self.coins += 3
        elif(self.logg[-1] == "coup"):
            if(self.coins > 7):
                self.coins -= 7
                Game_master.player2.card1 = ""
            else:
                print(self.name, "made an illegal move!")
        return None
    
class Game_master:
    def __init__(self):
        #print("__init__(game)")
        gamefile = open("gamefile.txt", "w")
        gamefile.write("")
        gamefile.close()
        self.card = []
        return None
    def game_init(self, player_name):
        #print("game_init")
        gamefile = open("gamefile.txt", "a")
        deck = ["duke", "duke", "duke", "assassin", "assassin", "assassin", "ambassador", "ambassador", "ambassador", "captain", "captain", "captain", "contessa", "contessa", "contessa"]
        cards = []
        get_cards = Deck(len(player_name), deck)
        cards = get_cards.draw()
        #print(cards)
        #print(len(player_name))
        for i in range (0, len(player_name)):
            gamefile.write(player_name[i])
            gamefile.write(cards[0])
            self.card.append(cards[0])
            cards.remove(cards[0])
            gamefile.write(cards[0])
            self.card.append(cards[0])
            cards.remove(cards[0])
            gamefile.write("2")
            #print(cards)
        gamefile.close()
        return None
    def turn(self, player_name, whose_turn):
        #print("turn")
        # Process one action, such as "a tax" or "markus steal daniel"
        # Check to see whether that action was valid
        # Write that action to a gamefile and each player's log
        # If a player had to discard, also write that action to a gamefile
        # Update player cards and coins accordingly
        gamefile = open("gamefile.txt", "r")
        gamefiler = gamefile.read()
        gamefile.close()
        #print(len(self.card))
        #print(self.card)
        if(whose_turn == 0):
            player = Player(player_name[whose_turn], self.card[0], self.card[1])
            player.act()
            player.log()
        elif(whose_turn == 1):
            player = Player(player_name[whose_turn], self.card[2], self.card[3])
            player.act()
            player.log()
        elif(whose_turn == 2):
            player = Player(player_name[whose_turn], self.card[4], self.card[5])
            player.act()
            player.log()
        elif(whose_turn == 3):
            player = Player(player_name[whose_turn], self.card[6], self.card[7])
            player.act()
            player.log()
        elif(whose_turn == 4):
            player = Player(player_name[whose_turn], self.card[8], self.card[9])
            player.act()
            player.log()
        elif(whose_turn == 5):
            player = Player(player_name[whose_turn], self.card[10], self.card[11])
            player.act()
            player.log()
        return False
    def game(self, player_name):
        #print("game")
        gamefile = open("gamefile.txt", "r")
        gamefiler = gamefile.read()
        gamefile.close()
        self.game_init(player_name)
        is_game_over = False
        whose_turn = 0
        while(not is_game_over):
            is_game_over = self.turn(player_name, whose_turn)
            if(whose_turn < len(player_name)):
                whose_turn += 1
            else:
                whose_turn = 0
        #print(gamefiler)
        return None

gam = Game_master()
gam.game(["dave", "paul", "rasputin"])