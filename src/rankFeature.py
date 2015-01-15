def getFeature(infile):
    fr = open(infile)
    line = fr.readline()
    line = fr.readline()
    
    bk = {}
    while line:
        line = line.strip()
        listArray = line.split('\t')
        key = listArray[0] + '_'+listArray[1]
        features = {}
        features['rank'] = listArray[2]
        bk[key] = features
        line = fr.readline()

    for key in bk.keys():
        print key,
        for val in bk[key].values():
            print val,
        print

     
