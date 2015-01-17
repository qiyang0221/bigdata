import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import rankFeature as rank


def draw(rank):
    fr = open("myscore.txt")
    fr.readline()
    fr.readline()

    score = []
    int i = 0
    while line:
        line = line.strip()
        score[i] = line
        i += 1
        line = fr.readline()
    
    int rk = []
    for key in sorted(rank.keys()):
        rk.append(rank[key]['rank'])

    x1 = rk[0:91]
    y1 = score[0:91]
    plt.plot(x,y)
    plt.xlabel("rank")
    plt.ylabel("score")
    plt.title("term_1")
    plt.show()

    x2 = rk[92:]
    y2 = socre[92:]
    plt.plot(x,y)
    plt.xlabel("rank")
    plt.ylabel("score")
    plt.title("term_2")
    plt.show()
 

rk,mx = rank.getFeature()
draw(rk)
