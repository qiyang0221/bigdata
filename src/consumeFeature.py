# -*- coding: utf-8 -*-  
#coding=utf-8

import codecs
import utils

'''
def getFeature(infile):

    #features: 消费数据['打印','图书馆','宿舍','教室','超市','食堂','交通','con_total']
    inConsumeData = codecs.open(infile,'r')
    data = {}
    locations = {'打印':'copy','图书馆':'lib','宿舍':'apartment','教室':'classroom','超市':'supermarket','食堂':'eat','交通':'transport'}
    cnt = 0
    line = inConsumeData.readline()
    line = inConsumeData.readline()
    while line:# and cnt < 500:
        line = line.strip()
        tmp = line.split('\t')
        semester = tmp[0]
        sid = int(tmp[1])
        key = semester+ '.' + str(sid)

        loc = tmp[2]
        money = round(float(tmp[5]),3)
        if key not in data.keys():
            data[key] = {}
            for val in locations.values():
                data[key][val] = 0
            data[key][locations[loc]] = money
            data[key]['con_total'] = money
        else:
            data[key][locations[loc]] += money
            data[key]['con_total'] += money
        cnt += 1
        line = inConsumeData.readline()
    inConsumeData.close()

    return data
'''

def eatTime(time):
    if time < 90000:
        return 0
    elif time >= 113000 and time < 140000:
        return 1
    elif time >= 170000 and time < 190000:
        return 2
    return -1

def dormTime(time):
    if time > 60000 and time < 90000:
        return 0
    elif time > 113000 and time < 133000:
        return 1
    elif time > 213000:
        return 2
    return -1

def otherTime(time):
    if time < 120000:
        return 0
    elif time >= 120000 and time < 180000:
        return 1
    elif time >= 180000:
        return 2
    return -1

def getFeature(infile,features):
    fr = codecs.open(infile,'r')

    new_features = ['copy0','copy1','copy2','lib0','lib1','lib2','dorm0','dorm1','dorm2','classroom0','classroom1','classroom2','supermarket0','supermarket1','supermarket2','eat0','eat1','eat2','transport0','transport1','transport2']
    locations = {'打印':'copy','图书馆':'lib','宿舍':'dorm','教室':'classroom','超市':'supermarket','食堂':'eat','交通':'transport'}
    features = utils.featureInit(features,new_features)

    line = fr.readline()
    line = fr.readline()
    while line:
        line = line.strip()
        listArray = line.split('\t')
        line = fr.readline()

        sem = listArray[0]
        if infile.find('test') >= 0 and sem == '3':
            continue
        stu = int(listArray[1])
        loc = locations[listArray[2]]
        date = utils.convertDate(sem,listArray[3])
        time = int(listArray[4])
        interval = -1
        
        if loc == 'dorm':
            interval = dormTime(time)
        elif loc == 'eat':
            interval = eatTime(time)
        else:
            interval = otherTime(time)
        if date == -1 or interval == -1:
            continue
        features[sem][stu][date][loc+str(interval)] = 1    
    return features
