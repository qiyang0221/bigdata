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

    mat = [[0 for col in range(len(bk_class_set)+1)] for row in range(len(bk))]
    row = 0
    for key in bk.keys():
        col = 0
        mat[row][col] = key
        col += 1
        for val in bk[key].values():
            mat[row][col] = val
            col += 1
        row+=1

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print mat[i][j],
        print
