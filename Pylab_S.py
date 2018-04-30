import pylab

pylab.figure(1)
pylab.plot([1,2,3,4],[1,2,3,4])
pylab.figure(2)
pylab.plot([1,4,2,3],[5,6,7,8])
pylab.savefig('Figure-Addie')
pylab.figure(1) #指定当前操作的图是哪一副
pylab.plot([5,6,10,3]) #没有指定x坐标，默认x随机生成范围是len(y),所以在本例中是len([5,6,10,3]),0~3
pylab.savefig('Fig-Jane')

principal = 10000 #初始投资额
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(values,'ko') #圆点虚线  #pylab.polt(values):默认蓝色实线
# pylab.plot(values, linewidth = 30)
pylab.title('5% Growth, Compounded Annually')
# pylab.title('5% Growth, Compounded Annually', fontsize = 'xx-large')
pylab.xlabel('Years of Compounding')
# pylab.xlabel('Years of Compounding',fontsize = 'x-small')
pylab.ylabel('Value of Principal ($)')
pylab.show()

#绘图是的默认设置用pylab.rcParams访问
