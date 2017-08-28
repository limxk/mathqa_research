# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:19:29 2017

@author: Kai
"""

import csv
import random
import glob
import os

full_combined_data = []
Questions = []
Answers = []

sameness=True

with open('Clean_Data/combined_data.csv', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader, None)
    for row in spamreader:
        full_combined_data += [row]
        Questions += [ row[2] + ' ' + row[3] ]
        Answers += [ row[6] ]


