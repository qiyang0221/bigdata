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

'''
for key in sorted(features.keys()):
    print mx_rk-features[key]['rank'],
    key_arr = key.split('.')
    print 'qid:%s' % key_arr[0],

    i = 1
    for kk in sorted(features[key].keys()):
        if not kk == 'rank':
            print "%d:%f" % (i,features[key][kk]),
            i += 1
    print
'''
'''
for f in bk_feature_list:
    tot = 0
    for key in features.keys():
        tot += features[key][f]
    print "%s:%d\n"%(f,tot)

'''

'''
for key in sorted(features.keys()):
    print key,
    for kk in sorted(features[key].keys()):
        print "%s:%d" % (kk,features[key][kk]),
    print
'''
