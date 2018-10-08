import time
import threading
def SayHello():
    time.sleep(5)
    print("hello")
    # time.sleep(5)

#即便主线程结束了，主线程也不会退出
if __name__ == "__main__":
    for _ in range (5):
        t = threading.Thread(target=SayHello)
        length = len(threading.enumerate())
        print(length)
        t.start()
    print("---main Thread finished---")
