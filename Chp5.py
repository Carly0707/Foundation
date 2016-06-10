# a = [66.25, 333, 333, 1, 1234.5]
# print a.count(333), a.count(66.25), a.count('x')
#
# a.insert(2, -1)
# a.append(333)
# print a
#
# print a.index(333)
#
# a.remove(333)
# print a
#
# a.reverse()
# print a
#
# a.sort()
# print a
#
# print a.pop()

# # Using Lists as Stacks
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print stack
#
# print stack.pop()
# print stack

# # Using Lists as Queues
# from collections import deque
# queue = deque(["brohood", "John", "Michael"])
# queue.append("ProfessorX")
# queue.append("Magneto")
# print queue.popleft()
# print queue

# # built-in functions with lists
# def f(x): return x % 3 == 0 or x % 5 == 0
# print filter(f, range(2, 25))
# # -------------------------------------------
# def cube(x): return x*x*x
# print map(cube, range(1, 11))
#
# def add(x, y): return x+y
# seq1 = range(8)
# seq2 = [1,1,1,1,1,1,1,5]
# print map(add, seq1, seq2)
# # -------------------------------------------
# def add(x,y): return x+y
# print reduce(add, range(1, 11))
#
# def sum(seq):
#     def add(x,y): return x+y
#     return reduce(add, seq, 2)
# print sum(range(1,11))
# print sum([])
# -------------------------------------------

# #List Comprehensions
# squares = []
# for x in range(10):
#     squares.append(x**2)
# print squares
# # -------------------------------------------
# squares = [x**2 for x in range(10)]
# print squares

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],]
print matrix

matrix_m = [[row[i] for row in matrix] for i in range(4)]
print matrix_m
# equals to the following statement
matrix_n = []
for i in range(4):
    matrix_n.append([row[i] for row in matrix])
print matrix_n
# equals to the following statement
matrix_o =[]
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    matrix_o.append(transposed_row)
print matrix_o


# # del
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print a
# del a[2:4]
# print a
# del a[:]
# print a
# del a
# # print a >>> DEL has deleted the whole variable

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana'] #this is a list
fruit = set(basket)  # this is a set
print fruit
print 'orange' in fruit
print 'crabgrass' in fruit
# --------------------------------------------
# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print a
print b
print a - b # letters in a but not in b
print a | b # letters in either a or b
print a & b # letters in both a and b
print a ^ b # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
print a

# Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel
print tel['jack']

del tel['sape']
tel['irv'] = 4127
print tel

print tel.keys()
print 'guido' in tel




