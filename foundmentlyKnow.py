'''map function & for '''
def fib(n):
	if n == 0 or n==1:
		return 1
	else:
		return fib(n-1) + fib(n-2)
for i in map(fib, [2,6,4]):
	print (i)

L1 = [1,4]
L2 = [2,3]
for i in map(min, L1,L2):
	print (i)

'''lambda no-name function'''
L = []
for i in map (lambda x,y: x**y, [1,2,3,4], [3,2,1,0]):
	L.append(i)
print (L)

'''There rae many function in Py to do on Str
   such as  count(s1) find(s1) rfind(s1) index(s1) rindex(s1) 
   lower() replace(old,new) rstrip() split(d)'''


'''tuple as the key of dictiontry  dict：key-value
   dict 中的项目是无序的，monthNumbers[1]指的是1月的key-value
   key()是一个方法：返回一个dict_keys类型的对象
   所有python的内置不可变对象都是可散列的，所有python内置的可变对象都是不可散列的
   dict function:
   len(d):返回d中项目的数量
   d.keys():返回d中所有键的view
   d.values()
   k in d:
   d[k]:返回key为k的value
   d.get(k,v): 如果K在d中，则返回d[k],否则返回v
   del d[k]: 从d中删除key k
   for k in d： 遍历d中的key'''
monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print ('the third month is ' + monthNumbers[3])
dist = monthNumbers['Apr'] - monthNumbers['Jan']
print ('Apr and Jan are', dist, 'months apart')
keys = []
for e in monthNumbers:
	keys.append(str(e))
print (keys)
keys.sort()
print (keys)

months = monthNumbers.keys() 
list1 = list(months)
print (list1)       

'''Error finding'''
def isPal(x):
   temp = x
   temp.reverse
   if temp == x:
      return True
   else:
      return False
def silly(n):
   for i in range(n):
      result = []
      elem = input('Enter element: ')
      result.append(elem)
   if isPal(result):
      print('yes')
   else:
      print('no')
# 异常控制
'''Error try Except'''
numSuccess = 1
numFail = 0 
try:
   successFail = numSuccess/numFail
   print('this result is work')
except ZeroDivisionError:
   print('this result wont work ')
print('now here')

while True:
   val = input('Enter an integer: ')
   try:
      val = int(val)
      print('The square of the number you entered is ', val**2)
      break
   except ValueError:
      print(val ,'is not an integer')

'''define readInt function to slove the input of integer'''
def readInt():
   while True:
      val = input('Enter an integer1: ')
   try:
      return(int(val))
   except ValueError:
      print(val ,'is not an integer')

'''define readVal function to slove the input of any type'''
def readVal(valType,requestMsg,errorMsg):
   while True:
      val = input(requestMsg + ' ')
      try:
         return(valType(val))
      except ValueError:
         print(val ,errorMsg)
readVal(int ,'Enter an integer2:' ,'is not a integer')
val = readVal(int ,'Enter an integer3: ','is not an integer')

def getRatios(vect1, vect2):
   '''假设vect1和vect2是长度相同的数值型列表，返回一个包含vect[i]和vect2[i]中有意义的值的列表'''
   ratios = []
   for index in range(len(vect1)):
      try:
         ratios.append(vect1[index]/vect2[index])
      except ZeroDivisionError:
         ratios.append(float('nan')) #nan not a number
      except:
         raise ValueError('getRatios called with bad arguments') #raise expectionName(arguements)
   return ratios
try:
   print(getRatios([1.0,2.0,7.0,6.0],[1.0,2.0,0.0,3.0]))
   print(getRatios([],[]))
   print(getRatios([1.0,2.0],[3.0]))
except ValueError as msg:
   print(msg)

def getGrades(fname):
   try:
      gradesFile = open(fname , 'r') #open file for reading
   except IOError:
      raise ValueError('getGrades could not open ' + fname)
   grades = []
   for line in gradesFile:
      try:
         grades.append(float(line))
      except:
         raise ValueError('Unable to convert line to float')
   return grades
try:
   grades = getGrades('quiz1grades.txt')
   grades.sort()
   median = grades[len(grades)//2]
   print('Median grade is ', median)
except ValueError as errorMsg:
   print('Whoops.',errorMsg)

'''assert Boolean expression
   assert Boolean expression, argument'''

class IntSet(object):
   """docstring for IntSet"""
   def __init__(self):
      self.vals = []
   def insert(self,e):
      if e not in self.vals:
         self.vals.append(e)
   def member(self,e):
      return e in self.vals
   def remove(self,e):
      try:
         self.vals.remove(e)
      except:
         raise ValueError(str(e) + 'not found')
   def getMembers(self):
      return self.vals[:]
   def __str__(self):
      '''返回一个表示self的字符串'''
      self.vals.sort()
      result = ''
      for e in self.vals:
         result = result + str(e) + ','
      return '{' + result[:-1] + '}' #-1可以忽略最后的逗号
print(type(IntSet),type(IntSet.insert))
s = IntSet()
s.insert(3)
print(s.member(3))
s = IntSet()
s.insert(4)
s.insert(3)
print(s)