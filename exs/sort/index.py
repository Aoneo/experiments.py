
def avgN(n1, n2):
    return (n1 + n2) / 2

def avgL(lst):
    n = 0
    for i in lst:
        n += i
    return n / len(lst)

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
        if l[i] <= minValue:
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


#Φτιάξτε μια συνάρτηση η οποία να δέχεται ως όρισμα 
#ένα λεξικό. Τα κλειδιά του λεξικού είναι τα ονόματα 
#φοιτητών. Οι τιμές του λεξικού είναι ένα άλλο λεξικό που 
#περιέχει ως κλειδιά τα μαθήματα που έχει περάσει ο 
#φοιτητής και τιμές τους αντίστοιχους βαθμούς. 
#Π.χ. d={"Mike":{"MEM107":6, "MEM108":9}, 
#        "Peter":{"MEM105":6, "MEM107":9}}.
# Η συνάρτηση θα επιστρέφει δύο λίστες, στην πρώτη θα είναι 
# τα ονόματα φοιτητών και στη δεύτερη ο μέσος όρος των 
# βαθμών των μαθημάτων που έχει περάσει ο αντίστοιχος 
# φοιτητής της πρώτης λίστας. Οι λίστες θα είναι 
# ταξινομημένες αλφαβητικά με τη μέθοδο selection sort.


universityStudentGrades = {"Mike":{"MEM107":6, "MEM108":9}, "Peter":{"MEM105":5, "MEM107":8}}

def avgGrades(dictionary):
    names = []
    grades = []
    returnDict = {}

    for i in dictionary:
        names.append(i)
        grades.append( avgL( list( dictionary[i].values() ) ) )
    for x in range(len(names)):
        returnDict[names[x]] = grades[x]
    return selectionSorting( returnDict )








###### HOMEWORK 28/3 ######
#                         #
#  Make dictionarySort()  #
#                         #
###########################


# ready-made

d = { 'a': 1, 'f': 6, 'x':24, 'e':5 }

def readyMadeDictionarySort(d, query = 'k'):
    r = {}
    if query == 'k':
        for key in sorted(d.keys()):
            r[key] = d[key]
    else:
        for i in sorted(d.values()): ### KeyError: 1
            r[i] = d[i]
    return r


# custom algorithm

def order(x, y):    
    if x[1] < y[1]:
        return x, y
    else:
        return y, x

def dictionaryBubbleSort(d, query = 'v'):
    dictionaryItems = []
    if query == 'k':
        for j in d:
            v = (j, d[j])
            dictionaryItems.append(v)
    elif query == 'v':
        for j in d:
            v = (d[j], j)
            dictionaryItems.append(v)
    for x in range(len(dictionaryItems) - 1):
        for i in range(len(dictionaryItems) - 1):
            dictionaryItems[i], dictionaryItems[i+1] = order(dictionaryItems[i], dictionaryItems[i+1])
    return dictionaryItems

