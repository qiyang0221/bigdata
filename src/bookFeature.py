#!/usr/bin/python
# -*- coding: utf-8 -*-  
#coding=utf-8

import utils

def bk_class_info(infile):
    bk_class_fr = open(infile)
    line = bk_class_fr.readline()  

    bk_class = {}
    line = bk_class_fr.readline()
    while line:
        line = line.strip()
        listArray = line.split('\t')
        bk_class[listArray[0]] = listArray[1]
        line = bk_class_fr.readline()
    bk_class_fr.close()
   
    return bk_class

def bookStatics(book_file,book_class):
    fr = open(book_file)
    line = fr.readline()
    line = fr.readline()

    bookInfo = {}
    while line:
        line = line.strip()
        listArray = line.split('\t')
        sem = listArray[0]
        if sem not in bookInfo.keys():
            bookInfo[sem] = {}

        book_index = listArray[2]
        if book_class.has_key(book_index):
            book_kind = book_class[book_index]
            if book_kind not in bookInfo[sem].keys():
                bookInfo[sem][book_kind] = 0
            bookInfo[sem][book_kind] += 1
        line = fr.readline()

    ret = {}
    for sem in sorted(bookInfo.keys()):
        ret[sem] = {}
        backitems=[[v[1],v[0]] for v in bookInfo[sem].items()]
        backitems.sort()
        size = len(backitems)
        for i in range(6):
            ret[sem][backitems[size - i - 1][1]] = 'book_'+str(i)
    return ret

def getFeature(book_file_name,book_class_file_name,features):    
    bk_class = bk_class_info(book_class_file_name)

    #feature_list = ['TV','TT', 'TU', 'TS', 'TP', 'TQ', 'TN', 'TL', 'TM', 'TJ', 'TK', 'TH', 'TF', 'TG','TD', 'TE', 'TB', 'A', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'J', 'M', 'L', 'O', 'N', 'Q', 'P', 'S', 'R', 'U', 'T', 'V', 'Y', 'X', 'Z'] 
    #add new features
   
    new_features_map = bookStatics(book_file_name,bk_class)
    '''
    for sem in new_features_map.keys():
        print sem+':'
        for bk_kind in new_features_map[sem].keys():
            print "%s:%s" %(bk_kind,new_features_map[sem][bk_kind]),
        print
    '''
    new_features = ['book_0','book_1','book_2','book_3','book_4','book_5']

    features = utils.featureInit(features,new_features)

 
    bk_fr = open(book_file_name)
    line = bk_fr.readline()
    line = bk_fr.readline()
    while line:
        line = line.strip()
        listArray = line.split('\t')
        line = bk_fr.readline()

        sem = listArray[0]
        if book_file_name.find('test') >= 0 and sem == '3':
            continue
        stu = int(listArray[1])
        book_index = listArray[2]
        date = utils.convertDate(sem,listArray[3])
        if date == -1:
            continue

        if book_index in bk_class.keys():
            book_kind = bk_class[book_index]
            if book_kind in new_features_map[sem].keys():
                features[sem][stu][date][new_features_map[sem][book_kind]] = 1
    bk_fr.close()

    return features

'''
book_file_path = '../data/train/book.txt'
book_class_file_path = '../data/book_class.txt'

getFeature(book_file_path,book_class_file_path)
'''
