N = int(input("Enter N: "))
oddList = []
primeList = []
primeListActual = []
primeListActual.append(2)
primeListActual.append(3)
i = 5
if N%2 == 0:
	while i<N:
		oddList.append(i)
		i += 2
else:
	while i<=N:
		oddList.append(i)
		i += 2
for oddNo in oddList:
	j = 3
	odd = 1
	while j<(oddNo/2):
		if oddNo%j == 0:
			odd = 0
			break
		j += 1
	if odd == 1:
		primeList.append(oddNo)
		primeListActual.append(oddNo)
print(primeListActual)
consecutivePrimeSum = []
for primeNo in primeList:
	k = 0
	sum = 0
	while sum < primeNo:
		sum += primeListActual[k]
		if sum == primeNo:
			consecutivePrimeSum.append(primeNo)
			break
		k += 1
print(consecutivePrimeSum)
print(len(consecutivePrimeSum))