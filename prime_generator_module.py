import math

def generate_primes_super_advanced(mode, limit):
    prime_list = [2]
    count = 2
    list_length = 1
    previous_length = 0
    if mode == "number":
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
    elif mode == "primes":
        while list_length < limit:
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
    else: raise ValueError('Please use "number" or "primes"')
    #print("Super advanced finished. Anaylsed %d numbers. %d are prime." % (count, list_length))
    return prime_list
