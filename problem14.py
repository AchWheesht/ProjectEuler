# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def produce_chain(number):
    count = 1
    while number > 1:
        if number % 2 == 0:
            number = int(number/2)
        else:
            number = (3* number) + 1
        count += 1
    return count

def find_longest_chain():
    count = 1
    longest_chain = 0
    longest_number = 0
    while count < 1000000:
        hold = produce_chain(count)
        if hold > longest_chain:
            longest_chain = hold
            longest_number = count
        print("Checked: ", count)
        count += 1
    return (longest_chain, longest_number)

print(find_longest_chain())
