# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?



#for grid of size n:

#create n lists of n length...

#a = [2,    3,  4,  5,  ...n]
#b = [3, b[0] + a[1], b[1] + a[2]....]
#c = [4, c[0] + b[1], c[1] + b[2].... ]
#etc.etc.
#answer is last entry of final list

def generate_lists(size):
    the_list = list(range(2, size + 2))
    for i in range(size-1):
        the_list[0] = i + 3
        for i in range(1, size):
            the_list[i] = the_list[i-1] + the_list[i]
    return(the_list[-1])

print(generate_lists(20))
