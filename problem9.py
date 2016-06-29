# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
#
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

def generate_squares():
    squares = []
    count = 1
    while True:
        hold = count ** 2
        if hold > (300000): break
        squares.append(hold)
        count += 1
    return squares

def find_triples(square_list):
    triples_list = []
    for i in range(len(square_list)):
        for n in range(len(square_list)):
            sums = square_list[i] + square_list[n]
            if sums in square_list:
                triples_list.append((square_list[i], square_list[n], sums))
                break
    return triples_list

def root_triples(triple_list):
    root_list = []
    for item in triple_list:
        a = math.sqrt(item[0])
        b = math.sqrt(item[1])
        c = math.sqrt(item[2])
        root_list.append((a, b, c))
    return root_list

def sum_tuple(root_list):
    sum_list = []
    for item in root_list:
        total = int(item[0] + item[1] + item[2])
        sum_list.append(total)
    return sum_list

square_list = generate_squares()
triples_list = find_triples(square_list)
root_list = root_triples(triples_list)
sum_list = sum_tuple(root_list)
try:
    index = sum_list.index(1000)
except:
    pass
correct_triple = root_list[index]
product = correct_triple[0] * correct_triple[1] * correct_triple[2]
print(product)
# print(square_list)
# print(triples_list)
# print(root_list)
# print(sum_list)
