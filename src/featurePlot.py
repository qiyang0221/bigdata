#-*- coding: utf-8 -*-
#coding=utf-8

import matplotlib
import matplotlib.pyplot as plt
from numpy import *

'''
def draw(dictionary,feature):
   y = zeros(len(dictionary))
   i = 0
   for key in dictionary.keys():
       y[i] = dictionary[key][feature]
       i += 1
   
   x = range(len(dictionary))

   plt.plot(x,y)
   plt.xlabel("student")
   plt.ylabel(feature)
   plt.title(feature)
   plt.show()
'''

def draw(dictionary, feature):
   rank = {}
   for key in dictionary.keys():
       keyArr = key.split('.')
       sem = keyArr[0]
       if sem not in rank.keys():
           rank[sem] = {}
       rank[sem][int(dictionary[key]['rank'])] =dictionary[key][feature]

   for key in sorted(rank.keys()):
       size = len(rank[key])
       x = range(size)
       y = range(size) 
       i = 0
       for kk in sorted(rank[key].keys()):
           x[i] = kk
           y[i] = rank[key][kk]
           i += 1
       
       fig = plt.figure()
       ax = fig.add_subplot(111)
       ax.scatter(x,y)
       plt.xlabel('rank')
       plt.ylabel(feature)
       plt.title('sem:' + str(key) )
       plt.show()
