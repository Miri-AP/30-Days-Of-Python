# Introduction
# Day 1 - 30DaysOfPython Challenge
import sys
print(sys.version)

print("Hello World!")   # print hello world
print(['Mir', 'Python', 'Mexico'])   # List
print({'name': 'Mir', 'country': 'Mexico', 'city': 'Mexico City'})   # Dictionary
print("I am enjoying 30 days of python")


print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 4j))              # Complex
print(type('Mir'))          # String
print(type([1, 2, 3]))           # List
print(type({'name': 'Mir'}))  # Dictionary
print(type({9.8, 3.14, 2.7}))    # Tuple
# Dictionary: 
i = {'goat':7,'dog':8,'elephant':9}
print(type(i))


# Find an Euclidean distance between (2, 3) and (10, 8)

p1=[2,3]
p2=[10,8]
distance = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
print("Euclidean distance between", p1, "and", p2, "is:", distance)
# answer: 9.433981132056603

import math
print(math.dist([2,3],[10,8]))