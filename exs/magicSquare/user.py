import random
import numpy as np
import math


def square(m):
	m2 = np.zeros((3, 3))

	for i in range(3):
		for j in range(3):
			m2[i, j] = (m[i, j] ** 2)

	return m2


def testSquare(m):
	# m = square(mx)
	rows = []
	cols = []
	srld = int(m[0, 0] + m[1, 1] + m[2, 2])
	slrd = int(m[0, 2] + m[1, 1] + m[2, 0])
	for i in range(3):
		k = int(sum(m[i, :]))
		rows.append(k)
		d = int(sum(m[:, i]))
		cols.append(d)
	A = np.array([rows, cols])
	if srld != slrd:
		return False
	else:
		for i in range(3):
			for j in range(3):
				if A[i,j] != srld:
					return False
		return True


n = 10000000
for i in range(n):
	m = np.zeros((3,3))
	for i in range(3):
		for j in range(3):
			m[i, j] = random.randint(1, 10)
	if testSquare(m):
		print(m)
print('none found')