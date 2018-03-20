
def selectionSorting(inputList):
    l = list(inputList)
    key = 0
    for x in l:
        valuePos = findMinPlace(l, key)
        l[key], l[valuePos] = l[valuePos], l[key] 
        key += 1
    return l


def findMinPlace(inputList, key):
    l = list(inputList)
    minValue = l[key]
    place = key
    for i in range(key, len(l)):
        if booleanSort(l[i], minValue):
            minValue = l[i]
            place = i
    return place

def findMaxPlace(inputList, key):
    l = list(inputList)
    minValue = l[key]
    place = key
    for i in range(key, len(l)):
        if l[i] > minValue:
            minValue = l[i]
            place = i
    return place

def booleanSort(tuppleOne, tuppleTwo):
    t1 = (tuppleOne[0]**2) + (tuppleOne[1]**2)
    t2 = (tuppleTwo[0]**2) + (tuppleTwo[1]**2)
    if t1 < t2:
        return True
    else:
        return False



print( selectionSorting([(1,4),(-7,4),(2,6),(7,-4),(2,0),(-5,3)]) )


