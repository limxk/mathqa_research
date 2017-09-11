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

with open('Clean_Data/combined_data.csv', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile)
    next(spamreader, None)
    for row in spamreader:
        Questions += [ row[2] + ' ' + row[3] ]
        Answers += [ row[6] ]
        Questionid += [ row[0] ]
        Answerid += [ row[1] ]

#Remove "\n" and duplicate "$$"
def replace_dollar(term):
    """
    Changes all latex delimiters to "$"

    Args:
        term: string to be checked.

    Returns:
        String where all latex delimiters is reduced to "$" and "\n" replaced by " "
    """
    
    term = term.replace("$$","$")
    term = term.replace("<code>", "$")
    term = term.replace("</code>", "$")
    #random character to denote alternative latex starting delimiters
    term = term.replace("\\begin{align}", "\a")
    term = term.replace("\\begin{align*}", "\a") 
    term = term.replace("\\begin{aligned}", "\a")
    term = term.replace("\\begin{equation}", "\a")
    #random character to denote alternative latex ending delimiters
    term = term.replace("\\end{align}", "\b")
    term = term.replace("\\end{align*}", "\b")
    term = term.replace("\\end{aligned}", "\b")
    term = term.replace("\\end{equation}", "\b")
    
    term = term.replace("\n", " ")
    
    term = term.replace("\$", " ") #remove "$" symbols from text as well
    
    return term

for i in range ( len(Questions) ):
    Questions[i] = replace_dollar(Questions[i])
    Answers[i] = replace_dollar(Answers[i])
    if i%10000 == 0: print("Replacing $ sign : question " + str(i))

if not os.path.exists('Clean_Data/combined_data1_replacedollar.csv'):
    open('Clean_Data/combined_data1_replacedollar.csv', 'w+')

if os.path.getsize('Clean_Data/combined_data1_replacedollar.csv') < 1 :
    with open('Clean_Data/combined_data1_replacedollar.csv', 'w', newline="", encoding="utf8") as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['Questionid']+['Answerid']+['Questions']+['Answers'])
        
        for i in range ( len(Questions) ):
            spamwriter.writerow([Questionid[i]]+[Answerid[i]]+[Questions[i]]+[Answers[i]])

#Remove html tags 
def remove_html(term):
    """
    Remove html tags from text

    Args:
        term: string to be checked.

    Returns:
        String where html tags are replaced by " ". We try to ignore "<" and ">" used in latex formulae.
    """
    tempstr=""
    tempstr2=""
    is_html = False
    
    for x in term:
        
        if x == "<":
            if is_html:
                tempstr += tempstr2
                tempstr2 = x
            else:
                is_html = True
                tempstr2 = x                
        elif x == ">":
            if is_html:
                is_html = False
                tempstr += " "
                tempstr2 = ""
            else:
                tempstr += x
        elif is_html:
            tempstr2 += x
        else:
            tempstr += x
            
    return tempstr

for i in range ( len(Questions) ):
    Questions[i] = remove_html(Questions[i])
    Answers[i] = remove_html(Answers[i])
    if i%10000 == 0: print("Removing html tags : question " + str(i))

if not os.path.exists('Clean_Data/combined_data2_nohtml.csv'):
    open('Clean_Data/combined_data2_nohtml.csv', 'w+')

if os.path.getsize('Clean_Data/combined_data2_nohtml.csv') < 1 :
    with open('Clean_Data/combined_data2_nohtml.csv', 'w', newline="", encoding="utf8") as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['Questionid']+['Answerid']+['Questions']+['Answers'])
        
        for i in range ( len(Questions) ):
            spamwriter.writerow([Questionid[i]]+[Answerid[i]]+[Questions[i]]+[Answers[i]])



#Remove symbols and clean up formulae
def remove_symbols(term):
    """
    Remove non-alphanumeric symbols from text
    Additionally, remove spaces from formulae

    Args:
        term: string to be checked.

    Returns:
        String where only alphanumerals and spaces are retained in text, and spaces removed in formulae
    """
    tempstr=""
    is_formula = False
    is_alt_formula = False
    
    for x in term:
        
        if x == "$":
            is_formula = not(is_formula)
            if is_formula:
                tempstr += " $"
            else:
                tempstr += "$ "
        elif x == "\a":
            if not(is_formula): 
                tempstr += " $"
                is_alt_formula = True
        elif x == "\b":
            if is_alt_formula: 
                tempstr += "$ "
                is_alt_formula = False
        elif is_formula or is_alt_formula:
            if not(x == " "): tempstr += x
        else:
            if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 " : tempstr += x
            
    return tempstr


for i in range ( len(Questions) ):
    Questions[i] = remove_symbols(Questions[i])
    Answers[i] = remove_symbols(Answers[i])
    if i%10000 == 0: print("Removing symbols : question " + str(i))
    
if not os.path.exists('Clean_Data/combined_data3_nosymbols.csv'):
    open('Clean_Data/combined_data3_nosymbols.csv', 'w+')

if os.path.getsize('Clean_Data/combined_data3_nosymbols.csv') < 1 :
    with open('Clean_Data/combined_data3_nosymbols.csv', 'w', newline="", encoding="utf8") as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['Questionid']+['Answerid']+['Questions']+['Answers'])
        
        for i in range ( len(Questions) ):
            spamwriter.writerow([Questionid[i]]+[Answerid[i]]+[Questions[i]]+[Answers[i]])

"""
for i in range ( len(Questions) ):
    Questions[i] = Questions[i].split()
    Answers[i] = Answers[i].split()
    if i%10000 == 0: print("Splitting tokens : " + str(i))

if not os.path.exists('Clean_Data/combined_data4_final.csv'):
    open('Clean_Data/combined_data4_final.csv', 'w+')

if os.path.getsize('Clean_Data/combined_data4_final.csv') < 1 :
    with open('Clean_Data/combined_data4_final.csv', 'w', newline="", encoding="utf8") as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['Questionid']+['Answerid']+['Questions']+['Answers'])
        
        for i in range ( len(Questions) ):
            spamwriter.writerow([Questionid[i]]+[Answerid[i]]+[Questions[i]]+[Answers[i]])
"""
            

