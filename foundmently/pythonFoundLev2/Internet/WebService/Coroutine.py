import time

# 模拟携程

def A():
    while True:
        print("---a---")
        yield
        time.sleep(0.5)

def B(c):
    while True:
        print("---b---")
        c.__next__()
        time.sleep(0.5)

if __name__ == '__main__':
    a = A()
    B(a)