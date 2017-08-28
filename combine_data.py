# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:19:29 2017

@author: Kai
"""

import csv
import random
import glob
import os

Qquestionid = []
Qanswerid = []
Qtitle = []
Qbody = []

Aquestionid = []
Aanswerid = []
Abody = []

questionfiles = glob.glob('Raw_Data/Q/*.csv')

for file in questionfiles:
    with open(file, encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader, None)
        for row in spamreader:
            Qquestionid+=[row[0]]
            Qanswerid+=[row[1]]
            Qtitle+=[row[2]]
            Qbody+=[row[3]]

answerfiles = glob.glob('Raw_Data/A/*.csv')

for file in answerfiles:
    with open(file, encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader, None)
        for row in spamreader:
            #print(row[0])
            Aquestionid+=[row[0]]
            Aanswerid+=[row[1]]
            Abody+=[row[2]]

#Verify that questions are paried with correct answers
'''
questionsameness = True
answersameness = True

for i in range( len(Qquestionid) ):
    questionsameness = questionsameness and Qquestionid[i] == Aquestionid[i]
    answersameness = answersameness and Qanswerid[i] == Aanswerid[i]
    if not(questionsameness and answersameness):
        print("not same index : " + str(i))
        questionsameness = True
        answersameness = True

print( " questionsameness : " + str(questionsameness))
print( " answersameness : " + str(answersameness))

for l in range(10):
    j = random.randint(0, len(Qquestionid) )
    print( "Qqeustionid : " + Qquestionid[j] + " Aquestionid : " + Aquestionid[j] )
    k = random.randint(0, len(Qanswerid)-1)
    print( "Qanswerid : " + Qanswerid[k] + " Aanswerid : " + Aanswerid[k] )
'''

if os.path.getsize('Clean_Data/combined_data.csv') < 1 :
    with open('Clean_Data/combined_data.csv', 'w', newline='', encoding="utf8") as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['Qquestionid']+['Qanswerid']+['Qtitle']+['Qbody']+['Aquestionid']+['Aanswerid']+['Abody'])
        
        for i in range ( len(Qquestionid) ):
            spamwriter.writerow([Qquestionid[i]]+[Qanswerid[i]]+[Qtitle[i]]+[Qbody[i]]+[Aquestionid[i]]+[Aanswerid[i]]+[Abody[i]])
