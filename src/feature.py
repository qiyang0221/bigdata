#!/usr/bin/python
import bookFeature as book
import rankFeature as rank

path = "../data"

book_class_path = path + "/book_class.txt"
book_path = path + "/train/book.txt"
rank_path = path + "/train/rank.txt"

features = rank.getFeature(rank_path)
bk_features = book.getFeature(book_path,book_class_path)

bk_feature_list = ['TP', 'TN', 'TM', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'J','O', 'bk_total']

for f in bk_feature_list:
    for key in features.keys():
        if key not in bk_features.keys():
            features[key][f] = 0
        else:
            features[key][f] = bk_features[key][f]
'''
for f in bk_feature_list:
    tot = 0
    for key in features.keys():
        tot += features[key][f]
    print "%s:%d\n"%(f,tot)

'''

for key in features.keys():
    print key,
    for kk in features[key].keys():
        print "%s:%d" % (kk,features[key][kk]),
    print

