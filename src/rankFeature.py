def getFeature(infile):
    fr = open(infile)
    line = fr.readline()
    line = fr.readline()
    
    rk = {}
    while line:
        line = line.strip()
        listArray = line.split('\t')
        key = listArray[0] + '_'+listArray[1]
        rk[key] = {}
        rk[key]['rank'] = int(listArray[2])
        line = fr.readline()

    return rk
'''
    for key in rk.keys():
        print key,
        for val in rk[key].values():
            print val,
        print
'''
