#!/usr/bin/python
# -*- coding: utf-8 -*-  
#coding=utf-8
import bookFeature as book
import rankFeature as rank
import libAccessFeature as libaccess
import consumeFeature as consume
import featurePlot as fp
import utils

path = "../data"

directory = '/train'

book_class_path = path + '/book_class.txt'
book_path = path + directory + '/book.txt'
rank_path = path + directory + '/rank.txt'
libaccess_path = path + directory + '/lib_time.txt'
consume_path = path + directory + '/consume.txt'

features,mx_rk = rank.getFeature(rank_path)

features = book.getFeature(book_path,book_class_path,features)
features = consume.getFeature(consume_path,features)
features = libaccess.getFeature(libaccess_path,features)

for sem in features.keys():
    for stu in features[sem].keys():
        print sem,stu,
        print "rank:%d" %(features[sem][stu]['rank']),
        for date in range(utils.getDateLen()):
            for ft in features[sem][stu][date].keys():
                print '%s:%d' %(str(date) +ft,features[sem][stu][date][ft]),
        print
