# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def find_sum_of_squares():
    total = 0
    for i in range(1, 101):
        total += i*i
    return total

def find_square_of_sum():
    total = 0
    for i in range(1, 101):
        total += i
    total *= total
    return total

def find_difference():
    sum_of_squares = find_sum_of_squares()
    square_of_sum = find_square_of_sum()
    print(sum_of_squares)
    print(square_of_sum)
    print(square_of_sum - sum_of_squares)

find_difference()
