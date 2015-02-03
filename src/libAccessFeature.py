# -*- coding: utf-8 -*-  
#coding=utf-8

__author__ = 'Connor'

import codecs
import numpy as np
import matplotlib.pyplot as plt
import utils

def libTime(time):
    time = time / 1000
    if time < 113:
        return 0
    elif time > 133 and time < 170:
        return 1
    elif time > 183 and time < 223:
        return 2
    return -1

def getFeature(infile,features):
    # features: 第1、3学期是9,10,11,12,1月，第2学期是3,4,5,6,7月份的图书馆门禁数据 keys:[0,1,2,3,4,5],5代表总数
    inLibAccessData = codecs.open(infile,'r')
    new_features = ['libacc_0','libacc_1','libacc_2']
    features = utils.featureInit(features,new_features)
    
    line = inLibAccessData.readline()
    line = inLibAccessData.readline()
    while line:# and cnt < 50:
        line = line.strip()
        listArray = line.split('\t')
        line = inLibAccessData.readline()

        sem = listArray[0]
        stu = listArray[1]
        date = utils.convertDate(listArray[2])
        time = listArray[3]
        interval = libTime(time)
        if date == -1 or interval == -1:
            continue
        features[sem][stu][date][interval] = 1

    inLibAccessData.close()

    return features
