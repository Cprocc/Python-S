import time
# from FrameWork.dynamic_web_server import HTTPServer
HTML_ROOT_DIR = "../../html"


class Application(object):
    """
    一个通用的响应框架
    """
    def __init__(self, a):
        self.urls = a

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")  # 不确定字典中是否有该值，则可以用get方法
        if path.startswith("/static"):
            file_name = path[7:]
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                start_response(status="404 not found", headers=[])
                return "not found"
            else:
                file_data = file.read()
                file.close()
                start_response(status="200 OK", headers=[])
                return file_data.decode("utf-8")
        else:
            for url, handler in self.urls:
                if path == url:
                    response_body = handler(env, start_response)
                    return response_body
            start_response(status="404 not found", headers=[])
            response_body = "function or file not found"
            return response_body


# 补充function信息，补充url到function的映射
def show_c_time(env, start_response):
    # 当前调用的模式
    env.get("Method")
    env.get("PATH_INFO")
    # env.get("QUERY_STRING")

    # 当前调用的状态和头，用来组成报文头
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)

    # 返回相应体，在页面中显示的内容
    return "You request the time--->"+str(time.ctime())


def say_hello(env, start_response):
    env.get("Method")
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)

    # 返回相应体，在页面中显示的内容
    return "<---hello--->"


# urls自定义
urls = [
    ("/", show_c_time),
    ("/c_time", show_c_time),
    ("/say_hello", say_hello)
]

app = Application(urls)

# if __name__ == '__main__':
#     http_server = HTTPServer(app)
#     http_server.bind(8000)
#     http_server.start()
