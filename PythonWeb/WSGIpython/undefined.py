def application(env, start_response):
    env.get("method")
    status = "404 not found"
    header = []
    start_response(status, header)
    return "This is an function which have not defined"
