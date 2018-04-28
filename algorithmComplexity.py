def fact(n):
	"""假设n是自然数，返回n阶乘"""
	answer = 1
	while n > 1:
		answer *=n
		n -=1
	return answer
print (fact(50))
"""此程序要执行的步数5n+2"""

def squareRootExhaustive(x, epsilon):
	"""假设x和epsilon都是正的浮点数，并且epsilon<1，返回一个y
		使y*y与x的差小于epsilon"""
	step = epsilon**2
	ans = 0.0
	while abs(ans**2 - x) >= epsilon and ans*ans <=x:#ans**2比x小，主要是考虑x<1的情况
		ans += step
	if ans*ans >x:
		raise ValueError
	return ans
print(squareRootExhaustive(24.0,0.1))
def squareRootBi(x,epsilon):
	low = 0.0
	high = max(1.0, x)
	ans = (high + low)/2.0
	while abs(ans**2 - x) >= epsilon:
		if ans**2 < x:
			low = ans 
		else:
			high = ans
		ans = (high + low)/2.0
	return ans
print(squareRootBi(24.0,0.1))
#当(100,0.0001)时，两者运算差别较大

def f(x):
	ans = 0
	for i in range(1000):
		ans +=i
	print('Number of additions so far', ans)
	for i in range(x):
		ans +=i
	print('Number of additions so far', ans)
	for i in range(x):
		for j in range(x):
			ans +=1
			ans +=1
	print('Number of additions so far', ans)
	return ans

#O(logn), O(log(i))
def intToStr(i):
	'''假设i是非负整数
		返回一个表示i的十进制字符串'''
	digits = '0123456789'
	if i == 0:
		return 0
	result = ''
	while i > 0:
		result = digits[i%10] + result
		i=i//10
	return result

#O(len(s))
def addDigits(s):
	val = 0
	for c in s:
		val += int(c)
	return val

#O(x)
def factorial(x):
	if x == 1:
		return 1
	else:
		return x*factorial(x - 1)

#O(nlog(n))

#O(len(L1))*O(len(L2))
def isSubset(L1, L2):
	for e1 in L1:
		matched = False
		for e2 in L2:
			if e1 == e2:
				matched = True
				break
		if not matched:
			return False
	return True

def intersect(L1, L2):
	tmp = []
	for e1 in L1:
		for e2 in L2:
			if e1 == e2:
				tmp.append(e1)
	result = []
	for e in tmp:
		if e not in result:
			result.append(e)
	return result

#指数复杂度
def getBinaryRep(n, numDigits):
	'''假设n和numDigits的非负整数，返回一个长度为numDigits的字符串，为n的二进制表示'''
	result = ''
	while n >0:
		result = str(n%2) + result
		n = n//2
	if len(result) > numDigits:
		raise ValueError('not enough digits')
	for i in range(numDigits - len(result)):
		result = '0' + result
	return result
def genPowerset(L):
	powerset = []
	for i in range(0,2**len(L)):
		binStr = getBinaryRep(i, len(L))
		subset = []
		for j in range(len(L)):
			if binStr[j] == '1':
				subset.append(L[j])
		powerset.append(subset)
	return powerset

#简单的查找

#有序表的线性查找
def search(L, e):
	for i in range(len(L)):
		if L[i] == e:
			return True
		if L[i] >e:
			return False
	return False
#二分查找
def search1(L, e):
	def bSearch(L, e, low, high):
		if high == low:
			return L[low] == e
		mid = (low + high)//2
		if L[mid] ==e:
			return True
		elif L[mid] > e:
			if low == mid:
				return False
			else:
				return bSearch(L, e, low, mid - 1)
		else:
			return bSearch(L, e, mid + 1, high)
	if len(L) == 0:
		return False
	else:
		return bSearch(L, e, 0, len(L) - 1)
	