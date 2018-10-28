from pymongo import *

client = MongoClient("mongodb://localhost:27017")
db = client.test
stu = db.stu

# insert
# s1 = stu.insert({'name': "张hh"})

# update
# stu.update_one({"name": "张hh"}, {"$set": {"name": "张三丰"}})

# delete
# stu.delete_one({'name': 'gi2'})

# select
# sort的参数和直接在mongo.exe中调用有所不同
cursor = stu.find({'age': {'$lte': 20}}).sort('_id', DESCENDING).skip(10).limit(5)
for s in cursor:
    print(s['name'])

print((stu.find_one({'age': 20}))['name'])

