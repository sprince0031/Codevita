a = [77883, 48760, 68269, 31574, 57351, 20528, 45398, 54148, 37399, 31382]
N = 10
r = 3
l = 1

def factorial(n: int):
    fact = 1
    for i in range(2, n+1):
       fact *= i
    return fact

prod = 1
for i in range(l, r+1):
    fact = factorial(a[i])
    prod *= fact
mod = prod % 1000000007
print(mod**(r-l))