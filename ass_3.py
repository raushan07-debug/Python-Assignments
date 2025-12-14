
# Task 1


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result =result* i
    return result


num = 5
print("Factorial of", num, "is:", factorial(num))



# Task 2

import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
log_value = math.log(num)
sine_value = math.sin(num)

print("Square Root:", square_root)
print("Natural Logarithm:", log_value)
print("Sine:", sine_value)
