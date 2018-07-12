#散列表：变量buckets被初始化成为一个列表，其中包含numbuckets这个空列表
#如果想保存查找一个键值为dictkey的条目，首先要使用散列函数 % 将dictkey转换成一个整数
#并使用这个整数在buckets中索引，找到与dictkey相关的散列桶，在这个桶中搜索，是否存在值为dictkey的条目
class intDict(object):
    def __init__(self, numBuckets):
        self.numBuckets = numBuckets
        self.buckets = []
        for i in range(numBuckets):
            self.buckets.append([])
    def addEntry(self, key, dictVal):
        hashBucket = self.buckets[key%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:
                hashBucket[i] = (key, dictVal)
                return
        hashBucket.append((key, dictVal))
    def getValue(self, key):
        hashBucket = self.buckets[key%self.numBuckets]
        for e in hashBucket:
            if e[0] == key:
                return e[1]
        return None
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[: -1] + '}' 