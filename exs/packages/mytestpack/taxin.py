# -*- coding: utf-8 -*-
# AP EKSW !!!!!!!!!
#### TAXINOMHSH ME EPILOGH

def find_min(L,b):	# επιστρέφει τη θέση του ελάχιστου μιας λίστας L 
    smallest=b
    i=b+1
    while i!=len(L):
        if L[i]<L[smallest]:           #!!!!!!!!!!! EDW ALLAGH if myless(L[i],L[smallest])   Ή ΑΛΛΑΖΩ ΤΗΝ ΦΟΡΑ ΑΝ ΜΟΥ ΖΗΤΗΣΕΙ ΤΑΞΙΝΟΜΗΣΗ ΣΕ ΦΘΙΝΟΥΣΑ ΣΕΙΡΑ !!!!!!!!!!!!!!!!
            smallest=i	# εύρεση θέσης του ελάχιστου
        i=i+1
    return smallest

def selection_sort(L):
    i=0
    while i!=len(L):
        smallest = find_min(L,i)
        L[i], L[smallest] = L[smallest], L[i]	# αμοιβαία ανταλλαγή στοιχείων
        i=i+1

L = [10,23,5,45,9,66,77,12,8]
selection_sort(L)
print (L) # GIATI DEN EXEI EPISTREFOMENH TIMH H selection_sort(L)

#me return sthn selection_sort
#L = [10,23,5,45,9,66,77,12,8]
#print (selection_sort(L))

##########################################################################################

##### TAXINOMHSH ME EISAGWGH

def insertion_sort(L):
    i=0
    while i!=len(L):
        insert(L,i)
        i+=1

def insert(L,b):
    i=b     #L[:b-1] taxinomineni lista
    # to L[b] prepei na taxinonithei se lista 
    while i!=0 and L[i-1]>=L[b]:                    #!!!!!!!!!!! EDW ALLAGH     while i!=0 and myless(L[b],L[i-1]) Ή ΑΛΛΑΖΩ ΤΗΝ ΦΟΡΑ ΑΝ ΜΟΥ ΖΗΤΗΣΕΙ ΤΑΞΙΝΟΜΗΣΗ ΣΕ ΦΘΙΝΟΥΣΑ ΣΕΙΡΑ !!!!!!!!!!!!!!!!
        i=i-1  #psaxno pros ta piso pou tha bei
    value=L[b]
    del L[b]
    L.insert(i,value)

#test
L = [10,23,5,45,9,66,77,12,8]
insertion_sort(L)
print (L)

##########################################################################################

##  AAAAN EXEIS XRONO MATHE TH...SYNITHWS DE TH BAZEI
##########################################################################################
# TAXINOMHSH ME SYGXWNEYSH

def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:                #!!!!!!!!!!! EDW ALLAGH if myless(left[i],right[j])  Ή ΑΛΛΑΖΩ ΤΗΝ ΦΟΡΑ ΑΝ ΜΟΥ ΖΗΤΗΣΕΙ ΤΑΞΙΝΟΜΗΣΗ ΣΕ ΦΘΙΝΟΥΣΑ ΣΕΙΡΑ !!!!!!!!!!!!!!!!
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result

def merge_sort(L):
    if len(L)<2:
        return L[:]
    else:
        middle=len(L)//2
        left=merge_sort(L[:middle])
        right=merge_sort(L[middle:])
        return merge(left,right)
            

#### test 
L = [10,23,5,45,9,66,77,12,8]
print (merge_sort(L))



