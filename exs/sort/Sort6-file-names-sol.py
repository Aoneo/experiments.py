#Φτιάξτε μια συνάρτηση η οποία να δέχεται ως όρισμα 
#το όνομα ένος αρχείου και διαβάζει τις γραμμές του αρχείου 
#που αποτελείται ονοματεπώνυμα, ένα σε κάθε γραμμή. 
#Η συνάρτηση θα πρέπει να δημιουργεί ένα νέο αρχείο το οποίο 
#θα περιέχει τα ονόματα ταξινομημένα με αλφαβητική σειρά ως 
#προς το επώνυμο. Κάθε ονοματεπώνυμο αποτελείται από το 
#όνομα (πρώτα) και μετά από το επώνυμο, τα οποία χωρίζουν με 
#ένα κενό.   Χρησιμοποιήστε την ταξινόμηση με 
#εισαγωγή (insertion sort).

def insertion_sort(L):
    i=0
    while i!=len(L):
        insert(L,i)
        i+=1
    return L

def insert(L,b):
    i=b     #L[:b-1] taxinomineni lista
    # to L[b] prepei na taxinonithei se lista 
    while i!=0 and myless(L[b],L[i-1]):
        i=i-1  #psaxno pros ta piso pou tha bei
    value=L[b]
    del L[b]
    L.insert(i,value)  
    
def myless(s,t):   # a,b: strings ths morfhs "Onoma Epitheto"
    S = s.split()  # S,T: LISTES ths morfhs ["Onoma", "Epitheto"]
    T = t.split()
    if S[1]<T[1]:
        return True    
    elif S[1]==T[1]:  ### Ean einai idia ta sygkrinei me vash to mikro onoma
        return S[0]<=T[0]
    else:
        return False 

def f(file_name):
# ορισμός της  συνάρτησης 
  f=open(file_name,'r')
  L=f.readlines() #λίστα απο strings
  f.close()
  Lsorted = insertion_sort(L)
  fnew=open("sorted_names.txt",'w')
  for x in Lsorted:
  	fnew.write(x)
  	fnew.write('\n')
  fnew.close
  
  	
# Κυρίως πρόγραμμα
file_name = input("Give name of file: ")
f(file_name)












