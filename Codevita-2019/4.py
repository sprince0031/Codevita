def minPartition(s, n, s1, s2):
  if n < 0:
    return abs(s1-s2)
  inc = minPartition(s, n - 1, s1 + s[n], s2)
  
  exc = minPartition(s, n - 1, s1, s2 + s[n])
  
  return min(inc, exc)
              
data = input().split()
dataFinal = [int(i) for i in data]
n = len(dataFinal)

print(minPartition(dataFinal, n - 1, 0, 0))