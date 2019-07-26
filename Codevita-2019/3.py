# data = input()
# allData = data.splitlines()
from itertools import chain
import sys
allData = sys.stdin.readlines()
# print(allData)
N, rate, target = int(allData[0]), allData[1][:-1], int(allData[2])
# print(N, rate, target)
intListString = rate.split()
# print(intListString)
rates = [int(i) for i in intListString]
# print(rates)
R1, R2 = rates[0], rates[1]
# to find number of rooms per day in a year
M = list(range(1, 13))
D = [list(range(1,32)), list(range(1,29)), list(range(1,32)), list(range(1,31)), list(range(1,32)), list(range(1,31)), list(range(1,32)), list(range(1,32)), list(range(1,31)), list(range(1,32)), list(range(1,31)), list(range(1,32))]
print(M, D)
# numberOfCustomersPerDay = [(6-i)**2 + abs(j-15) for i,j in M, D]
numberOfCustomersPerMonthList = []
count = 0
while count < 12:
    numberOfCustomersPerDayList = []
    for i in range(1, len(D[count])+1):
        numberOfCustomersPerDay = (6-M[count])**2 + abs(i-15)
        if numberOfCustomersPerDay <= N:
            numberOfCustomersPerDayList.append(numberOfCustomersPerDay)
        else:
            numberOfCustomersPerDayList.append(N)
    numberOfCustomersPerMonthList.append(numberOfCustomersPerDayList)
    count += 1
print(numberOfCustomersPerMonthList)
# Flattening list
flattenedList = list(chain.from_iterable(numberOfCustomersPerMonthList))
print(flattenedList)
if N*R2 >= target:
    print(0)
else:
    combinationList = [[i, N-i] for i in range(1, N)]
    print(combinationList)
    revenuePossibilitiesPerHead = [(R1*i[0]+R2*i[1]) for i in combinationList]
    print(revenuePossibilitiesPerHead)
    finalRevenues = []
    for revenuePerHead in revenuePossibilitiesPerHead:
        sum = 0
        for customerPerDay in flattenedList:
            sum += revenuePerHead*customerPerDay
        finalRevenues.append(sum)
    print(finalRevenues)