def getFeature(infile):
    fr = open(infile)
    line = fr.readline()
    line = fr.readline()
    
    rk = {}
    mx_rk = 0
    while line:
        line = line.strip()
        listArray = line.split('\t')
        key = listArray[0] + '.'+listArray[1]
        rk[key] = {}
        rk[key]['rank'] = int(listArray[2])
        mx_rk = max(mx_rk,rk[key]['rank'])
        line = fr.readline()

    return rk,mx_rk
'''
    for key in rk.keys():
        print key,
        for val in rk[key].values():
            print val,
        print
'''
