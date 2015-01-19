#!/usr/bin/python

import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import rankFeature as rank


def draw(rank):
    fr = open("myscorefile.txt")
    line = fr.readline()

    score = []
    while line:
        line = line.strip()
        score.append(line)
        line = fr.readline()
   
    print len(score) 
    rk_1 = {}
    i = 0
    for key in sorted(rank.keys()):
        if i > 538:
            break
        rk_1[rank[key]['rank']] = score[i]
        i += 1

    x = [0 for i in range(538)]
    y = [0 for i in range(538)]
    i = 0
    for key in sorted(rk_1.keys()):
        x[i] = key
        y[i] = rk_1[key]
        print x[i],y[i]
        i += 1
    plt.plot(x,y)
    plt.xlabel("rank")
    plt.ylabel("score")
    plt.title("term_1")
    plt.show()

rk,mx = rank.getFeature('../data/train/rank.txt')
draw(rk)
