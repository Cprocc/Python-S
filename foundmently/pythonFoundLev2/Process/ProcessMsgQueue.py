from multiprocessing import Queue
# 多进程之间传输数据

# 初始化一个Queue对象，最多可接收三条put消息
q = Queue(3)
q.put("msg_1")
q.put("msg_2")
print(q.full())
q.put("msg_3")
print(q.full())

# 因为消息队列已满，下面的try会抛出异常，第一个try会等待两秒异常， 第⼆个Try会立马抛出异常
try:
    q.put("msg_4",True,2)
except:
    print("msg_queue is full,the number is:%s"%q.qsize())

try:
    q.put_nowait("msg_4")
except:
    print("msg_queue is full,the number is:%s"%q.qsize())

# 先判断消息队列是否已满，再写入；读取消息时，先判断消息队列是否为空，再读取
if not q.full():
    q.put_nowait("msg_4")
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())