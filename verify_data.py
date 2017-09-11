# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:19:29 2017

@author: Kai
"""

import csv
import random
import glob
import os


Questions = []
Answers = []
Questionid=[]
Answerid=[]

with open('Clean_Data/combined_data3_nosymbols.csv', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader, None)
    for row in spamreader:
        Questions += [ row[2] ]
        Answers += [ row[3] ]
        Questionid += [ row[0] ]
        Answerid += [ row[1] ]

Questionsplit = []
Answersplit = []

for i in range ( len(Questions) ):
    Questionsplit += [ Questions[i].split() ]
    Answersplit += [ Answers[i].split() ]
    if i%10000 == 0: print("Splitting tokens : " + str(i))

errorcount = 0
Questionerrorindex=[]
Answererrorindex=[]

for i in range ( len(Questions) ):
    
    toolong = False
    
    for j in range ( len(Questionsplit[i]) ):
        if len( Questionsplit[i][j] ) > 50 and not(Questionsplit[i][j][0]=="$") : 
            toolong = True
            print("Question token too long at question " + str(i) + " index " + str(j) )
            Questionerrorindex += [ [i,j] ]
    for j in range ( len(Answersplit[i]) ):
        if len( Answersplit[i][j] ) > 50 and not(Answersplit[i][j][0]=="$"): 
            toolong = True
            print("Answer token too long at question " + str(i) + " index " + str(j) )
            Answererrorindex += [ [i,j] ]
    if toolong: errorcount += 1

def printerror(count):
    
    for k in range(count):
        n = random.randrange(len(Questionerrorindex))
        i = Questionerrorindex[n][0] ; j = Questionerrorindex[n][1]
        print("Question " + str(i) + " index " + str(j) + "\n" +  Questionsplit[i][j])
        n = random.randrange(len(Answererrorindex))
        i = Answererrorindex[n][0] ; j = Answererrorindex[n][1]
        print("Answer " + str(i) + " index " + str(j) + "\n" +  Answersplit[i][j])
    

