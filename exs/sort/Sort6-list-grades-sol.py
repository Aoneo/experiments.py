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


def f(d):
  L1=[]
  L2=[]
  #Δημιουργώ τις 2 λίστες με ονόματα και μέσους όρους βαθμών
  L1=list(d.keys())
  for classes in d.values():
      n=len(classes)
      average=0
      grades=list(classes.values())
      average=sum(grades)/n
      L2.append(average)
  selection_sort(L1,L2)
  return L1,L2

#Κανω ταξινόμηση με βάση τη λίστα L1
def selection_sort(L1,L2):
    """Reorder the values in L from smallest to largest."""
    i=0
    while i != len(L1):
        smallest = find_min(L1, i)
        L1[i], L1[smallest] = L1[smallest], L1[i]
        L2[i], L2[smallest] = L2[smallest], L2[i]
        i=i+1

def find_min(L, b):
    """Return the index of the smallest value in L[b:]."""
    smallest = b # The index of the smallest so far.
    i=b+1
    while i != len(L):
      if L[i]<L[smallest]:
    # We found a smaller item at L[i].
         smallest = i
      i=i+1
    return smallest

  	
# Κυρίως πρόγραμμα
d = eval(input("Give dict of names and grades: "))
L1,L2=f(d)
print(L1,L2)