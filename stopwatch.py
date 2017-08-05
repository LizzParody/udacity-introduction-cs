import time

def time_execution(code):
    start = time.clock()
    result = eval(code) #evaluates the code
    run_time = time.clock() - start
    return result, run_time

print(time_execution("2*2"))

def spin_loop(n):
    i = 0
    while i < n:
        i = i +1

print(time_execution('spin_loop(10000)'))
