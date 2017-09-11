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

def remove_doubles(term):
    """
    Removes duplicate symbols of "$$"

    Args:
        term: string to be checked.

    Returns:
        String where "$$" is reduced to "$".
    """
    tempstr=""   
    
    for i in range( len(term) ):

        if i < len(term)-1:
            if not( (term[i]==term[i+1]) and (term[i] == "$") ): tempstr += term[i]
        else:
            tempstr += term[i]
    return tempstr

for i in range ( len(Questions) ):
    Questions[i] = remove_doubles(Questions[i])
    Answers[i] = remove_doubles(Answers[i])

if not os.path.exists('Clean_Data/combined_data1_nodoubles.csv'):
    open('Clean_Data/combined_data1_nodoubles.csv', 'w+')

if os.path.getsize('Clean_Data/combined_data1_nodoubles.csv') < 1 :
    with open('Clean_Data/combined_data1_nodoubles.csv', 'w', newline="", encoding="utf8") as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['Questions']+['Answers'])
        
        for i in range ( len(Questions) ):
            spamwriter.writerow([Questions[i]]+[Answers[i]])

def remove_tags(term, i):
    """
    Removes html tags and "\n"

    Args:
        term: string to be checked.

    Returns:
        String with html tags and "\n" removed
    """
    tempstr=""   
    istag = False
    isformula = False
    for x in term:
        if x == "$": 
            tempstr += x
            isformula = not(isformula)
        
        if isformula:
            tempstr += x
        else:
            if x == "<":
                if istag: print("sumtingwrong1 " + str(i) + term)
                istag=True
            if not(istag):
                if x == "\n": tempstr += " "
                else: tempstr += x
            if x == ">":
                if not(istag): print("sumtingwrong2 " + str(i) + term)
                istag=False
                tempstr += " "
    
    if istag: print("sumting wrong3")
    if isformula: print("sumting wrong4")
    return tempstr

for i in range ( len(Questions) ):
    Questions[i] = remove_tags(Questions[i], i)
    Answers[i] = remove_tags(Answers[i], i)

if not os.path.exists('Clean_Data/combined_data2_notags.csv'):
    open('Clean_Data/combined_data2_notags.csv', 'w+')

if os.path.getsize('Clean_Data/combined_data2_notags.csv') < 1 :
    with open('Clean_Data/combined_data2_notags.csv', 'w', newline="", encoding="utf8") as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['Questions']+['Answers'])
        
        for i in range ( len(Questions) ):
            spamwriter.writerow([Questions[i]]+[Answers[i]])

def is_function(term):
    """
    Checks if the term is a LaTeX function.

    Source: https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols

    Args:
        term: string to be checked.

    Returns:
        True if the term is a function, False otherwise.
    """
    function_terms = tuple()

    # binary operators
    operator_terms += ('pm', 'times', 'div', 'ast', 'dot', 'cap', 'cup',
                       'vee', 'wedge', '+', '-', 'times', 'plus',
                       u'\xb1', u'\xd7', u'\xf7', u'\u2212', u'\u2215',
                       u'\u2216', u'\u2217', u'\u2218', u'\u2219', u'\u221D',
                       u'\u221E', u'\u221F', u'\u2220', u'\u2225', u'\u2227',
                       u'\u2228', u'\u2229', u'\u222A')

    # relation operators
    operator_terms += ('leq', 'geq', 'equiv', 'nequiv', 'models', 'sim',
                       'simeq', 'mid', 'parallel', 'subset', 'supset',
                       'approx', 'subseteq', 'supseteq', 'cong', 'join', 'neq',
                       'proptoin', '=', '<', '>',
                       u'\u2260', u'\u2261', u'\u2262', u'\u2263', u'\u2264',
                       u'\u2265', u'\u2266', u'\u2267', u'\u2243',
                       u'\u2282', u'\u2283', u'\u2284', u'\u2285', u'\u2286',
                       u'\u2287', u'\u2288', u'\u2289', u'\u228A', u'\u228B',
                       u'\u2A1D', u'\u2223', u'\u2239', u'\u223C', u'\u223D',
                       u'\u2242', u'\u2243', u'\u2244', u'\u2245', u'\u2246',
                       u'\u2247', u'\u2248', u'\u2249', u'\u224A', u'\u224B',
                       u'\u224C', '!')

    # punctuation operators
    operator_terms += (',', 'colon', 'ldotp', 'cdotp', u'\u2234', u'\u2235',
                       u'\u2236', u'\u2237')

    # arrow operators
    operator_terms += ('leftarrow', 'Leftarrow', 'rightarrow', 'Rightarrow',
                       'leftrightarrow', 'Leftrightarrow', 'leftharpoonup',
                       'leftharpoondown', 'rightleftharpoons',
                       'rightharpoonup', 'rightharpoondown', 'mapsto')
    # miscellaneous operators
    operator_terms += ('ldots', 'cdots', 'vdots', 'ddots', 'forall', 'infty',
                       'exists', 'nabla', 'neg', 'triangle', 'angle', 'bot',
                       'prime', 'emptyset', u'\u2026')
    # vars sized operators
    operator_terms += ('prod', 'coprod', 'bigcap', 'bigcup',
                       'bigodot', 'bigotimes', 'bigoplus')
    # delimiter operators
    operator_terms += ('(', ')', 'uparrow', 'Uparrow', '[', ']',
                       'downarrow', 'Downarrow', '{', '}', 'updownarrow',
                       'Updownarrow', 'lfloor', 'rfloor', 'lceil', 'rceil',
                       'langle', 'rangle', '/', 'backslash', '|', 'lgroup',
                       'rgroup', '\\', '.', '\'')
    # other operators
    operator_terms += ('widetilde', 'widehat', 'overleftarrow',
                       'overrightarrow', 'overline', 'underline',
                       'overbrace', 'underbrace')

    return term.endswith(function_terms)

