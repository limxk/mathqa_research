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

