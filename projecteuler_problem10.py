# Summation of primes
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.


import time
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

def time_function(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    #print(alist[:100])
    return (end - start)

def sum_primes():
    print("Sum of all primes under 2 million: %d" % sum(generate_primes_super_advanced(2000000)))

print("It took %.4f seconds" % time_function(sum_primes))

#prime_list_super_advanced_time = time_function(generate_primes_super_advanced, number_of_primes)
#print("Super advanced prime generator took %.2f seconds" % prime_list_super_advanced_time)



#Super Advanced Prime Generator Theory

#1. All non-prime numbers can factor into primes.
#2. All non-prime factors for non-prime numbers can factor into primes
#3. Therefore, we only need to check prime factors

#4. A number cannot be factored by a number greater than its half
#5. There is only one possible factor greater than its third (2)
#6. There is only one *prime* factor greater than its quarter (2)
#7. A second possible prime factor occurs only at it's fifth (5)
#8. And a third occurs at its seventh (7)

#9. We can take this into account when finding non-prime numbers by always finding the smaller prime factor first.
#10. But we clearly do not need to check all possible factors if the number is prime
#11. As we can rule out all numbers above half if it does not divide by two etc.
#12. The largest possible smallest factor is the square root of the number in question
#13. So we do not need to check any number above the square root of the number in question, rounded down.
