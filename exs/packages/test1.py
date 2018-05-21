import os 

import sys
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py

sys.path.append('./exs/packages/')

print (sys.path)

import mytestpack.ergcl




os.system('python3 ~/Dropbox/Private_Lessons/2017-ProgII-ear/sos_python2/numpy/numpy-iou17-A.py')

a = mytestpack.ergcl.fraction(1,3)

print (a.getar())
print (a.getpar())
print (a.value())

b = mytestpack.ergcl.fraction(2,6)

print (a+b)

print (a-b)

print (a*b)

print (a/b)


a1 = mytestpack.ergcl.BankAccount('John Papadopoulos', '19371554951', 20000)
a2 = mytestpack.ergcl.BankAccount('Mike Antreou', '19371563268', 40000)
print (a1.katathesi(200))
print (a1.analipsi(3000))
print (a1.ypoloipo())



A=mytestpack.ergcl.Rectangle(0,0,10,65)
print(A.area())
print(A.contains(15,20))
