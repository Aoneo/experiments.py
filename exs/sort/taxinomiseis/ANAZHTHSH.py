# -*- coding: utf-8 -*-
## AP' EKSW!!!!


import math 
#### GRAMMIMH ANAZHTHSH
def linear_search(v,L):
    i=0
    while i!=len(L) and L[i]!=v:
        i=i+1
    return i    

## TEST
K = [48, 39, 56, 69, 40, 7, 25]
y = 7
print (linear_search(y,K)) # επιστροφή της συνάρτησης linear_search

##########################################################################################

##### Dyadikh anazhthsh 
## prosoxh mono gia TAXINOMHMENES LISTES !!!!!!!!
def binary_search(v,L):
    i=0
    j=len(L)-1
    k = 0 
    while i!=j+1:
        m=(i+j)//2
        if L[m]<v:           # !!!!! GIA THN binary_search_descending(v,L) (me thn L:tzxinomhmenh se fthinousa seira) ALLAZEI MONO AYTOif L[m]>v ...MONO !!!!!!
            i=m+1
        else:
            j=m-1
        k +=1
        print "k=", k
    if 0<=i<len(L) and L[i]==v:
        return i
    else:
        return -1 

## TEST
L=[1,5,12,25,29,34,42,59,65]
print (binary_search(25,L)) # Ean typwsei -1 ;h den yparxei h timh ;h einai MH TAKSINOMHMENH H LISTA

##########################################################################################
