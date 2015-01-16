# -*- coding: utf-8 -*-  
#coding=utf-8

__author__ = 'Connor'

import codecs
import numpy as np
import matplotlib.pyplot as plt

# 指定路径就可以了，绝对路径和相对路径都是可以的

def getFeature(infile):
    # features: 第1、3学期是9,10,11,12,1月，第2学期是3,4,5,6,7月份的图书馆门禁数据 keys:[0,1,2,3,4,5],5代表总数
    inLibAccessData = codecs.open(infile,'r')
    data = {}
    ms = [i for i in range(5)]
    cnt = 0
    line = inLibAccessData.readline()
    line = inLibAccessData.readline()
    while line:# and cnt < 50:
        line = line.strip()
        tmp = line.split('\t')
        semester = tmp[0]
        sid = int(tmp[1])

        key = semester+ '_' + str(sid)
        date = tmp[2]
        month = date[:2]
        if month == '02':
            line = inLibAccessData.readline()
            continue
        mm = convertMonth(semester,month)

        if key not in data.keys():
            data[key] = {}
            for m in ms:
                data[key][m] = 0
            data[key][mm] = 1
            data[key][5] = 1
        else:
            data[key][mm] += 1
            data[key][5] += 1
        cnt += 1
        line = inLibAccessData.readline()
    inLibAccessData.close()

    return data

def convertMonth(semester,month):
    mm = int(month)
    if semester == '1' or semester =='3':
        mm -=9
        if mm < 0:
            mm += 12
        mm %= 5
    if semester == '2':
        mm -= 3
        mm %= 5
    return mm

'''
def draw(dictionary,feature):
   y = np.zeros(len(dictionary))
   i = 0
   for key in sorted(dictionary.keys()):
       y[i] = dictionary[key][feature]
       if y[i]>10000:
           print(key)
       i += 1

   x = range(len(dictionary))

   plt.plot(x,y)
   plt.xlabel("student")
   plt.ylabel(feature)
   plt.title(feature)
   if type(feature) != str:
       save_name = str(feature) + '.png'
   else:
       save_name = feature + '.png'
   plt.savefig(save_name)
   plt.show()


if __name__ == '__main__':
    # data = getConsume('E:\\data\\bigData\\training\\消费.txt')

    data = getLibAccess('E:\\data\\bigData\\training\\图书馆门禁.txt')
    total_feature =[0,1,2,3,4]
    for feature in total_feature:
        draw(data,feature)
    draw(data,5)

    data = getConsume('E:\\data\\bigData\\training\\消费.txt')
    total_feature =['打印','图书馆','宿舍','教室','超市','食堂','交通']
    for feature in total_feature:
        draw(data,feature)
    draw(data,'total')
'''
