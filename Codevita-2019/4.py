def sumOfList(List):
    Sum = 0
    for i in List:
        Sum += i
    return Sum

def separateAlternate(cars):
    cars1, cars2 = [], []
    for i in range(len(cars)):
        if i % 2 == 0:
            cars1.append(cars[i])
        else:
            cars2.append(cars[i])
    return cars1 + cars2

cars = list(map(int, input().split()))
cars.sort(reverse=True)
totalLiters = sumOfList(cars)
print(totalLiters)
minTimeRequired = totalLiters//2
newCars = separateAlternate(cars)
print(newCars)
currentTotal = 0
cars1, cars2 = [], []
for car in newCars:
    print("currentTotal: ", currentTotal, car)
    if currentTotal < minTimeRequired:
        print("if")
        currentTotal += car
        currentIndex = cars.index(car)
        cars1.append(car)
    else:
        print("else")
        cars2.append(car)
print(cars1, cars2, currentTotal)

# prevDiff = MAX_INT
# currentDiff = abs(sumOfList(cars1) - sumOfList(cars2))
# i = 1
# while prevDiff >= currentDiff:
#     temp = cars1[i]
#     cars1[i] = 