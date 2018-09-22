# This program is to understand python lambda/map/filter/reduce keywords

# lambda #

# The lambda operator or lambda function is a way to create small anonymous
# functions, i.e. functions without a name. These functions are throw-away
# functions, i.e. they are just needed where they have been created.
# Lambda functions are mainly used in combination with the functions filter(),
# map() and reduce().

f_sq = lambda x: x*x
print f_sq(10)

f_add = lambda x, y: x+y
print f_add(10, 20)

# map() #
# syntax: r = map(func, seq)

seq1 = [1, 2, 3, 4]
print map(f_sq, seq1)

# map accepts multiple sequences
seq2 = [5, 6, 7, 8]
print map(f_add, seq1, seq2)


# filter() #
# syntax: r = filter(func, seq)
# filter is to filter out the values from the given sequence.
# every value from the sequence will be sent to function.
# If function returns true then only the values will be added to result list

seq3 = [1, 2, 3, 4, 5, 6]
# print odd numbers
print filter(lambda x: x % 2, seq3)
# print even numbers
print filter(lambda x: x % 2 == 0, seq3)


# reduce() #
# The function reduce(func, seq) continually applies the function func()
# to the sequence seq one by one(result of each iteration with the
# next value till the end of the value). It returns a single value.

seq4 = [71, 54, 12, 46, 86, 32]
print reduce(lambda x, y: x+y, seq4)
print reduce(lambda x, y: x+y, range(10))

f = lambda a, b: a if (a > b) else b
print reduce(f, seq4)


# lambda inside lambda
f_y = lambda y: y*y
f_x = lambda x: f_y(10)+x
print f_x(10)

# lambda inside lambda with map

print map(lambda x: x+1, map(lambda y: y*y, [2, 3, 4]))