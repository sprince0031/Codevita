testCases = int(input())
caseList = []
for case in range(0,testCases):	
	caseList.append(str(input()))
def fact(y):
	if y == 1:
		return 1
	else:
		return y*fact(y-1)

def permutations(palinStr):
    if len(palinStr) == 1:
        return palinStr

    recursive_perms = []
    for letter in palinStr:
        for perm in permutations(palinStr.replace(letter,'',1)):
            recursive_perms.append(letter+perm)
    return set(recursive_perms)

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
		totHalfCases = permutations(tempPalin)
		totCases = []
		if caseLen % 2 == 0:
			for casex in totHalfCases:
				totCases.append(casex + casex[::-1])
		else:
			for casey in totHalfCases:
				totCases.append(casey + caseList[x][divide] + casey[::-1])
		for finalCase in totCases:
			print(finalCase, end='')
	x+=1