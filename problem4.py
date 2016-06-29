# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
def determine_if_pailindrome(number):
    """Works only for six-digit numbers"""
    number_str = str(number)
    number_length = 6
    low_half = number_str[3:]
    high_half = number_str[:3]
    reversed_high_half = high_half[2] + high_half[1] + high_half[0]
    if low_half == reversed_high_half:
        return True
    else:
        return False

def factorise_for_three_digits(number):
    factors = []
    for i in range(100, 1000, 1):
        if number % i == 0: factors.append(i)
    three_digit_factors = []
    for factor in factors:
        cofactor = int(number / factor)
        if cofactor >= 100 and cofactor < 1000: three_digit_factors.append((factor, cofactor))
    return three_digit_factors

def find_highest_palindrome():
    for i in range((999*999), -1, -1):
        if determine_if_pailindrome(i):
            factors = factorise_for_three_digits(i)
            if factors:
                print("Solution found! %d is the highest palindrome" % i, factors)
                return

find_highest_palindrome()
