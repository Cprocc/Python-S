import algorithmComplexity
#Item 类
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' +str(self.value)\
        + ', ' + str(self.weight) + '>'
        return result
def value(item):
    return item.getValue()
def WeightInverse(item):
    return 1.0/ item.getWeight()
def density(item):
    return item.getValue() / item.getWeight()

def greedy(item, maxWeight, keyFunction):
    """假设Item是列表，maxWeight >= 0
        keyFunction将物品元素映射成数值"""
    itemsCopy = sorted(item, key = keyFunction, reverse= True) 
    #keyFunction定义了items中的排序规则
    #stored生成一个新列表，而不是修需要原始表（这个表要作为函数的参数）
    result = []
    totalValue,totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalValue += itemsCopy[i].getValue()
            totalWeight += itemsCopy[i].getWeight()
    return(result, totalValue)

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i],values[i],weights[i]))
    return Items

def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print('Total value of items taken is ', val)
    for item in taken:
        print(' ', item)

def testGreedys(maxWeight = 20):
    items = buildItems()
    print('Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, value)
    print('\nUse greedy by weight to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, WeightInverse)
    print('\nUse greedy by density to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, density)

testGreedys()


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


def chooseBest(pset, maxWeight, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)

def testBest(maxWeight = 20):
    items =  buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print ('total value of items taken is ', val)
    for item in taken:
        print(item)

testBest()

