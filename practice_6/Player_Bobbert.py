# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 20:28:07 2022

@author: Mike
"""

# BeatBeef&Markus
# strategy:
# always claim to have a duke to get Beef to income (tax turn 1 and block foreign aid)
# never challenge assassins, ambassadors, or duke after turn 1
# also never challenge blocks
# always block assassins (50% chance to win if I don't have contessa otherwise it always wins)
# if stolen from and I have a captain or ambassador then block                           0000000000000
# else challenge

import random

beef_card_priority = [
    "ambassador",
    "captain",
    "duke",
    "contessa",
    "assassin"
    ]

card_abilities = {
    "duke" :       ["tax", "block_foreign_aid"],
    "captain" :    ["steal", "block_steal"],
    "assassin" :   ["assassinate"],
    "contessa" :   ["block_assassinate"],
    "ambassador" : ["exchange", "block_steal"]
    }

turn_actions = [
    "income",
    "foreign_aid",
    "coup",
    "tax",
    "steal",
    "exchange",
    "assassinate"
    ]


class Player_Bobbert:
    def __init__(self, name="beef"):
        self.name = name
        self.log = ""
        self.cards = []
        self.coins = 0
    def react(self, hint):
        if hint == "turn":
            game_info = self.get_game_info(my_turn = True)
            # Beefeted always taxes turn 1
            if game_info["turn"] == 1:
                return "tax"
            
            # else, it's not turn 1. What's the next highest priority?
            # Beefeted will swap to get rid of an ambassador
            if "ambassador" in self.cards:
                return "exchange"
            
            
            # Now, time for Beefeted's objective
            target = self.find_target(game_info)
            if "assassin" in self.cards and self.coins >= 3:
                return "assassinate " + target
            if self.coins >= 7:
                return "coup " + target
            
            
            # if I have a captain then steal
            # else just foreign aid
            if("captain" in self.cards):
                return "steal" + target
            
            return "foreign aid"
            
        elif hint in ["placeback", "discard"]:
            for consideration in beef_card_priority:
                for card in self.cards:
                    if card == consideration:
                        return card
            # Error check
            print("Error: beef couldn't find a card!")
            return "?"
        elif hint == "challenged":
            log_lines = self.log.split('\n')
            last_line = log_lines[-3]
            action = last_line.split()[1]
            # First, see if he can answer the challenge
            for card in self.cards:
                if action in card_abilities[card]:
                    return card
            # Beef can't answer the challenge.
            for consideration in beef_card_priority:
                for card in self.cards:
                    if card == consideration:
                        return card
            # Error check
            print("Error: beef couldn't find a card!")
            return "?"            
        elif hint == "cb?":
            game_info = self.get_game_info(my_turn = False)
            # Always block if you can
            # and always block assassins and foreign aid
            if game_info["cb_state"]["action"] == "foreign_aid":
                return "block"
            if game_info["cb_state"]["action"] == "assassinate":
                if game_info["cb_state"]["target"] == self.name:
                    return "block"
            if game_info["cb_state"]["action"] == "steal":
                if game_info["cb_state"]["target"] == self.name:
                    if "captain" in self.cards or "ambassador" in self.cards:
                        return "block"
            
            # Now for Beefeted's challenges
            # always challenge turn 1 tax and steal
            if game_info["cb_state"]["action"] == "tax":
                if game_info["turn"] == 1:
                    return "challenge"
            elif game_info["cb_state"]["action"] == "steal":
                return "challenge"
            
            return "pass"
    
    
    # A more refined function that gets all players' cards and coins
    # This will function better than just getting a player who is alive:
    # It will also help identify threats. If you want to use this function,
    # Feel free to go ahead and try it.
    def get_game_info(self, my_turn = False):
        
        # Turns start with turn 1 - it becomes turn 1 as soon as the
        # first player acts.
        turn = 0
        
        # Find all the players
        first_log_line = self.log.split('\n')[0]
        start_i = first_log_line.find('[')
        end_i = first_log_line.find(']')
        players_string = first_log_line[start_i+1:end_i]
        players_array = players_string.split(", ")
        
        # Build a dictionary of players, each player key leading to another
        # dictionary showing their cards and coins
        players_dict = {}
        for player_name in players_array:
            players_dict[player_name] = {}
            players_dict[player_name]["cards"] = 2
            players_dict[player_name]["coins"] = 2
            players_dict[player_name]["claims"] = []
        
        
        cb_state= {} # challenge/block state information
        # Note: This information may not *always* be accurate,
        # but it will always be accurate when needed for a "cb?" hint.
        
        first_player = players_array[0]
        
        
        # Man, do I feel like this section is a little sloppy. Relies on
        # some back-looking to see if an action should have applied.
        # Forward-looking would be better if possible.
        intent = None
        recent_round_apply = False
        blocked = challenged = challenge_success = False
        intent_player = intent_target = None
        for line in self.log.split('\n'):
            if line == "":
                # Apply the most recent intent if I already passed my chance
                # to block or challenge.
                recent_round_apply = my_turn
                action = player = target = ""
            else:
                player = line.split()[0]
                action = line.split()[1]
                if action in ["steal", "coup", "assassinate"]:
                    target = line.split()[2]
                else:
                    target = None
            
            if action == "discard":
                players_dict[player]["cards"] -= 1
                
            # *maybe* apply the effects of the action if it's a turn action
            
            # decide whether the previous intent should apply
            apply_intent = False
            if action[:6] == "block_":
                blocked = True
                cb_state["blocker"] = player
            if action == "challenge":
                challenged = True
                challenger = player
            if action == "discard" and challenged == True:
                if player == challenger:
                    challenge_success = False
                else:
                    challenge_success = True
            if action in turn_actions or recent_round_apply:
                apply_intent = not (blocked ^ challenge_success)
        
            if apply_intent:
                if intent == "income":
                    players_dict[intent_player]["coins"] += 1
                if intent == "foreign_aid":
                    players_dict[intent_player]["coins"] += 2
                if intent == "tax":
                    players_dict[intent_player]["coins"] += 3
                if intent == "steal":
                    steal_coins = min(players_dict[intent_target]["coins"], 2)
                    players_dict[intent_player]["coins"] += steal_coins
                    players_dict[intent_target]["coins"] -= steal_coins
                if intent == "assassinate":
                    players_dict[intent_player]["coins"] -= 3
                if intent == "coup":
                    players_dict[intent_player]["coins"] -= 7
                if intent == "exchange":
                    pass
            
            # Prepare the next intent
            if action in turn_actions:
                intent = action
                intent_player = player
                intent_target = target
                blocked = False
                challenge_success = False
                challenged = False
                if player == first_player:
                    turn += 1
                cb_state["actor"] = player
                cb_state["action"] = action
                cb_state["target"] = target
                cb_state["blocker"] = None


        if my_turn == True and first_player == self.name:
            turn += 1
        
        
        game_dict = {}
        game_dict["players"] = players_dict
        game_dict["turn"] = turn
        game_dict["cb_state"] = cb_state
        return game_dict
        
    def find_target(self, game_info):
        # Find a target who is not Beef. Can be modified for smarter selection
        # of targets later on.
        valid_targets = []
        for player in game_info["players"]:
            if player == self.name:
                continue
            if game_info["players"][player]["cards"] > 0:
                valid_targets.append(player)
        
        if(valid_targets[0] == "markus"):
            return valid_targets[0]
        try:
            if(valid_targets[1] == "markus"):
                return valid_targets[1]
        except:
            return valid_targets[0]
    
    def who_claims_dukes(self):
        players_with_duke = []
        state = 0
        # 0: waiting to see a duke claim
        # 1: waiting to see if the duke claim is challenged
        # Note: if they get challenged, they either lose the duke they had
        #       OR they never had a duke. They get removed from the list.
        for line in self.log.split('\n'):
            if line == "":
                action = player = ""
            else:
                player = line.split()[0]
                action = line.split()[1]
            if action in ["tax", "foreign_aid"]:
                if player not in players_with_duke:
                    players_with_duke.append(player)
                state = 1
            if state == 1:
                if action == "challenge":
                    players_with_duke.remove(player)
                state = 0
        # print(players_with_duke)
        return players_with_duke
    
    def receive(self, message):
        self.log += message
        self.log += "\n"
    
    def show(self, show_cards = False):
        print("player", self.name)
        if show_cards:
            print("cards:", self.cards)
        else:
            print("cards:", len(self.cards))
        print("coins:", self.coins)