print(globals())
## LEGB规则locals ->enclosing function ->globals ->builtins(内件模块的命名空间
num = 100
def tes():
    num = 200
    def tes2():
        #num = 300
        print(num)
    return tes2

ret = tes()
ret()

print(dir(__builtins__))

