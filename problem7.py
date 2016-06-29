# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


import prime_generator_module

prime_list = prime_generator_module.generate_primes_super_advanced("primes", 10001)
print(prime_list[-1])
