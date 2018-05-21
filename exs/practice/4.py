
#Φτιάξτε μια συνάρτηση η οποία να δέχεται ως όρισμα ένα λεξικό. Τα κλειδιά του λεξικού είναι
#ο αριθμός ενός τηλεφώνου. Οι τιμές του λεξικού είναι ένα tuple που περιέχει το Όνομα και το
#Επώνυμο του κατόχου του τηλεφώνου. Π.χ. d={393875:('Βασίλης','Χριστόπουλος'), 458832:
#('Αλέξης','Ομορφούλης'), 393939:('Αλίκη','Ασχημούλα')}. Η συνάρτηση θα επιστρέφει μια
#λίστα, με tuples, με 3 στοιχεία, όπου κάθε tuple θα εχει τη μορφή (Όνομα, Επώνυμο, Αρ.
#Τηλ.). Οι λίστες θα είναι ταξινομημένες αλβαφητικά ως προς το Επώνυμο με τη μέθοδο
#selection sort.


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
        if l[i][1] <= minValue[1]:
            minValue = l[i]
            place = i
    return place


d = {
	393875: ('Βασίλης', 'Χριστόπουλος'),
	458832: ('Αλέξης', 'Ομορφούλης'),
	393939: ('Αλίκη', 'Ασχημούλα')
}

def f(d):
	l = []
	for i in d:
		t = (d[i][0], d[i][1], i)
		l.append(t)
	return selectionSorting(l)

print(f(d))
