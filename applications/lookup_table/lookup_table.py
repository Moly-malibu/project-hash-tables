# Your code here
import random
import math

table_pow = {}
table_factorial = {}
table_division = {}
table_modification = {}

def init_tables():
    for x in range(2, 14):
        for y in range(3, 6):
            table_pow[(x,y)] = math.pow(x,y)
    for x in range(2,14):
        for y in range(3,6):
            table_factorial[table_pow[(x,y)]] = math.factorial(table_pow[(x,y)])
def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    v = table_pow[(x,y)]
    v = table_factorial[v]
    v //= (x + y)
    v %= 982451653

    return v

print('initializating lookup tables...')
init_tables()

    # cache = {}

    # Your code here
    # item = (x,y)
    # if item not in cache:
    #     cache[item] = slowfun_too_slow(x,y)
    #     return cache[item]

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
