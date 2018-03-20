
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
        if letterSort(l[i], minValue, 1):
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


#Φτιάξτε μια συνάρτηση που να δέχεται ως όρισμα 
#μια λίστα με ακεραίους αριθμούς μη ταξινομημένη 
#και να επιστρέφει τη λίστα ταξινομημένη με πρώτα 
#τους άρτιους σε αύξουσα σειρά και στη συνέχεια τους 
#περιττούς αριθμούς σε αύξουσα σειρά. Χρησιμοποιήστε 
#την ταξινόμηση με επιλογή ή με εισαγωγή (selection sort 
#ή insertion sort). Η σχέση διάταξης θα ορίζεται από 
#τη συνάρτηση my_order() και π.χ. η my_order(1,2) 
#θα επιστρέφει False, η my_order(4,6) θα επιστρέφει True.


# x = 1/3/5/7/9   y = 0/2/4/6/8
# x,x | x,y | y,y | y,x
def numberTypeBoolean(x1, x2):
    if x1 % 2 != 0 and x2 % 2 != 0: # x,x
        if x1 < x2:
            return True
        else:
            return False
    elif x1 % 2 != 0 and x2 % 2 == 0: # x,y
        return False
    elif x1 % 2 == 0 and x2 % 2 == 0: # y,y
        if x1 < x2:
            return True
        else:
            return False
    elif x1 % 2 == 0 and x2 % 2 != 0: # y,x
        return True



  	
#Φτιάξτε μια συνάρτηση η οποία να δέχεται ως όρισμα 
#το όνομα ένος αρχείου και διαβάζει τις γραμμές του αρχείου 
#που αποτελείται ονοματεπώνυμα, ένα σε κάθε γραμμή. 
#Η συνάρτηση θα πρέπει να δημιουργεί ένα νέο αρχείο το οποίο 
#θα περιέχει τα ονόματα ταξινομημένα με αλφαβητική σειρά ως 
#προς το επώνυμο. Κάθε ονοματεπώνυμο αποτελείται από το 
#όνομα (πρώτα) και μετά από το επώνυμο, τα οποία χωρίζουν με 
#ένα κενό.   Χρησιμοποιήστε την ταξινόμηση με 
#εισαγωγή (insertion sort).


def nameSort(inputFile):
    f = open(inputFile, 'r')
    names = f.readlines()
    n = open('sortedNames.txt', 'w')

    sortedNames = selectionSorting(names)
    for i in sortedNames:
        n.write(i)
        n.write('\n')

    f.close()


def letterSort(fname, sname, cname):
    f = fname.split()
    s = sname.split()

    if f[cname] < s[cname]:
        return True
    else:
        return False


inputFile = input("Give name of file: ")

nameSort(inputFile)