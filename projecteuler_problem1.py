# Multiples of 3 and 5
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

import time

def simple_version():
    numbers = []
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0: numbers.append(i)
    return numbers

def complicated_version():
    numbers = []
    count = 0
    three_var = 0
    five_var = 0
    for i in range(1000):
        count += 1
        three_var += 1
        five_var += 1
        if three_var == 3 or five_var == 5:
            numbers.append(count)
        if three_var == 3:
            three_var = 0
        if five_var == 5:
            five_var == 0
    return numbers

def time_function(func, *args):
    start = time.time()
    func_return = func(*args)
    end = time.time()
    timed = end - start
    return (timed, func_return)

time_simple = time_function(simple_version)
time_complicated = time_function(complicated_version)

print("Simple took %.10f seconds and returned %d" % (time_simple[0], sum(time_simple[1])))
print("Complicated took %.10f seconds and returned %d" % (time_complicated[0], sum(time_complicated[1])))
