import time


def application(env, start_response):
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
