# -*- coding: utf-8 -*-
####ID e2-1-2-problem

#### Άσκηση: Γράψτε μια συνάρτηση σε python:
####
####    def process(D, value)
####
#### όπου D είναι ένα λεξικό όπου η τιμή του κάθε κλειδιού είναι ακέραιος και value είναι ένας ακέραιος.
#### Η συναρτησή σας θα πρεπει να επιστρέφει ένα λεξικό που είναι ίδιο με το D εκτός από τα κλειδιά των
#### οποίων η τιμή είναι τουλάχιστον value, στα οποία η νέα τιμή πρέπει να είναι αυξημένη κατά 1.
#### (Τα κλειδιά στο λεξικό D και στο λεξικό που επιστρέφετε πρέπει δηλ. να είναι τα ίδια.)
####
#### Για παράδειγμα αν D= {1:1, 2:3, 3:4, 4:1, 5:3} και value=3, τότε το αποτέλεσμα πρέπει να είναι το λεξικό
####    {1:1, 2:4, 3:5, 4:1, 5:4}.
####


dd = { 1: 2, 2: 2, -1: 1, 3: 1, 4: 10}
vv = 1


def process(d, v):
    d3 = {}
    for x in d:
        if d[x] >= v:
            d3[x] = d[x] + 1
        else:
            d3[x] = d[x]
    return d3

print(process(dd,vv))

def f2(d,v):
    for x in d:
        if d[x] >= v:
            d[x] +=1
    return d

print(f2(dd,vv))
            
    