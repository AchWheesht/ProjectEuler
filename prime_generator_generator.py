import math

def generate_primes_generator(limit):
    prime_list = []
    count = 1
    list_length = 1
    previous_length = 0
    while True:
        while count <= limit:
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
        #print("Super advanced finished. Anaylsed %d numbers. %d are prime." % (count, list_length))
        limit = yield prime_list
