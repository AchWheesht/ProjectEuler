# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
import math
import prime_generator_module

def find_lowest_prime_factor(primes, number):
    for item in primes:
        if number % item == 0:
            return item

def alternate_find_lowest_prime_factor(primes, number):
    for item in primes:
        if number % item == 0:
            return item

def find_lowest_prime_cofactor(factor, number):
    return int(number / factor)

def check_if_prime(prime_list, number):
    if number in prime_list:
        return True
    else:
        return False

def alternate_check_if_prime(number):
    sqrt_number = math.sqrt(number)
    if sqrt_number.is_integer(): return False
    else: sqrt_number = int(sqrt_number + 1)
    to_check = list(range(sqrt_number))
    del to_check[0]
    del to_check[0]
#    print(to_check)
    for i in to_check:
        if number % i == 0:
            return False
    return True

def find_prime_factors(number, prime_list = None):
    if not prime_list:
        prime_list = prime_generator_module.generate_primes_super_advanced("number", math.sqrt(number))
    all_primes = False
    all_primes = True
    factor_list = []
    #if number in prime_list:
        #factor_list.append(number)
        #return factor_list
    if alternate_check_if_prime(number):
        factor_list.append(number)
    else:
        all_primes = False
        low_prime = find_lowest_prime_factor(prime_list, number)
        factor_list.append(low_prime)
        high_factor = find_lowest_prime_cofactor(low_prime, number)
        factored_high_number = find_prime_factors(high_factor, prime_list)
        factor_list += factored_high_number
    return factor_list
