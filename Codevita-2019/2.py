
# data = input()
# allData = data.splitlines()
import sys
allData = sys.stdin.readlines()
print(allData)
T, allCases = int(allData[0]), allData[1:]
# withoutNewLines = [j[:len(j)-1] for j in allCases]
print(T, allCases)
intListString = [i[:len(i)-1].split() for i in allCases]
print(intListString)
intList = [list(map(int, i)) for i in intListString]
print(intList)

j = 0
while j < len(intList):


    j += 1