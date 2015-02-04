# -*- coding: utf-8 -*- 
#coding=utf-8

import codecs
import numpy as np
import matplotlib.pyplot as plt
import utils

def libTime(time):
    time = time
    if time < 120000:
        return 0
    elif time >= 120000 and time < 180000:
        return 1
    elif time >= 180000 and time <= 223000:
        return 2
    return -1

def getFeature(infile,features):
    inLibAccessData = codecs.open(infile,'r')
    new_features = ['libacc0','libacc1','libacc2']
    features = utils.featureInit(features,new_features)

    line = inLibAccessData.readline()
    line = inLibAccessData.readline()
    while line:
        line = line.strip()
        listArray = line.split('\t')
        line = inLibAccessData.readline()
        
        sem = listArray[0]
        if infile.find('test') >= 0 and sem == '3':
            continue
        stu = int(listArray[1])
        date = utils.convertDate(sem,listArray[2])
        time = int(listArray[3])
        interval = libTime(time)
        if date == -1 or interval == -1:
            continue
        features[sem][stu][date]['libacc'+str(interval)] = 1

    inLibAccessData.close()

    return features
