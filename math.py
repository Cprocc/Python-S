import math
print(math.e)
x = math.e**-5
result1 = 0
result2 = 0

for i in range(9):
    result1 += (-1)**i * 5**i / math.factorial(i)
    print(result1,"----------------")
    result2 += 5**i / math.factorial(i)
    print(result2)

print(result1-x,result2**(-1) - x)