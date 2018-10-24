from multiprocessing import Process
from socket import *
import re
# 常量的所有字母设置为大写，用以区分。
# HTML_ROOT_DIR 为静态文件根目录
HTML_ROOT_DIR = "./html"

def handleClient(clientSocket):
    """
    处理客户端请求
    :param args:
    :return:
    """
    # 获取客户端请求数据
    requestData = clientSocket.recv(1024)
    print("requestData " + str(requestData))

    # 解析用户的请求头，判断是否需要对应的资源
    requestLine = requestData.splitlines()
    for line in requestLine:
        print(line)
    # 提取用户请求的文件名
    requestStartLine = requestLine[0]
    fileName = re.match(r"\w+ +(/[^ ]*) ",requestStartLine.decode("utf=8")).group(1)

    # if "/" == fileName:
    if fileName == '/':
        fileName = "/index.html"

    try:
        file = open(HTML_ROOT_DIR + fileName,"rb")
    except IOError:
        responseStartLine = "HTTP/1.1 404 NOT Found\r\n"
        responseHeaders = "Server:My server\r\n"
        responseBody = "This file is not found!"
    else:
        fileData = file.read()
        file.close()
        responseStartLine = "HTTP/1.1 200 OK\r\n"
        responseHeaders = "Server:My server\r\n"
        responseBody = fileData.decode("utf-8")


    # # 构造对客户端的响应数据
    # responseStartLine = "HTTP/1.1 200 OK\r\n"
    # responseHeaders = "Server:My server\r\n"
    # responseBody = "hello pythonWeb"
    response = responseStartLine + responseHeaders + "\r\n" + responseBody
    print("response data "+str(response))

    # 将数据返回给客户端
    clientSocket.send(bytes(response,"utf-8"))
    clientSocket.close()

def mian():
    serSocket = socket(AF_INET,SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    serPort = ('',7799)
    serSocket.bind(serPort)
    serSocket.listen(100)

    while True:
        clientSocket, cliSocketAddress = serSocket.accept()
        print("[%s, %s]client connection"% cliSocketAddress)
        handleProcess = Process(target=handleClient, args=(clientSocket,))
        handleProcess.start()
        clientSocket.close()

documentRoot = './html'

if __name__ == '__main__':
    mian()





