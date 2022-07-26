# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 20:05:39 2022

@author: Mike
"""

import pickle

# problem 1
rick = open("test.pkl", "rb")
im_a_pickle = pickle.load(rick)
print(type(im_a_pickle))
rick.close()

# im_a_pickle is a dictionary that gives the lyrics to a fantastic song
print("never", im_a_pickle["never"][0], "\n" + "never", im_a_pickle["never"][1], "\n" + "never", im_a_pickle["never"][2])
