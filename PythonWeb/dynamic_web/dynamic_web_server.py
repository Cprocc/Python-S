from multiprocessing import Process
from socket import *
import re
import sys

# 常量的所有字母设置为大写，用以区分。
# HTML_ROOT_DIR 为静态文件根目录

HTML_ROOT_DIR = "../html"
WSGI_PYTHON_DIR = "../WSGIpython"


class HTTPServer(object):
    """
    创建服务器的服务器类
    """

    def __init__(self):
        self.ser_socket = socket(AF_INET, SOCK_STREAM)
        self.ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.response_headers = ""

    # 接收状态码，响应头，由application调用
    def start_response(self, status, headers):
        """
        status = "200 OK"
        headers = [
            ("Content-Type", "text/plain")
        ]
        由application调用，参数由application决定，最终用来组合报文
        :param status:
        :param headers:
        :return:
        """
        response_headers = "HTTP/1.1" + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header
        self.response_headers = response_headers

    def handle_client(self, client_socket):
        request_data = client_socket.recv(1024)
        print("request_data " + str(request_data))

        # 解析用户的请求头，判断是否需要对应的资源
        request_line = request_data.splitlines()
        for line in request_line:
            print(line)
        # 提取用户请求的文件名
        request_start_line = request_line[0]
        file_name = re.match(r"(\w+) +(/[^ ]*) ", request_start_line.decode("utf=8")).group(2)
        method = re.match(r"(\w)+ +(/[^ ]*) ", request_start_line.decode("utf=8")).group(1)

        # 判断请求的类型，.py可执行文件，.html可引导的界面
        if file_name.endswith(".py"):
            try:
                m = __import__(file_name[1:-3])
            except ModuleNotFoundError:
                self.response_headers = "HTTP/1.1 404 NOT Found\r\n"
                response_body = "This function is not found!"
            else:
                # env用来包含用户请求的各种方式
                env = {
                    "PATH_INFO": file_name,
                    "Method": method
                }
                # 接收来自对应的可执行文件的返回值，来组成相应报文的body部分
                response_body = m.application(env, self.start_response)
            response = self.response_headers + "\r\n" + response_body

        else:
            # if file_name == '/':
            if "/" == file_name:
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
            print("response data " + str(response))

            # 将数据返回给客户端
        client_socket.send(bytes(response, "utf-8"))
        client_socket.close()

    def start(self):
        self.ser_socket.listen(100)
        while True:
            client_socket, client_socket_address = self.ser_socket.accept()
            # print("[%s, %s]client connection" % client_socket_address)
            print("{}{}".format(client_socket_address[0], client_socket_address[1]))
            handle_process = Process(target=self.handle_client, args=(client_socket,))
            handle_process.start()
            client_socket.close()

    def bind(self, param):
        ser_port = ("", param)
        self.ser_socket.bind(ser_port)


def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    http_server.bind(8000)
    http_server.start()


if __name__ == '__main__':
    main()
