# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 15:49:10 2022

@author: Mike
"""

#problem 1
import random;
print (random.randint(1, 10));

#problem 2
for integer in range(1,101):
    print(integer * integer, "is the square of ", integer)
    
#problem 3
inFile = open("C:\\Users\\Mike\\Documents\\GitHub\\Coup_Instructor\\practice_1\\abab.txt", "r");
abab = inFile.read();
inFile.close();

ays = 0;
bys = 0;

for character in abab:
    if (character == 'a'):
        ays = ays + 1;
    elif (character == 'b'):
        bys = bys + 1;
        
print("There are", ays, "ays and there are", bys, "b's.")
    
#problem 4
inFile = open("C:\\Users\\Mike\\Documents\\GitHub\\Coup_Instructor\\practice_1\\abab.txt", "r");
abab = inFile.read();
inFile.close();

ays = 0;
bys = 0;
aiar = 0;
biar = 0;
wasa = False;
wasb = False;

for character in abab:
    if (character == 'a' and wasa):
        ays = ays + 1;
        wasb = False;
        if (ays > aiar):
            aiar = ays;
    elif (character == 'b' and wasb):
        bys = bys +1;
        wasa = False;
        if (bys > biar):
            biar = bys;
    elif (character == 'a'):
        ays = 1;
        wasa = True;
    elif (character == 'b'):
        bys = 1;
        wasb = True;
        
print("The longest number of a's in a row is", aiar, "and the longest number of b's in a row is", biar, "b's.")

#problem 5
rand1 = 0;
rand2 = 0;
rand3 = 0;
rand4 = 0;

import random;

#this loops and finds all working seeds, the first is 82682, second is 1841336, third is 1942544, etc.
for int in range(0, 2147483647):
    random.seed(int);
    rand1 = random.randint(10, 36);
    rand2 = random.randint(10, 36);
    rand3 = random.randint(10, 36);
    rand4 = random.randint(10, 36);
    if ((rand1 == 15) and (rand2 == 27) and (rand3 == 36) and (rand4 == 10)):
        print(int,':');
        print(rand1);
        print(rand2);
        print(rand3);
        print(rand4);