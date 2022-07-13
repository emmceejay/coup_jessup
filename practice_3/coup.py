# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 16:35:07 2022

@author: Mike
"""
import random
import Player_Beef

class Deck:
    def __init__(self):
        self.cards = []
        copies = 3
        coup_types = ["duke", "captain", "contessa", "ambassador", "assassin"]
        for i in range(copies):
            for card in coup_types:
                self.add(card)
        self.shuffle()
    def add(self, card):
        self.cards.append(card)
    def insert(self, card):
        # That's right, inserting into the top of the deck
        # requires another method!
        self.cards.insert(0, card)
    def show(self):
        print("deck contents:")
        for card in self.cards:
            print(card)
    def draw(self):
        self.shuffle()
        if len(self.cards) == 0:
            print("Error: draw from empty deck")
            return None
        else:
            first_card = self.cards[0]
            self.cards.remove(first_card)
            return first_card
    def shuffle(self):
        random.shuffle(self.cards)
    
    
class Player:
    def __init__(self, name):
        self.name = name
        self.log = ""
        self.coins = 0
        self.cards = []
    def turn(self):
        if self.coins < 7:
            return "tax"
        else:
            target = self.find_active_target()
            return "coup" + " " + target
    def react(self, hint):
        if hint == "turn":
            return self.turn()
        elif hint == "discard":
            discard_me = self.cards[0]
            self.cards.remove(self.cards[0])
            return discard_me
        elif hint == "income":
            rand = random.randint(0,2)
            if(rand == 1):
                return "challenge"
            else:
                return "pass"
        elif hint == "foreign_aid":
            rand = random.randint(0,2)
            if(rand == 1):
                return "challenge"
            elif(rand == 2):
                return "block"
            else:
                return "pass"
        elif hint == "coup":
            rand = random.randint(0,2)
            if(rand == 1):
                return "challenge"
            else:
                return "pass"
        elif hint == "tax":
            rand = random.randint(0,2)
            if(rand == 1):
                return "challenge"
            else:
                return "pass"
        elif hint == "steal":
            rand = random.randint(0,2)
            if(rand == 1):
                return "challenge"
            elif(rand == 2):
                return "block"
            else:
                return "pass"
        elif hint == "exchange":
            rand = random.randint(0,2)
            if(rand == 1):
                return "challenge"
            else:
                return "pass"
        elif hint == "assassinate":
            rand = random.randint(0,2)
            if(rand == 1):
                return "challenge"
            elif(rand == 2):
                return "block"
            else:
                return "pass"
        elif hint == "block_foreign_aid":
            rand = random.randint(0,2)
            if(rand == 1):
                return "challenge"
            else:
                return "pass"
        elif hint == "block_steal":
            rand = random.randint(0,2)
            if(rand == 1):
                return "challenge"
            else:
                return "pass"
        elif hint == "block_assassinate":
            rand = random.randint(0,2)
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
        
        
class Game_Master:
    def __init__(self):
        self.players = []
        self.active_player_names = []
        self.active_player_name = ""
        self.log = ""
        self.deck = Deck()
    def game_init(self, players):
        # You can check for duplicate player names if you're worried about
        # people fiddling with the game
        """for i in range(0, len(players)-1):
            if(players[i] == players[i-1]):
                print("Error: players must have different names")"""
        if(len(players) < 2):
            print("Error: game must be played with at least 2 players")
        if(len(players) > 6):
            print("Error: game must be played with at most 6 players")
        self.active_player_names = []
        for player in players:
            self.active_player_names.append(player.name)
            self.players.append(player)
        self.log = ""
        for player in self.players:
            player.coins = 2
            player.log = ""
            player.cards = [self.deck.draw(), self.deck.draw()]
        first_message = "players: "
        first_message += str(self.active_player_names)
        first_message = first_message.replace("'","")
        self.broadcast(first_message)
        self.active_player_name = self.active_player_names[0]
    def turn(self):
        active_player = self.name_to_player(self.active_player_name)
        action = active_player.react("turn")
        message = self.active_player_name + " " + action
        self.broadcast(message)
        # Next week we have to insert challenge and block architecture here
        do_continue = self.challenge_and_block(action)
        if(do_continue == "continue"):
            self.active_player_name = self.active_player_names[0]
            active_player = self.name_to_player(self.active_player_name)
            split_action = action.split()
            if len(split_action) == 2:
                action = split_action[0]
                target_name = split_action[1]
            elif len(split_action) == 1:
                target_name = None
            else:
                print("Error: invalid action returned")
            #Check if action was legal
            if(action == "assassinate"):
                if(active_player.coins < 3):
                    print("illegal action: not enough coins")
                    self.turn()
            elif(action == "coup"):
                if(active_player.coins < 7):
                    print("illegal action: not enough coins")
                    self.turn()
            #do action
            self.handle_action(self.active_player_name, action, target_name)
            # Now advance the active player
            self.advance_active_player()
            return
        elif(do_continue == "block"):
            self.advance_active_player()
            return
        else:
            print("Error: unknown action")
            return
    def challenge_and_block(self, action):
        for player in self.active_player_names:
            if(player != self.active_player_name):
                active_player = self.name_to_player(player)
                reaction = active_player.react(action)
                if(reaction == "block"):
                    #block
                    self.active_player_name = player
                    active_player = self.name_to_player(self.active_player_name)
                    for player in self.active_player_names:
                        if(player != self.active_player_name):
                            reaction = player.react("block" + "_" + action)
                            if(reaction == "challenge"):
                                #challenge
                                if(self.active_player_name == "Player_Beef"):
                                    do_more = active_player.react("challenged")
                                    if(do_more == "succeeded"):
                                        player.cards.append(self.deck.draw())
                                else:
                                    if(action == "block_foreign_aid"):
                                        if(active_player.cards[0] == "duke"):
                                            self.active_player_name = player
                                            active_player = self.name_to_player(self.active_player_name)
                                            active_player.react("discard")
                                            if(len(active_player.cards) == 0):
                                                self.active_player_names.remove(self.active_player_name)
                                            return "block"
                                        elif(len(active_player.cards) != 1):
                                            if(active_player.cards[1] == "duke"):
                                                self.active_player_name = player
                                                active_player = self.name_to_player(self.active_player_name)
                                                active_player.react("discard")
                                                if(len(active_player.cards) == 0):
                                                    self.active_player_names.remove(self.active_player_name)
                                            return "block"
                                        else:
                                            self.active_player_name = self.active_player_names[0]
                                            active_player = self.name_to_player(self.active_player_name)
                                            active_player.react("discard")
                                            if(len(active_player.cards) == 0):
                                                self.active_player_names.remove(self.active_player_name)
                                            return "continue"
                                    if(action == "block_steal"):
                                        if(active_player.cards[0] == "captain"):
                                            self.active_player_name = player
                                            active_player = self.name_to_player(self.active_player_name)
                                            active_player.react("discard")
                                            if(len(active_player.cards) == 0):
                                                self.active_player_names.remove(self.active_player_name)
                                            return "block"
                                        elif(len(active_player.cards) != 1):
                                            if(active_player.cards[1] == "captain"):
                                                self.active_player_name = player
                                                active_player = self.name_to_player(self.active_player_name)
                                                active_player.react("discard")
                                                if(len(active_player.cards) == 0):
                                                    self.active_player_names.remove(self.active_player_name)
                                            return "block"
                                        if(active_player.cards[1] == "ambassador"):
                                            self.active_player_name = player
                                            active_player = self.name_to_player(self.active_player_name)
                                            active_player.react("discard")
                                            if(len(active_player.cards) == 0):
                                                self.active_player_names.remove(self.active_player_name)
                                            return "block"
                                        elif(len(active_player.cards) != 1):
                                            if(active_player.cards[1] == "ambassador"):
                                                self.active_player_name = player
                                                active_player = self.name_to_player(self.active_player_name)
                                                active_player.react("discard")
                                                if(len(active_player.cards) == 0):
                                                    self.active_player_names.remove(self.active_player_name)
                                            return "block"
                                        else:
                                            self.active_player_name = self.active_player_names[0]
                                            active_player = self.name_to_player(self.active_player_name)
                                            active_player.react("discard")
                                            if(len(active_player.cards) == 0):
                                                self.active_player_names.remove(self.active_player_name)
                                            return "continue"
                                    if(action == "block_assassinate"):
                                        if(active_player.cards[0] == "contessa"):
                                            self.active_player_name = player
                                            active_player = self.name_to_player(self.active_player_name)
                                            active_player.react("discard")
                                            if(len(active_player.cards) == 0):
                                                self.active_player_names.remove(self.active_player_name)
                                            return "block"
                                        elif(len(active_player.cards) != 1):
                                            if(active_player.cards[1] == "contessa"):
                                                self.active_player_name = player
                                                active_player = self.name_to_player(self.active_player_name)
                                                active_player.react("discard")
                                                if(len(active_player.cards) == 0):
                                                    self.active_player_names.remove(self.active_player_name)
                                            return "block"
                                        else:
                                            self.active_player_name = self.active_player_names[0]
                                            active_player = self.name_to_player(self.active_player_name)
                                            active_player.react("discard")
                                            if(len(active_player.cards) == 0):
                                                self.active_player_names.remove(self.active_player_name)
                                            return "continue"
                    return "block"
                active_player = self.name_to_player(self.active_player_name)
                if(reaction == "challenge"):
                    #challenge
                    if(action == "tax"):
                        if(active_player.cards[0] == "duke"):
                            self.active_player_name = player
                            active_player = self.name_to_player(self.active_player_name)
                            active_player.react("discard")
                            if(len(active_player.cards) == 0):
                                self.active_player_names.remove(self.active_player_name)
                            return "continue"
                        elif(len(active_player.cards) != 1):
                            if(active_player.cards[1] == "duke"):
                                self.active_player_name = player
                                active_player = self.name_to_player(self.active_player_name)
                                active_player.react("discard")
                                if(len(active_player.cards) == 0):
                                    self.active_player_names.remove(self.active_player_name)
                            return "continue"
                        else:
                            self.active_player_name = self.active_player_names[0]
                            active_player = self.name_to_player(self.active_player_name)
                            active_player.react("discard")
                            if(len(active_player.cards) == 0):
                                self.active_player_names.remove(self.active_player_name)
                            return "block"
                    if(action == "steal"):
                        if(active_player.cards[0] == "captain"):
                            self.active_player_name = player
                            active_player = self.name_to_player(self.active_player_name)
                            active_player.react("discard")
                            if(len(active_player.cards) == 0):
                                self.active_player_names.remove(self.active_player_name)
                            return "continue"
                        elif(len(active_player.cards) != 1):
                            if(active_player.cards[1] == "captain"):
                                self.active_player_name = player
                                active_player = self.name_to_player(self.active_player_name)
                                active_player.react("discard")
                                if(len(active_player.cards) == 0):
                                    self.active_player_names.remove(self.active_player_name)
                            return "continue"
                        else:
                            self.active_player_name = self.active_player_names[0]
                            active_player = self.name_to_player(self.active_player_name)
                            active_player.react("discard")
                            if(len(active_player.cards) == 0):
                                self.active_player_names.remove(self.active_player_name)
                            return "block"
                    if(action == "exchange"):
                        if(active_player.cards[0] == "ambassador"):
                            self.active_player_name = player
                            active_player = self.name_to_player(self.active_player_name)
                            active_player.react("discard")
                            if(len(active_player.cards) == 0):
                                self.active_player_names.remove(self.active_player_name)
                            return "continue"
                        elif(len(active_player.cards) != 1):
                            if(active_player.cards[1] == "ambassador"):
                                self.active_player_name = player
                                active_player = self.name_to_player(self.active_player_name)
                                active_player.react("discard")
                                if(len(active_player.cards) == 0):
                                    self.active_player_names.remove(self.active_player_name)
                            return "continue"
                        else:
                            self.active_player_name = self.active_player_names[0]
                            active_player = self.name_to_player(self.active_player_name)
                            active_player.react("discard")
                            if(len(active_player.cards) == 0):
                                self.active_player_names.remove(self.active_player_name)
                            return "block"
                    if(action == "assassinate"):
                        if(active_player.cards[0] == "assassin"):
                            self.active_player_name = player
                            active_player = self.name_to_player(self.active_player_name)
                            active_player.react("discard")
                            if(len(active_player.cards) == 0):
                                self.active_player_names.remove(self.active_player_name)
                            return "continue"
                        elif(len(active_player.cards) != 1):
                            if(active_player.cards[1] == "assassin"):
                                self.active_player_name = player
                                active_player = self.name_to_player(self.active_player_name)
                                active_player.react("discard")
                                if(len(active_player.cards) == 0):
                                    self.active_player_names.remove(self.active_player_name)
                            return "continue"
                        else:
                            self.active_player_name = self.active_player_names[0]
                            active_player = self.name_to_player(self.active_player_name)
                            active_player.react("discard")
                            if(len(active_player.cards) == 0):
                                self.active_player_names.remove(self.active_player_name)
                            return "block"
                    
        self.active_player_name = self.active_player_names[0]
        return "continue"
    def show(self, show_cards = False):
        print("Coup game")
        print("players:", len(self.players))
        for player in self.players:
            player.show(show_cards)
            print()
        print("game so far:")
        print(self.log)
    def receive(self, message):
        self.log += message
        self.log += "\n"
    def broadcast(self, message):
        self.receive(message)
        for player in self.players:
            player.receive(message)
    def name_to_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        # if not found
        print("Error: player '%s' not found" % player_name)
        return None
    def eliminate(self, player_name):
        self.active_player_names.remove(player_name)
    def player_eliminated(self, player_name):
        if player_name in self.active_player_names:
            return False
        else:
            return True
    def player_alive(self, player_name):
        if player_name in self.active_player_names:
            return True
        else:
            return False
    def advance_active_player(self):
        # note to students: there are *lots* of better ways to do this and
        # I encourage you to take them up
        ap_index = self.active_player_names.index(self.active_player_name)
        ap_index += 1
        if ap_index == len(self.active_player_names):
            ap_index = 0
        self.active_player_name = self.active_player_names[ap_index]
    def handle_action(self, player_name, action, target_name):
        # Handle an unblocked, unchallenged action
        player = self.name_to_player(player_name)
        if target_name is not None:
            target = self.name_to_player(target_name)
        if action == "income":
            player.coins += 1
        elif action == "foreign_aid":
            player.coins += 2
        elif action == "tax":
            player.coins += 3
        elif action == "steal":
            coins_to_steal = min(target.coins, 2)
            player.coins += coins_to_steal
            target.coins -= coins_to_steal
        elif action == "coup":
            player.coins -= 7
            if self.player_alive(target.name):
                discarded_card = target.react("discard")
                message = target_name + " discard " + discarded_card
                target.cards.remove(discarded_card)
                self.broadcast(message)
                if len(target.cards) == 0:
                    self.eliminate(target.name)
        elif action == "assassinate":
            player.coins -= 3
            if self.player_alive(target.name):
                discarded_card = target.react("discard")
                message = target_name + " discard " + discarded_card
                target.cards.remove(discarded_card)
                self.broadcast(message)
                if len(target.cards) == 0:
                    self.eliminate(target.name)
        elif action == "exchange":
            if(self.active_player_name == "Player_Beef"):
                if(player.cards.len == 2):
                    player.cards.append(self.deck.draw())
                    player.cards.append(self.deck.draw())
                    player.react("i_exchange")
                else:
                    player.cards.append(self.deck.draw())
                    player.react("i_exchange")
                return
            else:
                player.cards.append(self.deck.draw())
                player.cards.append(self.deck.draw())
                for i in range(2):
                    placeback_card = player.react("placeback")
                    # no message here to broadcast: this information is private
                    player.cards.remove(placeback_card)
                    self.deck.insert(placeback_card)
        else:
            print("action not implemented:", player_name, action, target)
    def game(self, players, fname = "coup_game_test.coup"):
        self.game_init(players)
        while len(self.active_player_names) > 1:
            self.turn()
        message = "winner: " + self.active_player_name
        self.broadcast(message)
        gamefile = open(fname, "w")
        gamefile.write(self.log)
        gamefile.close()
        
        
def double_list(mylist):
    orig_len = len(mylist)
    for i in range(orig_len):
        mylist.append(mylist[i])
    return mylist
        
gam = Game_Master()
dave = Player("dave")
paul = Player("paul")
rasputin = Player("rasputin")
gam.game([dave, paul, rasputin])