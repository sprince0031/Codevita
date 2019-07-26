testCases = int(input())
caseList = []
for case in range(0,testCases):
	caseList.append(str(input()))

from itertools import permutations

def fact(y):
	if y == 1:
		return 1
	else:
		return y*fact(y-1)
x = 0
while x < testCases:
	#print(x+1)
	caseLen = len(caseList[x])
	if caseLen == 1:
		print(caseList[x])
		exit()
	else:
		factVal = caseLen//2
		palinNum = fact(factVal)
		divide = caseLen//2
		tempPalin = caseList[x][:divide]
		totHalfCases = [''.join(letter) for letter in permutations(tempPalin)]
		totCases = []
		if caseLen % 2 == 0:
			for case in totHalfCases:
				totCases.append(case + case[::-1])
		else:
			for case in totHalfCases:
				totCases.append(case + caseList[x][divide] + case[::-1])
		for finalCase in totCases:
			print(finalCase, end='')
	x+=1