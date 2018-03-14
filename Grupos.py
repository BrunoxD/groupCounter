#!/usr/bin/python3

def countGroups(nro, a, b):
	groupSix = nro
	groupFive = 0
	while (groupSix >= 0) and ((groupSix % a != 0) or (groupFive % b != 0)):
		groupSix -= 1
		groupFive += 1
		#print(groupSix, groupFive)
	if groupSix >= 0:
		return (groupSix/a), (groupFive/b)
	return "Is not possible"

for i in range(1,25):
	for j in range(1,25-i):
			aux = countGroups(51, i, j)
			if (aux != "Is not possible") and abs(i-j) == 1: 
				print(i, j, aux)