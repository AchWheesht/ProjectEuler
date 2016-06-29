# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Working out a method to do this took far too long. But I managed it! Sort of.
#Basically, we can find the lowest common factor for any two numbers with the following method:

#1. Find the ratio of the two numbers as a fraction (i.e. 6 and 9 is 2:3)
#2. Multiply the smaller number by the larger ratio number, or vice versa (i.e. 6 by three, or 9 by 2)

#Unfortunately, I couldnt find a way to properly implement this in code. The best I could come up with is this:

#1. Get a list of the prime factors for numbers a and b
#2. Eliminate any duplicates between the lists.
#3. For number a, multiply it by the product of all remaining numbers in list b.

#That gets the lowest common denominator for those two numbers. Hooray!
#For a list with multiple numbers, we can just domino up the list two numbers at a time.
#Unfortunetly, since im generating my prime numbers on the fly, the program cannot finish with the list of
#numbers from 1 to 20. Fortunately, for me, the LCD of the numbers 1 to 19 is 232792560. Any number ending in
#60 is obviously divisible by 20. Ergo, the LCD for all numbers up to 20 is the same as the LCD for all numbers
#up to 19.
#(Note: optimised the program so it can now comfortably do the the list up to 20. It can currently comfortably handle
#sequential numbers up to 30)

#There are better ways to do this, but I managed to work this out without consulting *any* outside resources.

import prime_factor_module
import prime_generator_module
import prime_generator_generator
import timer_module
import math

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def prune_list(numbers):
    new_numbers = []
    for item in numbers:
        if item == 1:
            numbers.remove(item)
    for item in numbers:
        flag = True
        for i in range(len(numbers)):
            if item == numbers[i]: continue
            if numbers[i] % item == 0: flag = False
        if flag:
            new_numbers.append(item)
    return new_numbers

def find_lcd_of_two_numbers(a, b):
    if a == b:
        return 1
    elif a % b == 0:
        return a
    elif b % a == 0:
        return b
    else:
        sum_a = a
        sum_b = b
        while True:
            if sum_a == sum_b:
                return sum_a
            if sum_a > sum_b:
                sum_b += b
            if sum_b > sum_a:
                sum_a += a

def find_lcd_of_list(number_list):
    number_list = number_list
    while len(number_list) > 1:
        lcd = find_lcd_of_two_numbers(number_list[0], number_list[1])
        number_list[0] = lcd
        del number_list[1]
    return number_list[0]


def find_lcd(numbers_list, prime_list = None):
    numbers = prune_list(numbers_list)
    print("Pruned List: ", numbers)
    prime_list = []
    largest_number = 0
    while len(numbers) > 1:
        largest_number = max([numbers[0], numbers[1], largest_number])
        prime_list = prime_generator.send(math.sqrt(largest_number))
        print("finding lcd of  %d and %d" % (numbers[0], numbers[1]))
        a = prime_factor_module.find_prime_factors(numbers[0], prime_list)
        b = prime_factor_module.find_prime_factors(numbers[1], prime_list)
        finished = False
        while finished == False:
            finished = True
            for item in b:
                if item in a:
                    finished = False
                    a.remove(item)
                    b.remove(item)
        if b:
            b = condense(b)
            numbers[0] *= b
            del numbers[1]
        else:
            if numbers[1] < numbers[0]:
                del numbers[1]
            else: del numbers[0]
    return numbers[0]

def condense(values):
    print("Condensing: ", values)
    while len(values) > 1:
        values[0] *= values[1]
        del values[1]
    print("Condensed into:", values)
    return values[0]

# product = 1
# for i in range(len(alist)):
#     product *= alist[i]
#
# print("Finding primes for: ", product)
# prime_list = prime_generator_module.generate_primes_super_advanced("number", product)

def print_result(*args):
    args = args[0]
    func = args[0]
    alist = args[1]
    print("result: ", func(alist))

prime_generator = prime_generator_generator.generate_primes_generator(0)
prime_generator.send(None)

while True:
    choice = input("Which solution? (primes, addition, both, exit)")
    if choice == "exit":
        break
    elif choice == "primes" or choice == "both":
        print("time for primes: ", timer_module.timer(print_result, [find_lcd, alist]))
        #print(find_lcd(alist))
    elif choice == "addition" or choice == "both":
        print("time for simple: ", timer_module.timer(print_result, [find_lcd_of_list, alist]))
        #print(find_lcd_of_list(alist))
    else:
        print("invalid input")


# while len(alist) > 1:
#     alist[0] *= alist[1]
#     del alist[1]
#     for i in range(len(alist)):
#         if i == 0: continue
#         print("%d / %d: %.5f" % (alist[0], alist[i], alist[0]/alist[i]))

#we can ignore 2 and 4, because all instances of two and four will be covered by 8
