#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:42:09 2020

@author: Margaret
"""
import os
import math

currentDir = os.getcwd()
print(currentDir)

#os.chdir('/Users/glove.6B')

#read in GloVe file and put into a list of vector string entries
def readVectors(file):
    print("Working on it!")
    strings = []
    with open(file, "r") as Glove:
        for entry in Glove:
            strings.append(entry)
    #print here to see example vector 50 as a string
    #print(strings[50])
    global vectors
    vectors = []
    for string in strings:
        vectors.append(string.split())
    #print here to see an example vector as a list
    #print(vectors[50])
    print("And done! Call object \'vectors\' to see your list of vectors, though you might want to index it instead.")



#loop through vector entries and return critical vectors
def findVec(w1, w2):
    v1s = []
    v2s = []
    for vector in vectors:
        if vector[0] == w1:
            v1s.extend(vector)
        elif vector[0] == w2:
                v2s.extend(vector)
        else:
            continue
    #print here for full vectors with word label
    #print(v1s)
    #print(v2s)
    v1 = [float(n) for n in v1s[1:]]
    v2 = [float(n) for n in v2s[1:]]
    #print here for vectors as floats without word label
    #print(v1)
    #print(v2)
    #find the cosine of the two vectors
    #1: get dot product of v1 and v2
    dotP1 = [v1[f] * v2[f] for f in range(len(v1))]
    #print here for the vector multiplication step of the dotProduct of the vectors
    #print(dotP1)
    dotP = sum(dotP1)
    #print here for the sum step of the dotProduct
    #print(dotP)
    #2: find ||v1|| & ||v2||
    #2.1 find ||v1||
    v1SQ = [n*n for n in v1]  #find square of each # in v1 vector
    v1SQ_sum = sum(v1SQ)  #find sum of all squares
    v1_sqrt = math.sqrt(v1SQ_sum)  #find sqrt of sum
    #print here for the sum of square and sqrt for first vector
    #print(v1SQ)
    #print(v1_sqrt)
    #2.2 find ||v2||
    v2SQ = [n*n for n in v2] 
    v2SQ_sum = sum(v2SQ)
    v2_sqrt = math.sqrt(v2SQ_sum)
    #print here for sum of squares and sqrt for second vector
    #print(v2SQ)
    #print(v2_sqrt)
    #3: find ||v1|| ||v2||
    denom = v1_sqrt * v2_sqrt
    #print here for denominator of cosine formula
    #print(denom)
    #4 fine cosine
    cos = dotP/denom
    print('The cosine for \'%s\' and \'%s\' is %f' % (v1s[0], v2s[0], cos))
    #add cosine to final list
    cosines = []
    cosines.append("%s %s %f" % (v1s[0], v2s[0],cos))
    print('Your cosine has been added to the file cosines.txt')
    #export to file once complete
    with open("cosines.txt", "a") as output:
        output.write(str(cosines))

#use to import a file of word vectors; assumes each entry is on its own line in a text file
readVectors("glove.6B.50d.txt")

#use to find the cosine of two word vectors, e.g. neighbors and rats
findVec('neighbors', 'rats')
