import datetime

class Person(object):
	"""docstring for person"""
	def __init__(self, name):
		self.name = name
		try:
			lastBlank = name.rindex(' ') #从右往左找到第一个空格
			self.lastName = name[lastBlank + 1:]
		except:
			self.lastName = name
		self.birthday = None
	def getName(self):
		return self.name
	def getLastName(self):
		return self.lastName
	def setBirthday(self, birthdate):
		self.birthday = birthdate
	def getAge(self):
		if self.birthday == None:
			raise ValueError
		print (datetime.date.today())
		print (self.birthday)
		return (datetime.date.today() - self.birthday).days
	def __lt__(self,other):
		if self.lastName == other.name:
			return self.name < other.name
		return self.lastName < other.lastName
	def __str__(self):
		return self.name

me = Person('Micheal Gutting')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print(him.getLastName())
him.setBirthday(datetime.date(1961,8,4))
her.setBirthday(datetime.date(1958,8,16))
print(him.getName(), 'is', him.getAge(), 'days old')
pList = [me, him, her]
for p in pList:
	print(p)
pList.sort()
for p in pList:
	print(p)


class MITPerson(Person):
	nextIdNum = 0  #identification number

	def __init__(self,name):
		Person.__init__(self,name)
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1
	def getIdNum(self):
		return self.idNum
	def __lt__(self,other):
		'''根据idNum比较大小'''
		return self.idNum < other.idNum
	def isStudent(self):
		return isinstance(self, Student)
#function isinsance is inset in python vect1 belong vect2：return True
#such as isinstance([1,2], list) return True
p0 = MITPerson('zhaoxincheng')
print(str(p0) + '\'s id number is' + str(p0.getIdNum()))
p1 = MITPerson('Barbara Beaver')
print(str(p1) + '\'s id number is' + str(p1.getIdNum()))

p2 = MITPerson('Mark Gutting')
p3 = MITPerson('Billy Bob Beaver')
p4 = MITPerson('Billy Bob Beaver')
p5 = Person('Billy Bob Beaver')

print('p2 < p3 =',p1 < p2) #p2,p3,p4的大小比较是根据学号idNum确定的
print('p4 < p3 =',p4 < p3)
print('p5 < p2 =',p5 < p2) #p5与其他person对象的大小比较是根据person里定义的方法
'''print('p2 < p5=', p2 < p5) 这是错误的，因为调用哪一级的方法由第一个参数决定，而这里p5没有idNum属性
AttributeError:'person'object has no attribute ' idNum'  '''

class Student(MITPerson):
	pass #保留关键字‘pass’只有继承自超类的属性
class UG(Student):
	"""docstring for UG"""
	def __init__(self, name, classYear):
		MITPerson.__init__(self, name)
		self.year = classYear
	def getClass(self):
		return self.year
class Grad(Student):
	"""docstring for Grad"""
	pass 
'''UG && Grad is the different class based on Student '''
p6 = Grad('Buzz Aldrin')
p7 = UG('billy Beaver', 1984)
print(p6, 'is a graduate student is', type(p6) == Grad)
print(p6, 'is an undergraduate student is', type(p6) == UG )
print(p6, 'is a student is' , p6.isStudent())
print(p7, 'is a student is' , p7.isStudent())
print(p2, 'is a student is' , p2.isStudent())

class TransferStudent(Student):
	"""docstring for TransferStudent"""
	def __init__(self, name, fromSchool):
		MITPerson.__init__(self, name)
		self.fromSchool = fromSchool
	def getOldSchool(self):
		return self.getOldSchool

class Grades(object):
	"""docstring for Grades"""
	def __init__(self):
		self.students = []
		self.grades = {}
		self.isSorted = True
	def addStudent(self, student):
		if student in self.students:
			raise ValueError('Dupicate student')
		self.students.append(student)
		self.grades[student.getIdNum()] = []
		self.isSorted = False
	def addGrade(self, student, grade):
		try:
			self.grades[student.getIdNum()].append(grade)
		except:
			raise ValueError('student not in mapping')
	def getGrades(self, student):
		try: #return copy of list of student's grades 
		    return self.grades[student.getIdNum()][:]
		except:
			raise ValueError('Student not in mapping')
	def getStudents(self):
		if not self.isSorted:
			self.students.sort()
			self.isSorted = True
		for s in self.students:
			yield s
#yield会被特殊处理，表明此函数是生成器，一般与for语句一起使用，
#如gradeReport函数中对getStudents的调用
#允许使用for循环调用Grades类型调用中的所有学生，就像访问普通List
		'''返回成绩册中排好序的成绩列表'''
		'''if not self.isSorted:
			self.students.sort()
			self.isSorted = True
		return self.students[:]''' #返回一个学生列表的副本 
def gradeReport(course):
	report = ''
	for s in course.getStudents():
	    tot = 0.0
	    numGrades = 0
	    for g in course.getGrades(s):
	        tot += g
	        numGrades += 1
	    try:
	    	average = tot/numGrades
	    	report = report + ' \n'\
	    	+ str(s) + '\'s mean grade is ' + str(average)
	    except ZeroDivisionError:
	    	report = report + '\n'\
        	+str(s) + 'has no grades'
	return report

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
sixHunndred = Grades()
sixHunndred.addStudent(ug1)
sixHunndred.addStudent(ug2)
sixHunndred.addStudent(g1)
sixHunndred.addStudent(g2)
for s in sixHunndred.getStudents():
	sixHunndred.addGrade(s, 75)
sixHunndred.addGrade(g1, 25)
sixHunndred.addGrade(g2, 100)
sixHunndred.addStudent(ug3)
print (gradeReport(sixHunndred))

Rafeal = MITPerson('Rafeal Reif')
'''Python3 的隐藏机制
	当一种属性的名称以__开头，但不以__结束时，这个属性就在类外不可见'''
class infoHiding(object):
	"""docstring for infoHiding"""
	def __init__(self):
		self.visible = 'Look at me'
		self.__alsoVisible__ = 'Look at me too'
		self.__inVisible = 'Don\'t look at me directly'
	def printVisible(self):
		print(self.visible)
	def printInvisible(self):
		print(self.__inVisible)
	def __printInvisible(self): #这个函数不可在类的外部调用
		print(self.__inVisible)
	def __printInvisible__(self):
		print(self.__inVisible)
test = infoHiding()
print(test.visible)
print(test.__alsoVisible__)
'''print(test.__inVisible) 不可直接输出'''

test.printInvisible()
test.__printInvisible__()	
'''test.__printInvisible() 不可直接调用'''

'''在派生类中也无法调用，下列代码不能工作
class subClass(infoHiding):
	"""docstring for subClass"""
	def __init__(self):
		print('from subClass', self.__inVisible)
testsub = subClass
'''
'''gradeReport中类的实现方式决定，我们在调用course.getStudent()会创建并返回一个大小为n的列表，
    n是学生的数量
	当n很大时，创建副本的效率十分的低
	解决办法，gradeReport直接访问course.student，这违背了信息隐藏的原则'''
book = Grades()
book.addStudent(Grad('Juline'))
book.addStudent(Grad('Charlie'))
for s in book.getStudents():
	print(s)
	