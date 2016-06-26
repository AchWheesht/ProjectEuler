import time

def timer(func, *args):
    start = time.time()
    func_return = func(*args)
    end = time.time()
    timed = end - start
    return (timed, func_return)
