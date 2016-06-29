# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
import math

def generate_primes_super_advanced(numbers_to_analyse):
    prime_list = [2]
    count = 2
    list_length = 1
    previous_length = 0
    while count < numbers_to_analyse:
        if count % 50000 == 0: print("Analysed %d numbers" % count)
        count += 1
        is_prime = True
        for prime in prime_list:
            sqrt_number = int(math.sqrt(count))
            if prime > sqrt_number: break
            if count % prime == 0:
                is_prime = False
                break
        if is_prime == True:
            list_length += 1
            prime_list.append(count)
    print("Super advanced finished. Anaylsed %d numbers. %d are prime." % (count, list_length))
    return prime_list

def find_low_prime_factors(primes, number):
    factors = []
    for item in primes:
        if number % item == 0:
            factors.append(item)
    return factors

def find_low_prime_cofactors(low_primes, number):
    cofactors = []
    for item in low_primes:
        cofactors.append(int(number / item))
    return cofactors

def check_if_prime(prime_list, number):
    if number in prime_list:
        return True
    else:
        return False

# def reduce_down(prime_list, high_factors):
#     print("Currently Factorising List:", high_factors)
#     all_primes = False
#     while not all_primes:
#         all_primes = True
#         reduced_list = []
#         for item in high_factors:
#             if item in prime_list:
#                 reduced_list.append(item)
#             else:
#                 print("Preparing to Factor: ", item)
#                 all_primes = False
#                 low_primes = find_low_prime_factors(prime_list, item)
#                 high_factors = find_low_prime_cofactors(low_primes, item)
#                 final_list = reduce_down(prime_list, high_factors)
#                 reduced_list += final_list
#                 print("Factorise Successful! Got:", final_list)
#     print("Factorise List Successful! Got:", reduced_list)
#     return reduced_list

def reduce_down(prime_list, number):
    print("Currently Factorising List:", high_factors)
    all_primes = False
    while not all_primes:
        all_primes = True
        reduced_list = []
        for item in high_factors:
            if item in prime_list:
                reduced_list.append(item)
            else:
                print("Preparing to Factor: ", item)
                all_primes = False
                low_primes = find_low_prime_factors(prime_list, item)
                high_factors = find_low_prime_cofactors(low_primes, item)
                final_list = reduce_down(prime_list, high_factors)
                reduced_list += final_list
                print("Factorise Successful! Got:", final_list)
    print("Factorise List Successful! Got:", reduced_list)
    return reduced_list

number = int(input("?"))

prime_list = generate_primes_super_advanced(math.sqrt(number))
low_factors = find_low_prime_factors(prime_list, number)
print(low_factors)
high_factors = find_low_prime_cofactors(low_factors, number)
print(high_factors)

hold_primes = []
hold_nonprimes = []
for item in high_factors:
    if check_if_prime(prime_list, item):
        hold_primes.append(item)
    else:
        hold_nonprimes.append(item)

print(hold_primes)
print(hold_nonprimes)

final_list = reduce_down(prime_list, high_factors)
print(final_list)

all_prime_factors = low_factors + final_list
all_prime_factors.sort()
print(all_prime_factors)
