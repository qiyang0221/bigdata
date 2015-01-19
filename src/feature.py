#!/usr/bin/python
# -*- coding: utf-8 -*-  
#coding=utf-8
import bookFeature as book
import rankFeature as rank
import libAccessFeature as libaccess
import consumeFeature as consume

path = "../data"

directory = '/test'

book_class_path = path + '/book_class.txt'
book_path = path + directory + '/book.txt'
rank_path = path + directory + '/rank.txt'
libaccess_path = path + directory + '/lib_time.txt'
consume_path = path + directory + '/consume.txt'

features,mx_rk = rank.getFeature(rank_path)
bk_features = book.getFeature(book_path,book_class_path)

bk_feature_list = ['TP', 'TN', 'TM', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'J','O', 'bk_total']

for f in bk_feature_list:
    for key in features.keys():
        if key not in bk_features.keys():
            features[key][f] = 0
        else:
            features[key][f] = bk_features[key][f]


libaccess_features = libaccess.getFeature(libaccess_path)
libaccess_feature_list = [0,1,2,3,4,5]
for f in libaccess_feature_list:
    for key in features.keys():
        if key not in libaccess_features.keys():
            features[key][f] = 0
        else:
            features[key][f] = libaccess_features[key][f]

consume_features = consume.getFeature(consume_path)
consume_feature_list = ['打印','图书馆','宿舍','教室','超市','食堂','交通','con_total']
for f in consume_feature_list:
    for key in features.keys():
        if key not in consume_features.keys():
            features[key][f] = 0
        else:
            features[key][f] = consume_features[key][f]

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
