# -*- coding: utf-8 -*-
key = 65

def encrypt(letter, key):
    "Κρυπτογραφεί ένα γράμμα letter με κλειδί key, έναν αριθμό από 0 έως 127"
    return chr( (ord(letter)+key) % 128 )

def encstring(s, key):
    "Κρυπτογραφεί ένα string s με κλειδί key, έναν αριθμό από 0 έως 127"
    t=""
    for x in s:
        t += encrypt(x, key)
    return t

def decrypt(encletter, key):
    "Αποκρυπτογραφεί ένα γράμμα letter με κλειδί key, έναν αριθμό από 0 έως 127"
    return chr( (ord(encletter)-key) % 128 )

def decstring(s, key):
    "Αποκρυπτογραφεί ένα string s με κλειδί key, έναν αριθμό από 0 έως 127"
    t=""
    for x in s:
        t += decrypt(x, key)
    return t

# Διαβάζουμε το αρχείο myinitialCode.txt
f = open("code.txt", "r")
lines = f.readlines()
f.close()

# Κρυπτογραφούμε τις γραμμές που διαβάσαμε και τις γράφουμε στο αρχείο enCode.txt
f = open("encode.txt", "w")
for l in lines:
    f.write(encstring(l, key))
f.close()

# Ανοίγουμε ξανά το αρχείο encalice.txt και διαβάζουμε τις γραμμές του
f = open("encode.txt", "r")
lines = f.readlines()
f.close()

# Αποκρυπτογραφούμε τις γραμμές που διαβάσαμε και τις γράφουμε στο αρχείο newalice.txt
f = open("newcode.txt", "w")
for l in lines:
    f.write( decstring(l, key))
f.close()