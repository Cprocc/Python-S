from multiprocessing import Process
from socket import *
import re
# 常量的所有字母设置为大写，用以区分。
# HTML_ROOT_DIR 为静态文件根目录
HTML_ROOT_DIR = "./html"


def handle_client(client_socket):
    """
    处理客户端请求
    :param client_socket:
    :return:
    """
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request_data " + str(request_data))

    # 解析用户的请求头，判断是否需要对应的资源
    request_line = request_data.splitlines()
    for line in request_line:
        print(line)
    # 提取用户请求的文件名
    request_start_line = request_line[0]
    file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf=8")).group(1)

    # if "/" == file_name:
    if file_name == '/':
        file_name = "/index.html"

    try:
        file = open(HTML_ROOT_DIR + file_name, "rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 NOT Found\r\n"
        response_headers = "Server:My server\r\n"
        response_body = "This file is not found!"
    else:
        file_data = file.read()
        file.close()
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server:My server\r\n"
        response_body = file_data.decode("utf-8")

    # 构造对客户端的响应数据
    # response_start_line = "HTTP/1.1 200 OK\r\n"
    # response_headers = "Server:My server\r\n"
    # response_body = "hello pythonWeb"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data "+str(response))

    # 将数据返回给客户端
    client_socket.send(bytes(response, "utf-8"))
    client_socket.close()


def main():
    ser_socket = socket(AF_INET, SOCK_STREAM)
    ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    ser_port = ('', 7799)
    ser_socket.bind(ser_port)
    ser_socket.listen(100)

    while True:
        client_socket, client_socket_address = ser_socket.accept()
        print("[%s, %s]client connection" % client_socket_address)
        handle_process = Process(target=handle_client, args=(client_socket,))
        handle_process.start()
        client_socket.close()


if __name__ == '__main__':
    main()
