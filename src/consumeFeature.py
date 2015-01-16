# -*- coding: utf-8 -*-  
#coding=utf-8

import codecs

def getFeature(infile):

    #features: 消费数据['打印','图书馆','宿舍','教室','超市','食堂','交通','con_total']
    inConsumeData = codecs.open(infile,'r')
    data = {}
    locations = ['打印','图书馆','宿舍','教室','超市','食堂','交通']
    cnt = 0
    line = inConsumeData.readline()
    line = inConsumeData.readline()
    while line:# and cnt < 500:
        line = line.strip()
        tmp = line.split('\t')
        semester = tmp[0]
        sid = int(tmp[1])
        key = semester+ '_' + str(sid)

        location = tmp[2]
        money = round(float(tmp[5]),3)
        if key not in data.keys():
            data[key] = {}
            for loc in locations:
                data[key][loc] = 0
            data[key][location] = money
            data[key]['con_total'] = money
        else:
            data[key][location] += money
            data[key]['con_total'] += money
        cnt += 1
        line = inConsumeData.readline()
    inConsumeData.close()
    return data
