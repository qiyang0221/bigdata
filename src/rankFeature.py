import utils

def getFeature(infile):
    fr = open(infile)
    line = fr.readline()
    line = fr.readline()
    
    rk = {}
    mx_rk = 0
    while line:
        line = line.strip()
        listArray = line.split('\t')
        sem = listArray[0]
        stu = listArray[1]
        rank = int(listArray[2])
        mx_rk = max(rank,mx_rk)
        
        if sem not in rk.keys():
            rk[sem] = {}
        if stu not in rk[sem].keys():
            rk[sem][stu] = {}
        rk[sem][stu]['rank'] = rank
        for i in range(utils.getDateLen()):
            rk[sem][stu][i] = {}
        line = fr.readline()

    return rk,mx_rk
'''
    for key in rk.keys():
        print key,
        for val in rk[key].values():
            print val,
        print
'''
