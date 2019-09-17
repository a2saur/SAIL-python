# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:58:38 2019

@author: Me
"""

myList = ['Hi', 'Hello', 'Hey', 'Whats Up?']
myArr = ['I ', 'Think ', 'That ', 'This ', 'Is ', 'An ', 'Array.']
myTup = ('A ', 'Tuple!', 'Wow!')
myDict = {'Dictionary': 'That is what this is', 'Tuple': 'This is not a tuple', 'Array': 'This is not an Array, either', 'List': 'This is not a list'}
mySet = {'Is ', 'This ', 'A ', 'Set?'}
myFile = open('A_file.txt', 'r')
words = myFile.read()

x = [myList, myArr, myTup, myDict, mySet, words]
y = [' list', ' array', ' tuple', ' dictionary', ' set', 'file']

lf = 'List item indexes start at 0.\nIf you want the last item in the list, you can just use the index -1.\nTo get the first item from a list, let\'s say "myList," type myList[0].'
af = 'In python, an array is the same thing as a list.'
tf = 'A tuple is basically the same thing as a list, except unlike a list, a tuple cannot be modified'
df = 'Unlike the tuple and list, you can define the indexes of a dictionary. For example, assuming it was in my dictionary, I could write myDictionary[\'Frog\'] and it would pull up whatever is at the location \'Frog.\''
sf = 'Unlike the list, you cannot have two of the same items in one set.'
ff = 'There are many different types of files. You could open a text file, a csv (comma seperated values) file, or another python file.'

fact = [lf, af, tf, df, sf, ff]
for n in range(len(x)):
    print('Here is an example of a(n)', y[n], ':')
    print(x[n])
    print(fact[n])
    print('\n')