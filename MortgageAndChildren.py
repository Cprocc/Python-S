def findPayment(loan, r, m):
	'''假设loan和r是浮点数，m是整数
		返回一个总额为loan，月利率为r，期限为m个月的抵押贷款的每个月还款额'''
	return loan*((r*(1+r)**m)/((1+r)**m - 1))

class Mortgage(object):
	'''用来建立不同种类抵押贷款的抽象类'''
	def __init__(self, loan, annRate, months):
		'''创建一个总额为loan，期限为months，年利率为annRate的新抵押贷款'''
		self.loan = loan#初始贷款额
		self.rate = annRate/12#每月利率
		self.months = months#贷款期限
		self.paid = [0.0]#已支付的每月还款列表
		self.outstanding = [loan]#每月的未支付贷款余额列表
		self.payment = findPayment(loan, self.rate, months)#每月需支付的金额
		self.legend = None #description of mortgage
	def makePayment(self):
		'''支付每月还款'''
		self.paid.append(self.payment)
		reduction = self.payment - self.outstanding[-1]*self.rate
		self.outstanding.append(self.outstanding[-1] - reduction)
	def getTotalPaid(self):
		'''返回至今为止的支付总额'''
		return  sum(self.paid)#Python内置函数sum 返回一个字符串序列的综总和 
	def __str__(self):
		return self.legend

class Fixed(Mortgage):
	"""docstring for Fixed"""
	def __init__(self, loan, r, months):
		Mortgage.__init__(self, loan, r, months)
		self.legend = 'Fixed, ' + str(round(r*100,2)) + '%'

class FixedWithPts(Mortgage):
	"""docstring for FixedWithPts"""
	def __init__(self, loan, r, months, pts):
		Mortgage.__init__(self, loan, r, months)
		self.pts = pts
		self.paid = [loan*(pts/100)]
		self.legend = 'Fixed, ' + str(round(r*100,2)) + '%, '\
						+str(pts) + ' points'

class TwoRate(Mortgage):
	"""docstring for TwoRate"""
	def __init__(self, loan, r, months, teaserRate, teaserMonths):
		Mortgage.__init__(self, loan, teaserRate, months)
		self.teaserMonths = teaserMonths
		self.teaserRate = teaserRate
		self.nextRate = r/12
		self.legend = str(teaserRate*100)\
						+ '%  for ' + str(self.teaserMonths)\
						+' months, Then ' + str(round(r*100, 2)) + '%'
	def makePayment(self):
		if len(self.paid) == self.teaserMonths + 1:
			self.rate = self.nextRate
			self.payment = findPayment(self.outstanding[-1], self.rate, self.months - self.teaserMonths)
		Mortgage.makePayment(self)

'''给定一个样本，比较上述三种贷款的优劣'''
def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
	totMonths = years*12
	fixed1 = Fixed(amt, fixedRate, totMonths)
	fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
	twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
	morts = [fixed1, fixed2, twoRate]
	for m in range(totMonths):
		for mort in morts:
			mort.makePayment()
	for m in morts:
		print(m)
		print(' Total payment =  $' + str(int(m.getTotalPaid())))

compareMortgages(amt = 200000, years = 30, fixedRate = 0.07, pts = 3.25, 
					ptsRate = 0.05, varRate1 = 0.045, varRate2 = 0.095, varMonths = 48 )