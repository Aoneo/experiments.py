#Έχουμε μια ανακατεμένη τράπουλα όπως πριν και θέλουμε να μοιράσουμε σε 2 παίκτες 7 χαρτιά (τροποποιήστε την προηγούμενη συνάρτηση ώστε να επιστρέφει 2 λίστες με 7 χαρτιά). Επαναλαβεται Ν φορές ώστε να υπολογίστε την πιθανότητα να έχει ο ένας από τους 2 παίκτες μόνο 'Καρό' . [Numpy9-cards3.py]Numpy9-cards2.py
import random

def deal():
    color=['Κούπα','Μπαστούνι','Σπαθί','Καρό']
    val=['1','2','3','4','5','6','7','8','9','10','Βαλές','Ντάμα','Ρήγας']
    deck=[]
####### Δημιουργούμε την τράπουλα

import random

def deal():
    color=['Κούπα','Μπαστούνι','Σπαθί','Καρό']
    val=['1','2','3','4','5','6','7','8','9','10','Βαλές','Ντάμα','Ρήγας']
    deck=[]
    for c in color:
    	for v in val:
    		deck.append(v+'_'+c)
    random.shuffle(deck)
    A = random.sample(deck,7) 
    for x in A: # gia na mhn ta xrhsimopoiw sthn epomenh moirasia
    	deck.remove(x) 
    B = random.sample(deck,7)
    return A,B 

def probability(N, A, B, special):    
	M = 0
	for i in range(N):
		A, B = deal()
		count1A, count1B = 0, 0
		for x in A:
			if special in x:
				count1A += 1
		for y in B:
			if special in x:
				count1B += 1
		if count1A == len(A) or count1B == len(B):
			M+=1
	return ("H pithanothta einai=%s" %(M/N))


A, B = deal()
N = 100
special = 'Καρό'
print (probability(N, A, B, special))



