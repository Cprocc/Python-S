import hashlib
###加密算法
m = hashlib.sha256() # 创建hash对象，
print(m)
m.update(b"NewVal")
print(m.hexdigest())