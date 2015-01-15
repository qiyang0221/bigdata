import matplotlib
import matplotlib.pyplot as plt
from numpy import *

def getFeature(book_file_name,book_class_file_name):
    bk_class_fr = open(book_class_file_name)
    line = bk_class_fr.readline()  

    bk_class = {}
    bk_class_set = set()
    line = bk_class_fr.readline()
    while line:
        line = line.strip()
        listArray = line.split('\t')
        bk_class[listArray[0]] = listArray[1]
        bk_class_set.add(listArray[1])
        line = bk_class_fr.readline()
    bk_class_fr.close()
    
    bk_fr = open(book_file_name)
    line = bk_fr.readline()
    bk = {}
    line = bk_fr.readline()
    while line:
        line = line.strip()
        listArray = line.split('\t')
        key = listArray[0]+'_'+listArray[1]
        bk_num = listArray[2]
        if bk_class.has_key(bk_num):
            bk_kind = bk_class[bk_num]
            if(bk.has_key(key)):
                bk[key][bk_kind] += 1
            else:
                bk[key] = {}
                for kind in bk_class_set:
                    bk[key][kind] = 0	
                bk[key][bk_kind] += 1
        line = bk_fr.readline()
    bk_fr.close()

    for key in bk.keys():
        tot = 0
        for val in bk[key].values():
            tot += val
        bk[key]['bk_total'] = tot

    feature = ['TV', 'TT', 'TU', 'TS', 'TP', 'TQ', 'TN', 'TL', 'TM', 'TJ', 'TK', 'TH', 'TF', 'TG', 'TD', 'TE', 'TB', 'A', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'J', 'M', 'L', 'O', 'N','Q', 'P', 'S', 'R', 'U', 'T', 'V', 'Y', 'X', 'Z','bk_total']
    for f in feature:
        featurePlot(bk,f)

'''
    for key in bk.keys():
        print key,
        for kk in bk[key].keys():
            print "%s:%d" % (kk,bk[key][kk]),
        print
'''

def featurePlot(dictionary,feature):
   y = zeros(len(dictionary))
   i = 0
   for key in dictionary.keys():
       y[i] = dictionary[key][feature]
       i += 1
   
   x = range(len(dictionary))

   plt.plot(x,y)
   plt.xlabel("student")
   plt.ylabel(feature)
   plt.title(feature)
   plt.show()
    
