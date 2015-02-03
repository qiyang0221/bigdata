def getDateLen():
    days = 141
    return days

def convertMonth(semester,month):
    mm = int(month)
    if semester == '1' or semester =='3':
        mm -=9
        if mm < 0:
            mm += 12
        mm %= 5
    if semester == '2':
        mm -= 3
        mm %= 5
    return mm

def convertDate(semster,date):
    start_month = 9
    start_day = 1
    if semster == '2':
        start_month = 2
        start_day = 24

    mm = int(date[:2])
    dd = int(date[2:])
    
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    '''
    if semster == '1' or semster == '3':
        if mm > 1 and mm < 9:
            return -1
        elif mm == 1 and dd > 22:
            return -1
        elif dd > days[mm]:
            return -1
    else:
        if mm < 2 or mm > 7:
            return -1
        elif mm == 2 and dd < 24:
            return -1
        elif mm == 7 and dd > 14:
            return -1
        elif dd > days[mm]:
            return -1
    '''
         
    if (semster == '1' or semster == '3') and mm == 1:
        mm += 12

    index = 0
    if mm == start_month:
        index += dd - start_day
    else:
        index += days[start_month] - start_day
        i = start_month + 1
        while i < mm:
            index += days[i]
            i += 1
        if i == mm:
            index += dd
    if index >= getDateLen():
        index = -1
    return index

def featureInit(features,newFeatures):
    for sem in features.keys():
        for stu in features[sem].keys():
            for date in range(getDateLen()):
                for ft in newFeatures:
                    features[sem][stu][date][ft] = 0
    return features
