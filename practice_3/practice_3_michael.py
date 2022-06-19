#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:05 2022

@author: michael
"""

"""
Objectives:
    - Interactions between classes
    - Defensive programming
    - Write to a coup file
"""

"""
Instructions:
    - Copy this whole file into your own directory
    - Remove the instructor's name from the top and place your name
        - do the same with creation date
    - Follow the problem specifications that follow and make a python
      document that can run without any errors
    - For a hope score, push your homework to github by Sunday at 8:00 PM
        - If you submit after that, it's fine, but you get 0 marks if
          I grade and don't find your homework
"""


"""
Michael, Philip, and Thomas can skip problem 1 if they wish
"""
import random;
# Problem 1
# Write a function that takes a string as an argument
# Returns: the longest substring in that string after splitting the string
#          based on spaces.
# Example: my_func("hello world my name is Daniel")
#          returns: "Daniel"

"""def longest_sub(string):
    num = 0
    longest = 0
    for character in string:
        print(character)
        if(character is not " "):
            num = num + 1
            print(num)
        if(character == " "):
            if(num > longest):
                longest = num
                print(longest, "is the current longest")
            num = 0
    if(num > longest):
        longest = num
        num = 0
        print(longest, "is the current longest")
    print(longest, "is the longest")
    return None"""

# Problem 2
# In any way you see fit, find a way to *programmatically* determine whether
# the 8 files `game_*.coup` are valid games.
# You probably won't directly use this in your coup Game_Master,
# but you'll definitely implement a better game master with this knowledge.
# Recommendation: write some helper functions that are modular and easily
#                 usable in your coup.py file you'll make later on.

def check_all_files():
    check_legality("game_a.txt")
    check_legality("game_b.txt")
    check_legality("game_c.txt")
    check_legality("game_d.txt")
    check_legality("game_e.txt")
    check_legality("game_f.txt")
    check_legality("game_g.txt")
    check_legality("game_h.txt")
    return None

def check_legality(file_name):
    player1 = get_players(file_name, 1)
    player2 = get_players(file_name, 2)
    player1_coins = 2
    player2_coins = 2
    player1_cards = 2
    player2_cards = 2
    
    if(file_name == "game_a.txt"):
        file = open("game_a.txt", "r")
    elif(file_name == "game_b.txt"):
        file = open("game_b.txt", "r")
    elif(file_name == "game_c.txt"):
        file = open("game_c.txt", "r")
    elif(file_name == "game_d.txt"):
        file = open("game_d.txt", "r")
    elif(file_name == "game_e.txt"):
        file = open("game_e.txt", "r")
    elif(file_name == "game_f.txt"):
        file = open("game_f.txt", "r")
    elif(file_name == "game_g.txt"):
        file = open("game_g.txt", "r")
    elif(file_name == "game_h.txt"):
        file = open("game_h.txt", "r")
    line_max = sum(1 for line in file)
    file.close()
    line = 2
    
    while(line <= line_max):
        player = check_player(file_name, player1, player2, line)
        if(player != "winner"):
            play = check_play(file_name, player, line)
            if(play == "tax"):
                if(player == player1):
                    player1_coins += 3
                elif(player == player2):
                    player2_coins += 3
            elif(play == "foreign_aid"):
                if(player == player1):
                    player1_coins += 2
                elif(player == player2):
                    player2_coins += 2
            elif(play == "income"):
                if(player == player1):
                    player1_coins += 1
                elif(player == player2):
                    player2_coins += 1
            elif(play == "steal"):
                if(player == player1):
                    player1_coins += 2
                    player2_coins -= 2
                elif(player == player2):
                    player2_coins += 2
                    player1_coins -= 2
            elif(play == "assassinate"):
                if(player == player1):
                    if(player1_coins > 2):
                        player1_coins -= 3
                        player2_cards -= 1
                    else:
                        print(player1, "made an illegal move!")
                        return None
                elif(player == player2):
                    if(player2_coins > 2):
                        player2_coins -= 3
                        player1_cards -= 1
                    else:
                        print(player1, "made an illegal move!")
                        return None
            elif(play == "coup"):
                if(player == player1):
                    if(player1_coins > 7):
                        player1_coins -= 7
                        player2_cards -= 1
                    else:
                        print(player1, "made an illegal move!")
                        return None
                elif(player == player2):
                    if(player2_coins > 7):
                        player2_coins -= 7
                        player1_cards -= 1
                    else:
                        print(player1, "made an illegal move!")
                        return None
            else:
                if(player == player1):
                    print(player1, "is the winner")
                elif(player == player2):
                    print(player2, "is the winner")
        line += 1
    print("The game is fully legal")
    return None

def get_players(file_name, player_num):
    player1 = []
    player2 = []
    character = ""
    if(file_name == "game_a.txt"):
        file = open("game_a.txt", "r")
    elif(file_name == "game_b.txt"):
        file = open("game_b.txt", "r")
    elif(file_name == "game_c.txt"):
        file = open("game_c.txt", "r")
    elif(file_name == "game_d.txt"):
        file = open("game_d.txt", "r")
    elif(file_name == "game_e.txt"):
        file = open("game_e.txt", "r")
    elif(file_name == "game_f.txt"):
        file = open("game_f.txt", "r")
    elif(file_name == "game_g.txt"):
        file = open("game_g.txt", "r")
    elif(file_name == "game_h.txt"):
        file = open("game_h.txt", "r")
    file.read(10)
    while(character != ","):
        character = file.read(1)
        player1.append(character)
    character = file.read(1)
    while(character != "]"):
        character = file.read(1)
        player2.append(character)
    file.close()
    if(player_num == 1):
        return player1
    else:
        return player2

def check_player(file_name, player1, player2, line):
    player = []
    if(file_name == "game_a.txt"):
        file = open("game_a.txt", "r")
    elif(file_name == "game_b.txt"):
        file = open("game_b.txt", "r")
    elif(file_name == "game_c.txt"):
        file = open("game_c.txt", "r")
    elif(file_name == "game_d.txt"):
        file = open("game_d.txt", "r")
    elif(file_name == "game_e.txt"):
        file = open("game_e.txt", "r")
    elif(file_name == "game_f.txt"):
        file = open("game_f.txt", "r")
    elif(file_name == "game_g.txt"):
        file = open("game_g.txt", "r")
    elif(file_name == "game_h.txt"):
        file = open("game_h.txt", "r")
    while(line > 1):
        character = file.readline()
        line = line -1
    character = ""
    while(character != " "):
        character = file.read(1)
        player.append(character)
    if(player == player1):
        file.close()
        return player1
    elif(player == player2):
        file.close()
        return player2
    else:
        file.close()
        return "winner"

def check_play(file_name, player, line):
    play = []
    if(file_name == "game_a.txt"):
        file = open("game_a.txt", "r")
    elif(file_name == "game_b.txt"):
        file = open("game_b.txt", "r")
    elif(file_name == "game_c.txt"):
        file = open("game_c.txt", "r")
    elif(file_name == "game_d.txt"):
        file = open("game_d.txt", "r")
    elif(file_name == "game_e.txt"):
        file = open("game_e.txt", "r")
    elif(file_name == "game_f.txt"):
        file = open("game_f.txt", "r")
    elif(file_name == "game_g.txt"):
        file = open("game_g.txt", "r")
    elif(file_name == "game_h.txt"):
        file = open("game_h.txt", "r")
    while(line > 1):
        character = file.readline()
        line = line -1
    character = file.read(player.len())
    character = file.read(1)
    while(character != "\n"):
        character = file.read(1)
        play.append(character)
    file.close()
    return play
        
# Problem 3
# Build yourself a 'coup' directory and make a file called coup.py there.
# Build a player class in coup.py
    # Data
        # Coins
        # Cards
        # log ### Whenever the game writes to its game file, it also writes
              ### to each player's log
    # act()
        # If you have fewer than 7 coins, tax. Else, coup another player
        # You might have to parse the log to find another active player's name.


# Problem 4
# Copy over your deck class from practice 2 to coup.py
# Add the draw() method, which returns the first (top) card in the deck
# and then removes that card from the deck

# Problem 5
# Build a class Game_Master in coup.py
    # Data:
        # players
        # gamefile (file opened by game_init() and closed when the game ends)
        # deck
    # Methods:
        # game_init() (Note, this is *not* the __init__ function)
            # Arguments: the names of the players
            # Initializes the deck with 5 cards (they can all be dukes for now)
            # Give each player 2 cards and 2 coins
        # turn()
            # Process one action, such as "a tax" or "markus steal daniel"
            # Check to see whether that action was valid
            # Write that action to a gamefile and each player's log
            # If a player had to discard, also write that action to a gamefile
            # Update player cards and coins accordingly
        # game()
            # initialize a game and call turn() until the game is over
# Play a FFA game with 3 players and submit the file in your practice_3
# directory (since your Game_Master class lives in another directory)

"""
The following problem is for Michael, Thomas, and Philip
"""
# Problem 6
# Assume your player class only plays 1v1 coup.
# What is the optimal strategy for a no blocking, no challenging coup?
# Adjust your player class to adopt this strategy.
# To receive 4/4 on this assignment, I must *not* be able to design
# An agent to beat your player (no matter who goes first)

"""
literaly just steal to 7+ coins and coup
"""