def log_time(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@log_time
def hello():
    print("hello")

hello()