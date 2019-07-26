def solution(num):
	#print(num)
	def totalElements(x):
		no = 0
		while x>0:
			no += x
			x -= 1
		return no
	numOfElements = totalElements(num)
	#print(number)
	

N = input()
logicPyramid = solution(int(N))